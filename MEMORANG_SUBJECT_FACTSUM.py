1#Memorang Data Modifier



import csv



#MODIFY HERE

#SELECTION_COL = the number of the column you are performing data

#on ---> read left to right starting from 0

#BLOCK NUMBER = block number input

#COL TYPE = column type input for column titles

#FILE_OUTPUT = whatever you want the name of the file outputted

BLOCK_NUMBER = '1'

FILE_INPUT = 'FMS1_Clean.csv'

SUBJECT_FILTER = ['Gross Anatomy','Mircoanatomy','Genetics','Biostatistics','Biochemistry','SPP']





#creates dictionary data structure for easy manipulation

def construct_dict(dictionary, data, col_num, subject):



	rows = len(data)

	columns = len(data[0])


	for i in range(1,rows):


		row_subject = data[i][1]

		
		if (row_subject.find(subject) != -1) and (data[i][8] == "All"):
				
			dictionary_subject = subject
			curr_id = data[i][0]
			amount = int(data[i][col_num])


			boolean = False

			if curr_id in dictionary.keys():
				temp_list = dictionary.get(curr_id)
				for sublist in temp_list:
					if sublist[0] == subject:
						sublist[1] += amount
						boolean = True
						break

				if not boolean:
					temp_list.append([subject, amount])



			else:
				dictionary[curr_id] = [[subject, amount]]



	return dictionary



#Converts dictionary into 2d array

def create_table(dict):

	table = []



	#creates the column titles

	titles = []
	titles.append('MEDID')
	for subject in SUBJECT_FILTER:
		titles.append('1617_'+BLOCK_NUMBER+'_MM_factsStudied_'+subject)
			
		
	table.append(titles)



	#inputs row values

	for key in dict.keys():

		new_row = []
		new_row.append(key)
		tuples = dict.get(key)
		for t in tuples:
			new_row.append(str(t[1]))
			if t[0] == 'SPP':
				new_row.append(str(t[1]))
		table.append(new_row)



	return table



#writes 2d array into a csv

def write_output(table):

    with open('subjects.csv', 'w') as f:

    	

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



	new_dict = {}

	
	for subject in SUBJECT_FILTER:
		new_dict = construct_dict(new_dict, data, 4, subject)


	table = create_table(new_dict)

	write_output(table)






if __name__ == "__main__": main()