#!/usr/bin/python3

# Simple Local Network Scanner
# Author Taha Yildiz

import subprocess as sp
import platform
from netaddr import *
import argparse

try:
  def checkoscommand ():
    if platform.system() == "Windows":
      command = "ping -n 1 "
    else:
      command = "ping -c 1 "
    return command
  
  def pingsweap(command,address):
    network = IPNetwork(address)
    if network.size != 1 :
      for ip in IPNetwork(address).iter_hosts():
        status = sp.getstatusoutput(checkoscommand()+ str(ip))
        if status[0] == 0:
          print("System " + str(ip) + " is UP !")
        else:
          print("System " + str(ip) + " is DOWN !")      
    else:
      status = sp.getstatusoutput(checkoscommand()+ str(network[0]))
      if status[0] == 0:
        print("System " + str(network[0]) + " is UP !")
      else:
        print("System " + str(network[0]) + " is DOWN !")
  
  def main(argv):
    pingsweap(checkoscommand(),str(argv))
    
  if __name__ == '__main__':
  
    parser = argparse.ArgumentParser(description='Simple Local Network Scanner ')
    parser.add_argument('-i', help='Ex:192.168.1.5 or 192.168.1.0/24')
    args = parser.parse_args()
  
    if args.i == None or args.h == None:
      print("usage: pping.py [-h] [-i ip]")
    else:
      main(args.i)  

except KeyboardInterrupt:
  print("\nBY :)")

