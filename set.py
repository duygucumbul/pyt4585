# .set() => içerisinde uniq değer tutar yani aynı elemandan 2. bir eleman barındırmaz 3. barınmaz 

mySet = set()

print (mySet) 

mySet.add(1) 
print (mySet) 

mySet.add(1) 
mySet.add(2) 
mySet.add(3) 

print(len(mySet ))
mySet.add(1) 
mySet.add(2) 
mySet.add(3) 
print(len(mySet ))
print(mySet)


