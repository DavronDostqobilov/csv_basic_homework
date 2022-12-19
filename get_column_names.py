#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    list1=data.split('\n') 
    return list1[0].split(',')
f=open('data.csv','r')
a=f.read()
print(get_column_names(a))
    
# Read the csv file