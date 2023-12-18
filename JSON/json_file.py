import json
with open("sample.json") as f:
    python_dict = json.load(f)
print(python_dict)

for key,value in python_dict.items():
    print(key," is ", value)