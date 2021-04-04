import requests
import pandas as pd
import re
y=0
r = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
result = []
with open("logs.txt", "w") as f:
    f.write(r.text)

with open("logs.txt", "r") as file_1:
  content_line = file_1.readline()
  while y!=7:
      content = re.split('-|"|HTTP', content_line)
      IP = content[0]
      request_type_material = re.split(" ", content[3])
      request_type = request_type_material[0]
      request_material = request_type_material[1]
      tuple_result = (IP, request_type, request_material)
      result.append(tuple_result)
      y +=1
print(result)





