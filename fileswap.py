file1 = input("Enter the first file you want to swap: ")
file2 = input("Enter the second file you want to swap: ")

def fileswap(c , d):
  with open(c, 'r') as a:
    data_a = a.read()
  with open(d, 'r') as b:
    data_b = b.read()
  with open(c, 'w') as a:
    a.write(data_b)
  with open(d, 'w') as b:
    b.write(data_a)


fileswap(file1 , file2)
