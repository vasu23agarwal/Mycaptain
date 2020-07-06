n= int(input("How many terms? "))

n1 = 0
n2 = 1
count = 0

if n<=0:
   print("enter positive no.")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
