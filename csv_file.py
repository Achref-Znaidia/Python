import io

class csv_file:
    csv_path = "template_concept.csv"
    csv_content = ""
    csv_requirement = []
    csv_TcType = ""
    csv_api_availability = ""
    csv_deployment = ""
    csv_undeployment = ""

    def __init__(self, csv_path):
        self.csv_path = csv_path

    def get_content(self):
        self.csv_content = io.open(self.csv_path,'r').read()
        return self.csv_content

