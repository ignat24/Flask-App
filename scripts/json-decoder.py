import json
import subprocess as sp

with open('secrets.json', 'r') as file:
  data = json.load(file)

decode_mas={}

for key in data:
    decode = sp.getoutput("echo " + data[key] + " | base64 --decode")
    decode_mas[key]=decode


with open("secrets-decode.json", "w") as file:
    json.dump(decode_mas, file, indent=2)



