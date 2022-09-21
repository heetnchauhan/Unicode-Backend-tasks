def inputRange():
    a = int(input("Enter an integer number: "))
    b = int(input("Enter another integer number: "))
    
    t = {}
    
    for x in range(a,b):
        k=x
        s = ""
        while x!=0:
            d = x%2
            s = s + str(d)
            x = x//2
        s = s[::-1]

        for i in range(len(s)-1):
            if s[i]=="1" and s[i+1]=="1":
                t[k]="true"
                break
            else:
                t[k]="false"
            
      
    print(t)        

inputRange()


