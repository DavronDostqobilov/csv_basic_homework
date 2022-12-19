def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    x=data.split('\n')
    return x[0].split(',')
f=open('data.csv','r')
a=f.read()
print(get_first_column(a))
# Read the csv file