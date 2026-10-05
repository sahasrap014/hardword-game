import random
n=["must","fail","leaf","king","soap","more","four","comb","head","lime"]
s=random.choice(n)
l=list(s)


while(True):
    c=0
    c1=0
    print("_ _ _ _")
    print("enter a word without duplicates")
    s1=input()
    print(s1)
    l1=list(s1)
    if len(s1)!=4 and len(s1)!=0:
        print("enter four letter word only!!")
    else:
        for i in range(len(l)):#green
            if l[i]==l1[i]:
                c+=1
        print(c," letters is in correct position")
                
        for i in l:#yellow
            if i in l1:
                c1+=1
        print(c1-c," letters are present but not in correct position")
    
    if s==s1:
        print("YOU WON!")
        break