#prints list values in list a that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for lessthanfive in a:
#starts loop for list a
    if lessthanfive < 5:
    #if a value in list a is less than 5
        b.append(lessthanfive)
        #adds list value to list b
    else:
        break
    #if a list value is equal to or greater than 5, breaks the loop
print(b)
#prints the changed list b    
    
    