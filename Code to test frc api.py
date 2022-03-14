import requests
import base64
import json

f = open("C:\\Users\\gamin\\OneDrive\\Documents\\Code\\Frcbot\\config.json",)
config_file = json.load(f)
authy = config_file["key_frc"]

url = "https://frc-api.firstinspires.org/v3.0/2022/rankings/district?districtCodeONT=&teamNumber=865"

#key = base64.b64encode(key_frc.encode('ascii'))
payload={}
headers = {
  'Authorization': 'Basic' + str(authy),
  'If-Modified-Since': ''
}

response = requests.request("GET", url, headers=headers, data=payload)
print(authy)
print(response.text.replace(",","\n" ))
print(response)