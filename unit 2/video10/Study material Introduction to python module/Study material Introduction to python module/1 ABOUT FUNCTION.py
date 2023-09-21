#'Function can be categorised as i. built in,ii.modules,iii.user defined')
#"1. built in function a. type convertion function")
#'int(),str(),float()')
a=int('123')
print a
b=str(a)
print b
c=float(a)
print c
#"1. built in function ")
#'input(),eval(),min(),max(),abs(),type(),len,round(),range()')
a=int(input('enter a no'))
print a
a,b=3,4
print (eval('a+b'))
print(min(2,1,5,8,0,6))
print(max(2,1,5,8,0,6))
#'abs function always returns positive values/absolute values')
print (abs(-45))
print (abs(-45.9))
#'type function returns data type' )
print (type(a))
print (len('deep'))
print (round(4.5))
print (round(4.4))
print(range(2,5))
