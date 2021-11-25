string= 'Hello There'
print(string)

strLength=len(string)
count=0

'''while count<strLength:
    ch=string[count]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print(ch)
    count= count+1
'''

#modified for consonants

consonantCount=0
lowercaseString=string.lower()
while count<strLength:
    ch=lowercaseString[count]
    if(ch!='a' and ch!='e' and ch!='i' and ch!='o' and ch!='u' and ch.isalpha()):
        print(ch)
        consonantCount=consonantCount+1
    count= count+1

print(consonantCount)

conStr=('bcdfghjklmnpqrstuvwxyz')
while count<strLength:
    ch=lowercaseString[count]
    if (conStr.find(ch) > -1):
        consonantCount=consonantCount+1
    count=count+1
print(consonantCount=consonantCount+1)
