import sys
import pandas as pd
import math

if(len(sys.argv) > 4):
	raw_data = pd.read_csv(sys.argv[1], low_memory = False)
	variables_file = open(sys.argv[2])

	variables_names = []
	variables_types = []
	for line in variables_file:
		name_type = line.split();
		variables_names.append(name_type[0])
		variables_types.append(name_type[1].replace('\n', ''))

	output = open(sys.argv[3], 'w')

	output.write('@RELATION ' + str(sys.argv[4]) + '\n\n')

	for i in range(0, len(variables_names)):
		output.write('@ATTRIBUTE ' + str(variables_names[i]) + ' ' + str(variables_types[i]) + '\n')

	output.write('\n@DATA\n')
	for index, row in raw_data.iterrows():
		line = ''
		for i in range(0, len(variables_names)):
			if(str(row[variables_names[i]]) != 'nan'):
				if(variables_types[i] == 'string'):
					line += '\"' + str(row[variables_names[i]]) + '\"'					
				else:
					line += str(row[variables_names[i]])
			else:
				if(variables_types[i] == 'string'):
					line += '\"nan\"'
				else:
					line += '0'
			#	break

			if(i < len(variables_names) - 1):
				line += ','

		if(line != ''):	
			output.write(line + '\n')


