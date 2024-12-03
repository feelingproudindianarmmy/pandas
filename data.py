import pandas
mydataset={
    'cars':["BMW","VOLVO","FORD"],
    'passing':[1,2,3]
}
my=pandas.DataFrame(mydataset)
print(my)
hop=pandas.Series(mydataset,index=["car1","car2","car3"])
print(hop)


