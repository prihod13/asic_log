from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth,HTTPDigestAuth
import requests
import json
import time


def time_pg():
    named_tuple = time.localtime()  # получить struct_time
    time_string = time.strftime("log_time# %H:%M:%S ___ %D ", named_tuple)

    return str(time_string)



user ='root'
password='root'
hostname='http://192.168.1.20/cgi-bin/stats.cgi'

auth = requests.get(hostname, auth=HTTPDigestAuth(user, password))
print(auth)
#auths='http://192.168.1.20/cgi-bin/stats.cgi'



soup = BeautifulSoup(auth.text,'html.parser')
#print(soup)


file= "asic_log.json"
file_log_ubuntu = "file_log_ubuntu"
with open(file, "w+") as f:
    f.write(str(soup))

with open(file_log_ubuntu, "a+") as f:
    f.write(time_pg() + str(soup))




with open(file, "r") as f:
    data = json.load(f)
    for p in data['STATS']:
        print(p['rate_5s'])
        print(p['rate_30m'])
        print(p['rate_avg'])
        print(p['fan'])
        print(p['chain'])





