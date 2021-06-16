import json
import sys

import xmltodict

utf8_string = 'utf-8'

file_path_argument = sys.argv[1]
filter_argument = None if len(sys.argv) < 3 else sys.argv[2].replace("-", "")


def xml_to_json():
    with open(file_path_argument, encoding=utf8_string) as xml_file:
        if filter_argument is None:
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict, indent=4, ensure_ascii=False)
            with open('dataset_output.json', 'w', encoding=utf8_string) as output_json_file:
                output_json_file.write(json_data)
        elif filter_argument == "f":
            data_dict = xmltodict.parse(xml_file.read())
            filtered_records = []
            for record in data_dict['dataset']['record']:
                if record['score'] is not None and int(record['score']) > 500 and record['gender'] == 'Female':
                    filtered_records.append(record)
            filtered_records_with_root = {'dataset': {'record': filtered_records}}
            json_data = json.dumps(filtered_records_with_root, indent=4, ensure_ascii=False)
            with open('filtered_dataset_output.json', 'w', encoding=utf8_string) as output_json_file:
                output_json_file.write(json_data)
        else:
            print('Invalid filter argument: ' + filter_argument)


def json_to_xml():
    with open(file_path_argument, encoding=utf8_string) as json_file:
        if filter_argument is None:
            json_data = json.load(json_file)
            data_dict = xmltodict.unparse(json_data, pretty=True)
            with open('dataset_output.xml', 'w', encoding=utf8_string) as output_xml_file:
                output_xml_file.write(data_dict)
        elif filter_argument == "f":
            json_data = json.load(json_file)
            filtered_records = []
            for record in json_data['dataset']['record']:
                if record['score'] is not None and int(record['score']) > 500 and record['gender'] == 'Female':
                    filtered_records.append(record)
            filtered_records_with_root = {'dataset': {'record': filtered_records}}
            data_dict = xmltodict.unparse(filtered_records_with_root, pretty=True)
            with open('filtered_dataset_output.xml', 'w', encoding=utf8_string) as output_xml_file:
                output_xml_file.write(data_dict)
        else:
            print('Invalid filter argument: ' + filter_argument)


if file_path_argument.lower().endswith('.xml'):
    xml_to_json()
elif file_path_argument.lower().endswith('.json'):
    json_to_xml()
else:
    print('Invalid file extension')
