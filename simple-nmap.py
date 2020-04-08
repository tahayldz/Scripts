# !/usr/bin/python3

#Simple nmap 
#Author Taha Yildiz

import nmap
import re
import os
import argparse
import urllib3

class Tarama:
	def __init__(self):
		self.cmd_arg = "-n -Pn -sS -sV -T4 --top-ports 10"
		self.nmap_services_file = "/usr/share/nmap/nmap-services"
		self.nm = nmap.PortScanner()

	def get_service_name(self, port, proto):
		nmap_file = open(self.nmap_services_file,"r")
		service = ""
		for line in nmap_file:
				if re.search("([^\s]+)\s%d/%s\s"% (port, proto), line):
					service = re.search("([^\s]+)\s%d/%s\s"% (port, proto), line).groups(1)[0]
					break
		return service


	def run_scan(self,targets):
		self.nm.scan(hosts = "%s"% targets, arguments = "%s"% self.cmd_arg)


		for host in self.nm.all_hosts():
			print("Domain adresi\n",host)
			print("PORT     STATE     SERVICE")
			for proto in self.nm[host].all_protocols():
				result = self.nm[host][proto].keys()
				sorted(result)

				for port in result:
						res = str(port) + "/" + proto
						space = str(" " * (9 - len(res)))
						service = self.get_service_name(port, proto)
						state = self.nm[host][proto][port]['state']
						space2 = str(" " * (10 - len(state)))
						print("%s/%s%s%s%s%s" % (port,proto,space,state,space2,service))





if __name__ == "__main__":	


	parser = argparse.ArgumentParser(description='Simple Local Network Scanner ')
	parser.add_argument('-i', help='Ex:192.168.1.5 or 192.168.1.0/24')
	args = parser.parse_args()

	if args.i == None:
		print("Usage: simple-nmap.py [-h] [-i IP]")
	else:
		if os.geteuid() ==0 	: 
			try:
				tarama = Tarama()
				tarama.run_scan(args.i)
			except KeyboardInterrupt:
				print("\nBY :)")
		else:
			print("root yetkisi lazim :)")