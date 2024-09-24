import json



file= "asic_log.json"

with open(file, "r") as f:
     data = json.load(f)
     for p in data['STATS']:
          print(p['rate_5s'])
          print(p['rate_30m'])
          print(p['rate_avg'])
          print(p['fan'])
          print(p['chain'])



import subprocess

URL = "http://192.186.1.20"

comand= "ping 192.168.1.20"

status = subprocess.run(['ping', '-c', '2', '-n', '192.168.1.20'],
                            stderr=subprocess.PIPE, encoding='utf-8')

#print(status.stderr)






