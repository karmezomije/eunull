import csv

def read_csv_to_list(file):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        log_temp = list(reader)
    return log_temp
