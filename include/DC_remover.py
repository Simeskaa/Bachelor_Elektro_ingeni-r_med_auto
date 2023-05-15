class DC_remover():
    def __init__(self):
        self.prev_input = 0.0
        self.prev_output = 0.0
        self.alpha = 0.5

    def mean_value_filter(self, mic_array:list):
        avr_val = sum(mic_array)/len(mic_array)
        # removing the average value from each index
        for i in range(len(mic_array)):
            mic_array[i] = mic_array[i] - avr_val
        return mic_array

    def lp_filter_start(self, mic_array:list):
        mic_array_out = []
        for i in mic_array:
            mic_array_out.append(self.lp_filter(i))
        return mic_array_out

    def lp_filter(self, x):
        y = self.alpha * x - self.alpha * self.prev_input - self.alpha * self.prev_output
        self.prev_output = y
        self.prev_input = x
        return y
