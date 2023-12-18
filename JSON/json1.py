import json
json_str = '{"subject": "cyberquare","grade":10}'
python_dict = json.loads(json_str)
print("JSON String is : ", json_str)
print("python dictionary is: ", python_dict)
print(python_dict["subject"])
