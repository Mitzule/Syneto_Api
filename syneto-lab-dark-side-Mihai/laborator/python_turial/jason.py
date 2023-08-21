import json

with open("lab4.json") as json_file: #default is "r"
    
    # content = json_file.read()
    # print(json.loads(contant))
    
    print(json.load(json_file))
    
my_dict = {
    "jan" : 1, 
    "feb" : 2
}

my_js = json.dumps(my_dict)

with open("example.json", "w") as json_file:
    json_file.write(my_js)
    
