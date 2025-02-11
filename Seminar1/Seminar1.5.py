l = [1,2,3,4]

for i in range(len(l)):
    #i = 0, 1, 2, 3
    print("i =", i )
    a = l[i] + l[i-1]
    print(a)
