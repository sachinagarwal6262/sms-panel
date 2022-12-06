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
def get_not_found_circle(cir_file):
    N_F_cir=[]
    with open(cir_file, mode ='r')as file:
        # reading the CSV file
        csvFile_cir = csv.reader(file)
        # displaying the contents of the CSV file
        for lines in csvFile_cir:
            N_F_cir.append(*lines)
    return N_F_cir

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
    N_F_cir_list=[]
    N_not_F_cir_list=[]

    #Get JSON DATA
    data = get_circle_data()

    #list of CSV File
    csv_file_list=['tbl_statistics_Not_Found_circle_series_record.csv','tbl_whistle_combined_Not_Found_circle_series_record.csv','user_master_Not_Found_circle_series_record1.csv']

    #Loop each CSV file 
    for file in csv_file_list:
        result_data = get_not_found_circle(file)
        #print(len(result_data))
        result_csv_data.extend(result_data)

    N_F_cir = list(set(result_csv_data))

    for j in N_F_cir:
        if j in data:
            N_F_cir_list.append([j,data[j]['circle']])
        else:
            N_not_F_cir_list.append([j])
    
    print("circle Matched",len(N_F_cir_list))
    print("circle Not Matched",len(N_not_F_cir_list))

    #write CSV file for all found and not found series data
    write_csv('found_series_circle.csv',N_F_cir_list)
    write_csv('not_found_series_circle.csv',N_not_F_cir_list)

    print("Script Executed")

if __name__ == '__main__':
    main_function()        
