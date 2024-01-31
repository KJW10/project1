##함수
def add_func(n1,n2):
    return n1+n2
def sub_func(n1,n2):
    return n1-n2
def square(n1,n2):
    return n1**2, n2**2
##변수
num1, num2, res, red = 100, 200, 0, 0
##메인
res = add_func(num1, num2)
print(num1,'+',num2,'=',res)

res = sub_func(num1, num2)
print(num1,"-",num2,"=",res)

res , red= square(num1, num2)
print(num1,"**2","=",res,num2,"**2","=",red)
