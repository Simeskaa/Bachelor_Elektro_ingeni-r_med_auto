class DC_remover():
    def mean_value_filter(self, mic_array:list):
        avr_val = sum(mic_array)/len(mic_array)
        # removing the average value from each index
        for i in range(len(mic_array)):
            mic_array[i] = mic_array[i] - avr_val
        return mic_array

