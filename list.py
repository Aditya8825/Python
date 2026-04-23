# sum of max element in list<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# lst = [[1, 2, 3], [3, 4, 5], [5, 7, 3, 2]]

# result = [sum(x) for x in lst]

# print(result)




#sum of min element<<<<<<<<<<<<<<<<<<<<<<<<<<

# lst = [[1, 2, 3], [3, 4, 5], [5, 7, 3, 2]]

# result = []

# for sublist in lst:
#     min_val = sublist[0]   # assume first element is minimum
#     for num in sublist:
#         if num < min_val:
#             min_val = num
#     result.append(min_val)

# print(result)





# create a program to compute the difference between two list
# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# diff1 = [c for c in colors1 if c not in colors2]
# print(diff1)
# diff2 = [c for c in colors2 if c not in colors1]
# print(diff2)
# print(list(set(colors1) - set(colors2)))
# print(list(set(colors2) - set(colors1)))





## diffferent colors sction in both list<<<<<<<<<<<<<<<<<<<<<<<<<
# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# lst1=[]
# lst2=[]
# for i in colors1:
#     if i not in colors2:
#         lst1.append(i)
    
# for i in colors2:
#     if i not in colors1:
#         lst2.append(i)

# print(lst1)
# print(lst2)





#make alist of of dublicate or similr element
# lst = [0,0,1,2,3,4,4,5,6,6,7,8,9,4,4]
# lst1=[]
# t=[lst[0]]
# for i in lst[1:]:
#     if i == t[-1]:
#         t.append(i)
#     else:
#         lst1.append(t)
#         temp=[i]
#  lst1.append(t)
# lst1.append(t)
# print(lst1)





# lst = [0,0,1,2,3,4,4,5,6,6,7,8,9,4,4]

# lst1 = []
# t = [lst[0]]

# for i in lst[1:]:
#     if i == t[-1]:
#         t.append(i)
#     else:
#         lst1.append(t)
#         t = [i]   # reset correctly

# lst1.append(t)   # add last group

# print(lst1)





#create  a program to seprate a similar element or dublicate element<<<<<<<<<<
# lst = [0,0,1,2,3,4,4,5,6,6,7,8,9,4,4]

# lst1 = []
# lst2= []
# for i in lst:
#     if not lst2 or i == lst2[-1]:
#         lst2.append(i)
#     else:
#         lst1.append(lst2)
#         lst2 = [i]

# lst1.append(lst2)

# print(lst1)



# similar question<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# lst = [0,0,1,2,3,4,4,5,6,6,7,8,9,4,4]
# ans=[]
# temp=[lst[0]]
# for i in range(1,len(lst)):
#     if lst[i-1]==lst[i]:
#         temp.append(lst[i])
#     else:
#         ans.append(temp)
#         temp=[lst[i]]

# print(ans)





# lst1 = []
# lst2= []
# for i in lst:
#     if not lst2 or i == lst2[-1]:
#         lst2.append(i)
#     else:
#         lst1.append(lst2)
#         lst2 = [i]

# lst1.append(lst2)

# print(lst1)




### vivevers of above question<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lst = [0,0,1,2,3,4,4,5,6,6,7,8,9,4,4]
ans=[lst[0]]

for i in range(1,len(lst)):
 #   if i not in lst:
    if lst[i] !=lst[i-1]:
        ans.append(lst[i])
print(ans)