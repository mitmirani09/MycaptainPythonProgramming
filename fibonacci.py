n = int(input("Enter the value of n: "))
F1=0
F2=1

sum = 0
count = 1
print("Fibonacci series for n numbers is:")
while(count <= n):
  print(sum)
  count += 1
  F1 = F2
  F2 = sum
  sum = F1 + F2