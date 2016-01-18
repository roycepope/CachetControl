__author__ = 'Royce'

import os
from time import sleep
from libs.CachetControl import CachetControl

mumble_log = '/var/log/mumble-server.log'


def tail(f, n):
    stdin, stdout = os.popen2("tail -n " + str(n) + " " + f + "|grep Authenticated")
    stdin.close()
    lines = stdout.readlines()
    stdout.close()
    return lines

monitoring = True
users = []

Cachet = CachetControl()
while monitoring:
    sleep(5)
    mumble_tail = tail(mumble_log, 3)
    print mumble_tail
    if mumble_tail:
        if users:
            if users[-1] == mumble_tail[-1]:
                print "Match!"
        else:
            users.append(mumble_tail[0])
            print "Point Sent"
            Cachet.mumbleMonitor()
    else:
        users = []