import json
import os


class json_manager():

    def __init__(self):
        pass

    def read_json_file(self, json_file_path):
        # open json file
        json_file = open(json_file_path, "r")

        # read json file content
        json_file_content = json_file.read()

        # close json file
        json_file.close()

        # parse json file into json object:
        return json.loads(json_file_content)

    def write_into_json_file(self, json_file_path, json_content):
        # open json file
        json_file = open(json_file_path, "w")

        # convert json object into json file:
        json_file_content = json.dumps(json_content, indent=4, separators=(", ", " = "))

        # write json content into the file
        json_file.write(json_file_content)

        # close json file
        json_file.close()

    def print_json_file_content(self, json_file_path):
        # open json file
        json_file = open(json_file_path, "r")

        # read json file content
        json_file_content = json_file.read()

        # close json file
        json_file.close()

        # print content
        print("the content of json file :\n", json_file_content)

    def modify_node_json_file(self):
        pass

    def get_node_from_json_file(self):
        pass

    def remove_node_json_file(self):
        pass

    def create_json_file(self, json_file_path):

        json_content = {}

        if not os.path.exists(json_file_path):
            # open json file
            json_file = open(json_file_path, "w")

            # convert json object into json file:
            json_file_content = json.dumps(json_content, indent=4, separators=(", ", " = "))

            # write json content into the file
            json_file.write(json_file_content)

            # close json file
            json_file.close()
            print(f"The file {json_file_path} is created")
        else:
            print(f"The file {json_file_path} exist before")



    def delete_json_file(self, json_file_path):
        if os.path.exists(json_file_path):
            os.remove(json_file_path)
            print(f"The file {json_file_path} has been deleted")
        else:
            print(f"The file {json_file_path} does not exist")


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
File_path = "C:/Python repositry/Python/config.json"
File_path1 = "C:/Python repositry/Python/config1.json"
File_path2 = "C:/Python repositry/Python/config2.json"
json_manager = json_manager()
x = json_manager.read_json_file(json_file_path=File_path)
print(x)
json_manager.create_json_file(File_path2)
json_manager.write_into_json_file(json_file_path=File_path1, json_content=x)
json_manager.print_json_file_content(json_file_path=File_path1)
json_manager.delete_json_file(json_file_path=File_path1)
json_manager.delete_json_file(json_file_path=File_path2)
