string= input('Enter a sequence of characters :')
print(string)

total=0

for ch in string:    
    if ch.isdigit():
        print(int(ch))
        total=total+(int(ch))
    
    
print("Total is: ",total)