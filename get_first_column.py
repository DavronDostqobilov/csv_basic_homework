def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    id=[]
    x=data.split('\n')
    for i in x:
        id.append(i.split(',')[0])
    return id
f=open('data.csv','r')
a=f.read()
print(get_first_column(a))
# Read the csv file