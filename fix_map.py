import json

classes = json.load(open('model/classes.json'))

with open('pesticide_map.py', 'w', encoding='utf-8') as f:
    f.write("# pesticide_map.py\n\n")
    f.write("DISEASE_INFO = {\n")
    for c in classes:
        common = c.replace("___", " - ").replace("_", " ")
        f.write(f'    "{c}": {{"common": "{common}", "scientific": "Pending", "pesticide": "Consult agronomist"}},\n')
    f.write("}\n\n")
    f.write("def get_disease_info(disease_class):\n")
    f.write("    return DISEASE_INFO.get(disease_class, {\n")
    f.write('        "common": disease_class.replace("___", " ").replace("_", " "),\n')
    f.write('        "scientific": "Unknown",\n')
    f.write('        "pesticide": "Consult local agronomist"\n')
    f.write("    })\n")

print("pesticide_map.py has been completely rewritten with exact keys!")