import time
from serial import Serial
import subprocess

def find_first_space(data):
    ans = -1
    for i in range(len(data)):
        if(data[i] == " "):
            ans = i
            break
    return ans

def find_port_auto():
    output = ""

    try:
        output = subprocess.check_output("arduino-cli board list | grep Arduino", shell=True)
    except subprocess.CalledProcessError:
        output = ""

    if(str(output) != ""):
        output = str(output)
        output = output[2:]

        tmp = output.index(' ')

        output = output[:tmp]
    
    return str(output)

def open_serial_port():
    port_path = find_port_auto()

    if(port_path != ""):
        port = Serial(port_path, 9600, timeout=0)
        while(port.inWaiting() <= 0):
            pass
        port.read()
        return port
    else:
        return None
