try:
 y = int(input("enter a number"))
 assert y > 0, "Invalid Operation"
 print(y)
except AssertionError as msg: 
    print(msg)
