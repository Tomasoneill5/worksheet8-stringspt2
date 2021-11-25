string= 'John-is-a-computer-programmer'
#print(string.replace('-',' '))

length= len(string)
count=0
pos=0
while count<=length-1:
    ch=string[count]
    #print(ch)
    if ch== '-':
        print(string[pos:count])
        pos=count+1
    count=count+1
    if count==length:
        print(string[pos:count])