#!/usr/bin/env python

import subprocess
import sys


def main():
    modem_port = get_modem_port()
    print("Particle serial interface found at :" + modem_port)
    dfu_command = "stty -f " + modem_port + " 14400"
    returned_value = subprocess.run(dfu_command, shell=True)
    if returned_value.returncode == 0:
        print("Particle board at " + modem_port + " has been put in DFU mode.")


def get_modem_port():
    returned_value = subprocess.run("ls /dev/cu.usb*", stdout=subprocess.PIPE, shell=True)
    if returned_value.returncode == 1:
        print("No Particle board connected!")
        sys.exit(1)

    modem_port = str.strip(returned_value.stdout.decode("utf-8"))
    return modem_port


if __name__ == '__main__':
    main()
