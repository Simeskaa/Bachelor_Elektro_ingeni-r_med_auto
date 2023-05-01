import threading
import queue
from threading import Lock
import time
from copy import copy
import logging

q = queue.Queue()
lock = Lock()


def prod(lock):
    a = [1, 2, 3, 4, 5]
    counter = 0
    while True:
        curr_val = a[counter]
        logging.info("prod: About to ask for lock")
        with lock:
            logging.info("prod: Got lock")
            q.put(curr_val)
            logging.info(f'prod: Put {curr_val} in queue')
            logging.info("prod: About to let go of lock")
        logging.info("prod: lock is free")
        counter += 1
        if counter >= len(a):
            q.task_done()
            logging.info("prod: all tasks are done")
            break
        time.sleep(0.01)

def worker(lock):
    while True:
        logging.info("worker: About to ask for lock")
        with lock:
            logging.info("worker: Got lock")
            item = copy(q.get())
            logging.info(f'worker: Received {item} from queue')
            logging.info("worker: About to let go of lock")
        if item >= 5:
            q.task_done()
            logging.info("worker: Got 5, task done")
            break
        logging.info("worker: lock is free")
        time.sleep(0.02)




if __name__ == '__main__':
    # format for logging
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # Turning on threads
    t1 = threading.Thread(target=prod, args=(lock,), daemon=True)
    t2 = threading.Thread(target=worker, args=(lock,), daemon=True)
    t1.start()
    t2.start()
    # Wait for threads to finish
    t1.join()
    t2.join()
    logging.info("Main: Program finished")