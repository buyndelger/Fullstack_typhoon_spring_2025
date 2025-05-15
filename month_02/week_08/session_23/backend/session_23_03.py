import json


data= {
    "name":"Jonh",
    "age":30,
    "city": "New York",
    "langusges": ["Python", "JavaScript" "SQL"],
    "is_employee": True,
    "address": {"street": "123 Main St ","zip":"10001"} 

}
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)


json_string =json.dumps(data, indent=4)
print(json_string)



parsed_data =json.loads(json_string)
print(parsed_data["name"])
