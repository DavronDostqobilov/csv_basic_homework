import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    
    k=len(list(data)[0])
    return k
f=open('data.csv','r')
a=csv.reader(f)
print(find_number_of_columns(a))
# Read the csv file