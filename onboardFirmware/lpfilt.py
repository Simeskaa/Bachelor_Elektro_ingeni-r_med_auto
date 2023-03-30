prev_input = 0.0
prev_output = 0.0
alpha = 0.99


def filter_sample(x):
    global prev_input, prev_output
    y = alpha*x - alpha*prev_input - alpha*prev_output
    prev_output = y
    prev_input = x
    return y

