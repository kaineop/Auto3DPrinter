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

import sys


sys.argv.extend(['--port', 5000])
sys.argv.extend (['--host', "192.168.2.58"])
sys.argv.extend(['--apikey', "a"])


from controller import OctoprintAPI as cmd


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
            cmd.select_file("/path")
        elif (msg == "start-print"):
            cmd.start_job()

    if (cmd.get_printer_status() == "done"):
        s1.write("print-done")




