import time
from serial import Serial
import class_definitions
import functions as f

if __name__ == '__main__':
    port = f.open_serial_port()

    if(port != None):
        timesheet = timesheet()
        timesheet.load_from_file("timesheet.txt")
       
        current_time = time.localtime()
        next_time = timesheet.get_next_time(current_time)
        print("next time:", next_time)

        time_slot = timesheet.times.index(next_time) - 1

        current_state = timesheet.states[time_slot]
        port.write(chr(current_state).encode())
        print("initial state:", current_state)

        while True:
            #print("current_time:", current_time.tm_hour*100 + current_time.tm_min)
            #print("next_time:", next_time)
            current_time = time.localtime()
            time_num = current_time.tm_hour*100 + current_time.tm_min
            if time_num >= next_time:
                print("event reached")
                if (time_slot > (len(timesheet.times) - 1)):
                    time_slot += 1
                else:
                    time_slot = 0
                current_state = timesheet.states[time_slot]
                print("new state:", current_state)
                next_time = timesheet.times[time_slot]
                print(next_time)
                port.write(chr(current_state).encode())
            time.sleep(0.5)
    else:
        print("No Ports Found!")