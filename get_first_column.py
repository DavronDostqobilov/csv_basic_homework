def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    list1=[]
    data=data.split('\n')
    for i in data:
        
        list1.append(i.split(',')[1])
    return list1
f=open('data.csv','r')
a=f.read()
print(get_first_column(a))
# Read the csv file