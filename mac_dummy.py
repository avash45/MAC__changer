#!/usr/bin/env python

import subprocess
from types import new_class
interfacess=input("Enter the interface you want: ")
new_mac=input("Enter the new MAC address: ")

subprocess.call(["ifconfig", interfacess, "down"])
subprocess.call(["ifconfig", interfacess, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interfacess, "up"])
subprocess.call(["ifconfig"])