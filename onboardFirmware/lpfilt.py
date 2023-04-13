class base_filter:
    def __init__(self):
        self.prev_input = 0.0
        self.prev_output = 0.0
        self.alpha = 0.99

    def filter_sample(self, x):
        y = self.alpha * x - self.alpha * self.prev_input - self.alpha * self.prev_output
        self.prev_output = y
        self.prev_input = x
        return y

