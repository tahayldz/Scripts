import csv
import sys
import os
import subprocess
'''
email:hash:plain formatli bir dosyayi duzenleyerek mongodb'de collection olarak ekler.
ornek dosya girdisi
    tahayldz@gmail.com:bf49ab6b38b77362aa4a93afa98b53ffb697eb2ab427d2da27a6526595e893f9:naber
'''

mongo_db = "leakScraper"
out_file = "cleanLeak.csv"
fileIndex = []
def format(fileName,leakName):
    if os.path.exists(out_file):
    	os.remove(out_file)
    with open(fileName,'r') as file:   
        lines = file.readlines()
        for i in lines:
            s = i.strip().replace('"', '""').split(":")
            if len(s) >= 3:
                em = s[0].split("@")
                prefix = em[0]
                domain = em[1]
                plain = "".join(s[2:])
                hashed = s[1]
                delimiter = ','
                fd2 = open(out_file, "a")
                fd2.write(leakName + delimiter + prefix + delimiter  + domain  + delimiter  + hashed  + delimiter  + plain +"\n")
                fd2.close()

def mongoCollection():
    cmd = ["mongoimport","-d",mongo_db,"-c","credentials","--type","csv","--file",out_file,"--fields","l,p,d,h,P", "--numInsertionWorkers","8"]
    subprocess.call(cmd)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : importer.py leakName <creds.txt>")
        print("Example : importer.py tumblr tumblr.txt")
        exit()
    leakName = sys.argv[1]
    fileName = sys.argv[2]
    format(fileName,leakName)
    mongoCollection()
