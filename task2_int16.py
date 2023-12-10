from bs4 import BeautifulSoup
import json


PATH_CONST_HTML = r"Write your path here (only .html report)"
PATH_CONST_JSON = r"Write your path here (only .json report)"

'''
Парсер .html был написан из-за незнания, что отчет может быть и в формате JSON
Однако убирать его не стал - труды все равно потрачены :)
'''

def parse_vulnerabilities_report_html(path: str) -> None:
    
    html_report = open(path, 'r', encoding="utf-8")

    html_code = html_report.read()

    soup = BeautifulSoup(html_code, features="html.parser")
    
    tbody = soup.findAll("tbody")
    tbody = tbody[2]
    
    names = [vulner.get_text() for vulner in tbody.findAll("th")]
    names_count = [int(count.get_text()) for count in tbody.findAll("span") if not(count.has_attr("class"))]

    parsed_data = {"vulnerabilities": []}

    for ind in range(len(names)):
        parsed_data["vulnerabilities"].append({"name": names[ind], "count": names_count[ind]})

    with open("vulnerability_report_html_test.json", "w") as dump:
        dump.write(json.dumps(parsed_data, indent=4))


#parse_vulnerabilities_report_html(PATH_CONST_HTML)


def parse_vulnerabilities_report_json(path: str) -> None:

    raw_data = []
    with open(path, 'r') as file:
        raw_data = json.load(file)

    parsed_data = {}
    for host in raw_data["site"]:
        alerts_list = host["alerts"]
        for alert in alerts_list:
            if alert["name"] in parsed_data:
                parsed_data[alert["name"]] += int(alert["count"])
            else:
                parsed_data[alert["name"]] = int(alert["count"])

    dump_data = {"vulnerabilities": []}
    with open("vulner_report_json_test.json", "w") as dump:
        for vulnerability, instance in parsed_data.items():
            dump_data["vulnerabilities"].append({"name": vulnerability, "count": instance})

        dump.write(json.dumps(dump_data, indent=4))



#parse_vulnerabilities_report_json(PATH_CONST_JSON)