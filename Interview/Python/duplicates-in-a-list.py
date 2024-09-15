#How do you find duplicates in a list using Python? 

a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
res = []
for x in a:
    if a.count(x) > 1 and x not in res:
        print(str(x) + " is appeared "+str(a.count(x)) + " times")  
        res.append(x)  
print(res)

##################################################
#Remove the duplicates 
a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
print('provided list' +str(test_list))
set_temp=list(set(test_list))
print(set_temp)

res=[]
[res.append(i) for i in a if i not in res]
print(res)
