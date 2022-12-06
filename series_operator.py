#import config as Config
import json
import csv

# Function to get circle & operator data
def get_circle_data():
    """ Function to return json format data of circle and operator
    1. Read ./circle_mobile.json file
    2. return the json data
    """
    #json_file = Config.CIRCLE_OPERATOR_JSON_PATH + 'circle_mobile.json'
    json_file='/home/sachin/Documents/whistle/sms-panel-utililties/circle_mobile.json'
    with open(json_file) as f:
        data = json.load(f)
    return data

#Function to read CSV File data
def get_not_found_operator(op_file):
    N_F_op=[]
    with open(op_file, mode ='r')as files:
        # reading the CSV file
        csvFile_op = csv.reader(files)
        # displaying the contents of the CSV file
        for li in csvFile_op:
            N_F_op.append(*li)
    return N_F_op

#Function to write CSV File in "append" mode
def write_csv(filename,file_data):
    # writing to csv file 
    with open(filename, 'a') as csvfile:
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile)
        # writing the data
        csvwriter.writerows(file_data)

def main_function():
    result_csv_data=[]
    N_F_op_list=[]
    N_not_F_op_list=[]

    #Get JSON DATA
    data = get_circle_data()

    #list of CSV File
    csv_file_list=['tbl_statistics_Not_Found_operator_series_record.csv','tbl_whistle_combined_Not_Found_operator_series_record.csv','user_master_Not_Found_operator_series_record1.csv']
    
    #Loop each CSV file 
    for file in csv_file_list:
        result_data = get_not_found_operator(file)
        #print(len(result_data))
        result_csv_data.extend(result_data)

    N_F_op = list(set(result_csv_data))

    for i in N_F_op:
        if i in data:
            N_F_op_list.append([i,data[i]['operator']])
        else:
            N_not_F_op_list.append([i])

    print("op Matched",len(N_F_op_list))
    print("op Not Matched",len(N_not_F_op_list))

    #write CSV file for all found and not found series data
    write_csv('found_series_operator.csv',N_F_op_list)
    write_csv('not_found_series_operator.csv',N_not_F_op_list)

    print("Script Executed")

if __name__ == '__main__':
    main_function()