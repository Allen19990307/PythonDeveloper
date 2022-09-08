import json
if __name__ == '__main__':
  with open('1.json','r') as jsonfile:
    json_string = json.load(jsonfile)
    print(json_string[1]["campaigns"][0]["discountId"]["$oid"])