#Greatest common divisor and least comon multiple
'''
36=2X2X3X3
60=2X2X3X5
GCD=2X2X3
   =12
'''
def gcd(x, y):
    gcd = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd

print(gcd(12, 17))
print(gcd(4, 6))


#least common multiple
'''
30 = 2 × 3 × 5
45 = 3 × 3 × 5
2: one occurrence
3: two occurrences
5: one occurrence
2 × 3 × 3 × 5 = 90 <— LCM
'''


def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))
