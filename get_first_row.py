def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   list1=data.split('\n')
   return list1[1].split(',')
f=open('data.csv','r')
a=f.read()
print(get_first_row(a))
# Read the csv file