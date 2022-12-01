import requests
import random
import string
import csv
from config import *

geturl = "https://app.ecwid.com/api/v3/39150140/discount_coupons?token="+token
posturl = "https://app.ecwid.com/api/v3/39150140/discount_coupons"


# # get all codes from ecwid shop
# headers = {
#     "Accept": "application/json",
#     "Authorization": "Bearer "+token
# }

# response = requests.get(geturl, headers=headers).json()
# json_data = json.dumps(response, indent=4, ensure_ascii=True)
# print(json_data)
# # print(response.text)

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer "+token,
    "Content-Type": "application/json"
}

schoolID = ""   # get schoolID as variable -> gui?
count = 10      # how many codes should be uploaded to ecwid
number = 5      # how many letters in code
i = 0

with open('pbcodes.csv', 'w') as file:
    writer = csv.writer(file)
    header = ['Codes']
    writer.writerow(header)

file.close()

j = 0

# without 0 and O and I
# main loop
while True:
    name = "PB2022-"+str(schoolID) # set name of coupon
    code = ''.join(random.choices(string.ascii_uppercase+string.digits, k=number)) # set number of letters
    data = [code.upper()]
    if str(0) in data[0] or "O" in data[0] or "I" in data[0]:
        pass
    else:
        print(name, code)
        payload = {
        "name": name,
        "code": code,
        "discountType": "ABS",
        "status": "ACTIVE",
        "discount": 28,
        "usesLimit": "ONCEPERCUSTOMER",
        "applicationLimit": "UNLIMITED",
        "orderCount": 0,
        "catalogLimit": {
            "products": [],
            "categories": [
                64275257
                ]
            }
        }
        # ecwid api post json
        response = requests.post(posturl, json=payload, headers=headers)
        print(response.status_code)
        print(response.ok)
        print(response.text, "\n")
        with open('pbcodes.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        j += 1
    if j == count:
        print('Job done!')
        break
file.close()
exit(0)

# with 0 and O and I
for i in range(count):
    name = "PB2022-"+str(schoolID) # set name of coupon
    code = ''.join(random.choices(string.ascii_uppercase+string.digits, k=number)) # set number of letters
    data = [code.upper()]
    print(name, code)
    payload = {
        "name": name,
        "code": code,
        "discountType": "ABS",
        "status": "ACTIVE",
        "discount": 28,
        "usesLimit": "ONCEPERCUSTOMER",
        "applicationLimit": "UNLIMITED",
        "orderCount": 0,
        "catalogLimit": {
            "products": [],
            "categories": [
                64275257
            ]
        }
    }

    # response = requests.post(posturl, json=payload, headers=headers)
    # print(response.status_code)
    # print(response.ok)
    # print(response.text, "\n")
    # with open('pbcodes.csv', 'a') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(data)
    i += 1
    if i == count:
        print('Job done!')
        break
# file.close()