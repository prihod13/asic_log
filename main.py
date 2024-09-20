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












