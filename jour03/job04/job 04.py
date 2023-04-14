# function range (0-100 sans num/3, num/5)
for num in range(101):
    if num % 3==0 and num % 5==0:
       print ("FIZZBUZZ")
    elif num % 3==0:
       print("FIZZ")
    elif num % 5==0:
       print("BUZZ")
    elif num % 3==0 and num % 5==0:
       print ("FIZZBUZZ")
    else:
       print (num)
     
