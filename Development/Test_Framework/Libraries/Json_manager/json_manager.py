import json


class json_manager():

    def __init__(self):
        pass

    def read_json_file(self, json_file_content):
        # parse json file into json object:
        return json.loads(json_file_content)

    def write_into_json_file(self, json_content):
        # convert json object into json file:
        return json.dumps(json_content, indent=4, separators=(", ", " = "))

    def print_json_content(self, printed_value):
        # print content
        print("the content of json file :\n", printed_value)


json_file_content = """{
  "name": "John",
  "age": 30,
  "city": "New York"
}"""
json_content = {
  "name": "Paul",
  "age": 40,
  "city": "Las Vegas"
}
json_manager = json_manager()
x = json_manager.read_json_file(json_file_content)
json_manager.print_json_content(x)
y = json_manager.write_into_json_file(json_content)
json_manager.print_json_content(y)