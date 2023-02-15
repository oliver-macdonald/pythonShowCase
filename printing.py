doggyNames=["daisy","teddy","velma","vector"]
humanNames=["daisy","teddy","victor","vector","Victorea"]
ingrediants=["flour", "eggs", "salt"]

def listFilter(filterList,filterBy):
    for listItem in filterList:
        if listItem[0].lower() ==filterBy:
            print(listItem)

print("filter by e on ingrediants" )         
listFilter(ingrediants,"e")
print("______________________________")
print("filter by v")         
listFilter(doggyNames,"v")
print("______________________________")
listFilter(humanNames,"v")
print("\n")
print("filter by d")  
listFilter(doggyNames,"d")
print("______________________________")
listFilter(humanNames,"d")