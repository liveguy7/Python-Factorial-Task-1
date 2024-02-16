

number = int(input("Enter a non-negative number to take the Factorial of: "))
product = 1

for i in range(0, number, 1):
  product = product * (i+1)
  print("{0}: {1}".format(i, product))


print(product)


