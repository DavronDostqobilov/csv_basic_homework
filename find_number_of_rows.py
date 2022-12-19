def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    list1=data.split('\n')
    return len(list1)
f=open('data.csv','r')
a=f.read()
print(find_number_of_rows(a))

# Read the csv file
