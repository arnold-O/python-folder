###What are functions
# def fun_name(par1, par2, par3):
#     result =  par1 + par2 + par3
#     return result
#
#
# prv = fun_name(3, 4, 6)

#The copy of the values are not created when pass to the function, same values are referenced

# x,y,z = 2, 3, 5

#If x,y,z are passed into the function with par1, par2 and par3 as parameters , the values, in terms of id will not change
# prv2 = fun_name(x,y,z)

# print(prv2)


# def check_params(first, second, third):
#     return first + second - third
# pass_position = check_params(50, second=60, third=20)
# print(pass_position)

#defaults are created once
# def add_def(item, l2=[]):
#     l2.append(item)
#     return l2
#
# print(add_def(2))
# print(add_def(3, [1,4,5,6,7]))
# print(add_def(4))



def new_fun(para1, para2, para3):
    return para1+para2+para3



values1 = new_fun(1,2,3)
print(values1)

