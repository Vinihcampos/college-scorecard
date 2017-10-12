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

	#for i in range(0, len(variables_names)):
	#	if(variables_types[i] == 'numeric'):
	#		raw_data[variables_names[i]] = (raw_data[variables_names[i]] - raw_data[variables_names[i]].mean())/raw_data[variables_names[i]].std(ddof=0)

	output.write('\n@DATA\n')
	for index, row in raw_data.iterrows():
		line = ''
		number_of_nan = 0
		for i in range(0, len(variables_names)):
			if(str(row[variables_names[i]]) != 'nan'):
				if(variables_types[i] == 'string'):
					line += '\"' + str(row[variables_names[i]]) + '\"'					
				else:
					#if(row[variables_names[i]] == 0):
					#	line += '0'
					#else:
					#	line += '1'
					line += str(row[variables_names[i]])
			else:
				number_of_nan += 1
				if(variables_types[i] == 'string'):
					line += '\"nan\"'
				else:
					line += '0'
			#	break
			if(i < len(variables_names) - 1):
				line += ','
		if(line != '' and number_of_nan < 0.5 * len(variables_names)):	
			output.write(line + '\n')


