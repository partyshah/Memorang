1#Memorang Data Modifier

import csv

#MODIFY HERE
#SELECTION_COL = the number of the column you are performing data
#on ---> read left to right starting from 0
#BLOCK NUMBER = block number input
#COL TYPE = column type input for column titles
#FILE_OUTPUT = whatever you want the name of the file outputted

BLOCK_NUMBER = '1'
COL_TYPE = ['sessions', 'factsStudied', 'overallAccuracy', 'mcFacts', 'fcFacts']
FILE_INPUT = 'FMS1_Clean.csv'
SUBJECT_FILTER = "SPP"
SUBJECT_FILTER_TITLE = "spp"


#creates dictionary data structure for easy manipulation
def construct_dict(data, col_num):

	rows = len(data)
	columns = len(data[0])
	dictionary = {}



	for i in range(1,rows):
		#columns where Folder = "All"
		subject = data[i][1]

		if (subject.find(SUBJECT_FILTER) != -1) & (data[i][8] == "All"):

			curr_id = data[i][0]
			date = data[i][2]
			amount = data[i][col_num]

			if curr_id in dictionary.keys():
				temp_list = dictionary.get(curr_id)
				temp_list.append([date, amount])

			else:
				dictionary[curr_id] = [[date, amount]]

	return dictionary

#Converts dictionary into 2d array
def create_table(dict, col_name):
	table = []

	#creates the column titles
	for key in dict.keys():
		titles = []
		titles.append('MEDID')
		dates = dict.get(key)
		counter = 1
		for d in dates:
			append_val = str(counter)

			titles.append('1617_'+ BLOCK_NUMBER + '_MM_' + SUBJECT_FILTER + "_" + col_name + '_day' + append_val)
			counter += 1
		break

	table.append(titles)

	#inputs row values
	for key in dict.keys():
		new_row = []
		new_row.append(key)
		tuples = dict.get(key)
		for t in tuples:
			new_row.append(t[1])
		table.append(new_row)

	return table

#writes 2d array into a csv
def write_output(table, name):
    with open(name + "_" + SUBJECT_FILTER_TITLE + "_" + BLOCK_NUMBER + '.csv', 'w') as f:
    	
    	for sublist in table:
    		for item in sublist:
    			f.write(item + ',')
    		f.write('\n')

#Reads in a csv and puts into a 2d array
def read_in():
	data = []
	with open(FILE_INPUT) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			data.append(row)

	return data

#Calls methods in appropriate order 
def main():
	data = read_in() #read file


	counter = 3
	for name in COL_TYPE:
		new_dict = construct_dict(data, counter)
		table = create_table(new_dict, name)
		write_output(table, name)
		counter += 1


if __name__ == "__main__": main()