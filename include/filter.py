
class DC_remover():
    def __init__(self, alpha: float = 0.95):
        self.prev_input = 0.0
        self.prev_output = 0.0
        self.prev_prev_input = 0.0
        self.prev_prev_output = 0.0
        self.alpha = alpha

    def block_data_DC_reomver(self, mic_array: list):
        avr_val = sum(mic_array)/len(mic_array)
        for i in range(len(mic_array)):
            mic_array[i] = mic_array[i] - avr_val
        return mic_array

    def kai_filter(self, x: float):
        y = self.alpha * x - self.alpha * self.prev_input - self.alpha * self.prev_output
        #y = self.alpha * x - self.alpha * self.prev_input + self.alpha * self.prev_output
        self.prev_output = y
        self.prev_input = x
        return y

    def nett_filter(self, x):
        y = x - self.prev_input + self.alpha * self.prev_output
        self.prev_output = y
        self.prev_input = x
        return y

    def nett_filter_andre_orden(self, x):
        y = (x - self.prev_input + self.prev_prev_input) + self.alpha * (self.prev_output - self.prev_prev_output)
        self.prev_output = y
        self.prev_input = x
        self.prev_prev_output = self.prev_output
        self.prev_prev_input = self.prev_input
        return y

#https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-gtd.2014.1150
