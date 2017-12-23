import json

with open('myjson.json') as file:
    # json file => dict
    my_dict = json.load(file)
    print(my_dict['result']['name'])

    file.close()

# json string => dict
json_str = '{"result": {"name": "Doa2", "age": 34}}'
my_dict2 = json.loads(json_str)
print(my_dict2['result']['name'])


# dict => json string
my_json = json.dumps(my_dict2)
print(my_json)

with open('myjson2.json', 'w') as file:
    # dict => json file
    json.dump(my_dict2, file)
    
    file.close()
