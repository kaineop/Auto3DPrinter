"""
==========================================================
Copyright the Finn Ractliffe.
==========================================================


Codes to use (in first line of serial message):
1 -  execute command
2 - recieve info


-- Key --

E.g. message= 1select-file (Arduino will not recieve a response)
 message = 2print-progress (Arduino will recieve a serial msg response with information)

"""


def log_msg(code, dev, msg):
    print ("[" + dev + "] [" + code + "] : " + msg)

import serial


p = "/dev/t1" # Port from Linux
r = 9600 # Baud rate, u can try increase for a faster experience but wouldnt push it too much
active = True
print_status = ""

si = serial.Serial(p, r)
si.flushInput()

while active:
    # Recieving msgs
    if  si.inWaiting()>0:
        inp = si.readline()
        code = inp[:1]
        msg = inp[:2-15]
        dev = "Arduino"
        log_msg(code, dev, msg)
        if (msg == "select-print"):
            # select print
        elif (msg == "start-print"):
            # start print

    if (print_status == "done"):
        s1.write("print-done")




