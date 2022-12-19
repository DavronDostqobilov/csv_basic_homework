def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    list1=data.split('\n')
   
    return len(list1[0].split(','))
f=open('data.csv','r')
a=f.read()
print(find_number_of_columns(a))
# Read the csv file