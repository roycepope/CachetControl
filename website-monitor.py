__author__ = 'Royce'

import os
import re
import sys
import subprocess
from time import sleep
from libs.CachetControl import CachetControl

url = 'status.overlook.sh'
NoOfPackets = 5
timeout = 3600  # in milliseconds


def ping(url):
    response = os.system("ping -c 1 " + url)

    if response == 0:
        return True
    else:
        return False

def systemCommand(Command):
    Output = ""
    error = ""
    try:
        Output = subprocess.check_output(Command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        #Invalid command raises this exception
        error = e.output

    if Output:
        Stdout = Output.split("\n")
    else:
        Stdout = []
    if error:
        Stderr = error.split("\n")
    else:
        Stderr = []

    return Stdout, Stderr

if __name__ == "__main__":
    monitoring = True
    users = []

    try:
        Cachet = CachetControl()
        Components = Cachet.getComponenets()
        for component in Components:
            if 'website' or "Website" in component['name']:
                component_id = component['id']
    except Exception as e:
        component_id = ""
        print e
        sys.exit(1)

    # Build the ping command based on OS
    if sys.platform == 'win32':
        Command = 'ping -n {0} -w {1} {2}'.format(NoOfPackets, timeout, url)
    if sys.platform == 'darwin':
        Command = 'ping -c {0} -t {1} {2}'.format(NoOfPackets, timeout, url)
    else:
        Command = 'ping -c {0} -w {1} {2}'.format(NoOfPackets, timeout, url)
    while monitoring:
        Stdout, Stderr = systemCommand(Command)

        #print Stdout, Stderr
        if Stdout:
            print "Host [{}] is reachable.".format(url)
            Cachet.setComponent(component_id, 1)
            for line in Stdout:
                if 'loss' in line:
                    loss = line.split(',')[-1].split(' loss')[0]
                    loss = re.findall(r"[-+]?\d*\.\d+|\d+", loss)
        else:
            print "Host [{}] is unreachable.".format(url)
            Cachet.setComponent(component_id, 4)
        sleep(30)
