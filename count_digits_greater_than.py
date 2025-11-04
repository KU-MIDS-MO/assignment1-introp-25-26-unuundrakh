def count_digits_greater_than(n, t):
   if type(t) !=int or not (0 <= t <= 9):
       return -1
   if type(n) !=int or n < 0:
       return -1
   total = 0
   for digit in str(n):
       if int(digit) > t:
           total += 1
   return total 