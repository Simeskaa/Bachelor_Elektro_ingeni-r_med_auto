import concurrent.futures

from include.direction_and_distance_estimation import angle_cord_estimation as ace
#from include.signal_processing import processing
from include.UDP_class import UDP
from include.Pipeline import Pipeline
import json
import threading
import time
import logging


buffer_size = 1024
SENTINEL = object()


def producer(pipeline, event):
    """ Recieving a message from the network """
    while not event.is_set():
        inc_msg = recv()
        logging.info("Producer got message: %s", inc_msg)
        pipeline.set_message(inc_msg, "Producer")

    logging.info("Producer received EXIT event. Exiting")


def consumer(pipeline, event):
    """Saving data to a database"""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            "Consumer storing message: %s  (queue size=%s)",
            message,
            pipeline.qsize(),
        )

    logging.info("Consumer received EXIT event. Exiting")

def recv():
    msg = UDP.get_message(65508)
    inc_msg = json.loads(msg)
    return inc_msg


if __name__ == "__main__":
    formt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formt, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    UDP = UDP(ip_adress="192.168.0.69", port=5004, receive_msg=True)
    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()








