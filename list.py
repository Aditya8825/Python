# list2=[7,-4,-2,9,0,11,17,8,19,10]
# print(list[:-5:10])
# print(list[:-5:-10])



#update element<<<<<<<<<<<<<<<
# list.append("hello")
# list.insert(-4,36)
# print(list)



## extend function<<<<<<<<<
# list2 = [7, -4, -2, 9, 0, 11, 17, 8, 19, 10]
# list1 = [45, 46, 47]

# # Correct usage
# list1.extend(list2)
# # print(list1)

# combined_list = list1 + list2
# print(combined_list)


#add  element <<<<<<<<<<<<<<<
# write a program to print thr sum and print the sum of the other element in the list<<<<<<<<<<<<<<<<<<<<<<<
# lst=[1,2,3,4,5]
# sum = 0
# for i in lst:
#     sum += i
#     ans=[]
#     for i in lst:
#         ans.append(sum-i)
#         print(ans)
#         print(lst)


#add list element <<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
# lst=[{1,3,5,6} ,{3,4,5},{3,5,7},{10,20,30}]

# ans=[]
# for i in range(len(lst)):
#         temp=0
#         for j in lst[i]:
#                 temp+=j
#         ans.append(temp)
# print(ans)





# nums = [[1, 3, 5, 6], [3, 4, 5], [3, 5, 7], [10, 20, 30]]

# for sublist in nums:
#     for i in range(len(sublist)):
#         if sublist[i] % 2 == 0:
#             sublist[i] = sublist[i] + 1
#         else:
#             sublist[i] = sublist[i] - 1

#     print(sublist)



### extend list of 0 element


# lst = [3,4,5,6,0,0,0,1,2,0]

# result = []


# for i in range(len(lst)):
#     if lst[i] != 0:
#         result.append(lst[i])


# for i in range(len(lst)):
#     if lst[i] == 0:
#         result.append(lst[i])



# print(result)
lst=[[3,2,1,8],[50,3,7,9],[2,3,7,8]]
#FOR ODD INDEX LIST ADD +1 AND FOR EVEN SUB -1 
#ans=[3,1,1,2],[50,4,8,10],[1,3,7,7]
ans=[]
for i in range(len(lst)):
    temp=lst[i].copy()   
    if i%2==0:
        for j in range(len(temp)):
            if temp[j]%2==0:
                temp[j]-=1
        ans.append(temp)
    else:
        for j in range(len(temp)):
            if temp[j]%2==0:
                temp[j]+=1
        ans.append(temp)
    print(lst)
    print(ans)