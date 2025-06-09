import pandas

mydataset = {
    'Car Brand': ['Toyota' , 'Nissan' , 'Honda'],   
    'Engine': [2.0 , 5.0 , 8.0]
}

test = pandas.DataFrame(mydataset, index=[1,2,3])

print(test)
