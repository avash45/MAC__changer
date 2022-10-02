#!/usr/bin/env python

import subprocess
import optparse
import re

from re import RegexFlag
from types import new_class
from optparse import OptionParser

def get_arguements():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New mac address")
    (options,arguements)=parser.parse_args()
    if not options.interface:
        parser.error("[-]Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("Please specify a new mac address, use --help for more info.")
    else:
        return (options, arguements)

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_results=subprocess.check_output(["ifconfig", interface])

    mac_address_search_result=re.search( rb'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_results)
    mac_address_search_result=mac_address_search_result
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("\nCouldn't read the mac address")

print("\n")
(options,arguements)=get_arguements()
given_mac="b'"+options.new_mac+"'"

old_mac=str(get_current_mac(options.interface))
print("Current MAC- "+old_mac)

change_mac(options.interface, options.new_mac)

new_current_mac=str(get_current_mac(options.interface))
print("New MAC- "+new_current_mac)

if given_mac == new_current_mac:
    print("\n [+] MAC address was successfully changed to "+new_current_mac)
else:
    print("\n[-] MAC address did not get changed")
