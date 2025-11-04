def is_strictly_increasing_digits(n):
    if n < 0 or type(n) !=int:
        return -1
    s = str(n)
    for i in range(len(s) -1):
        if int(s[i]) >= int(s[i +1]):
            return False 
    return True 
    
        


    
   
       

    
