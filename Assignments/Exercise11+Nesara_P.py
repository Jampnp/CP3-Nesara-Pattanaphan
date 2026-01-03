high = int(input("Input the height of the pyramid :"))

for x in range(high):
    print(" " * (high-(x-1)) + "*"*(2*x+1))
    
