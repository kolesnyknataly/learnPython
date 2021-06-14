import json
import xmltodict as xmltodict

with open('dataset.xml', encoding='utf-8') as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

    filtered_records = []
    for record in data_dict['dataset']['record']:
        if record['score'] is not None and int(record['score']) > 500 and record['gender'] == 'Female':
            filtered_records.append(record)

    filtered_records_with_root = {'dataset': {'record': filtered_records}}
    json_data = json.dumps(filtered_records_with_root, indent=4, ensure_ascii=False)

    with open('dataset.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)
        json_file.close()

with open('dataset.json', encoding='utf-8') as json_file2:
    json_data2 = json.load(json_file2)
    data_dict2 = xmltodict.unparse(json_data2, pretty=True)

    with open('NEWdataset.xml', 'w', encoding='utf-8') as new_xml_file:
        new_xml_file.write(data_dict2)
        new_xml_file.close()
