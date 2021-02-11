class time_state_schedule:
    def __init__(self, times=[], states=[]):
        self.times = times
        self.states = states

class timesheet(time_state_schedule):
    def __init__(self, times=[], states=[]):
        time_state_schedule.__init__(self, times, states)

    def load_from_file(self, file_name):
        input_file = open(file_name, 'r')
        for line in input_file:
            values = line.split()
            self.times.append(int(values[0]))
            self.states.append(int(values[1], base=2))
        input_file.close()

    def get_next_time(self, time):
        current_time = time.tm_hour*100 + time.tm_min
        index = 0
        while self.times[index] <= current_time:
            if(index < (len(self.times) - 1)):
                index += 1
            else:
                index = 0
        return self.times[index]