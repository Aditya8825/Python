# x=5,
# print(type(x))



# tpl=(1,2,3,4,5,"hello")
# print(type(tpl))



# tpl=(4,5,6,7,[56,7,89])
# # print(tpl[2:])
# # print(tpl[-1])
# tpl[-1][1]=40
# print(tpl)


# tpl=(1,3,4,5,6)
# del tpl
# print(tpl)
# tpl+=("hello",5,7,8)
# print(tpl)


#  DIVIDE THE LIST  INTO TWO EQUAL HALVES AND PRINT THE SUM OF EACH HALF
# lst=[2,4,6,8,3,5,8,9]   
# #  output:20,25
# print(sum(lst[:len(lst)//2]),sum(lst[len(lst)//2:]))

tpl=(4,5,6,7,45,67)
# #tpl[3]=70
# # tpl[-1][1]=40
# print(id(tpl))
# tpl+=("hello",5,7,8)
# print(id(tpl))
# print(tpl)



#reversed tupled
# print(sorted(tpl,reverse=True))




tpl=list(tpl)
tpl[4]=49
tpl=tuple(tpl)
print(tpl)