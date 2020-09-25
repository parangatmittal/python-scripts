import json

input_file = 'data.txt'

json_format = {}

with open(input_file) as fh:
	for line in fh:
		heading, info = line.strip().split(None, 1)
		json_format[heading] = info.strip()

output_file = open("out.json", "w")
json.dump(json_format, output_file, indent=4, sort_keys=False)
output_file.close()
