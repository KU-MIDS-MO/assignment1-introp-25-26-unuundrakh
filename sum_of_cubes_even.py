def sum_of_cubes_even(n):
    if n < 0 or type(n) !=int:
       return -1
    if n > 2000 :
        print("warning but still compute")
     
    total = 0
    for x in range (0, n + 1):
        if x % 2 ==0:
            total += x ** 3
    return float(total)

