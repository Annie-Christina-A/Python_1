import random
print("lets play Hangman!!")
aplha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s=[]
t=[]
v=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
h=random.choice(v)
print(f"you have only {h} lives")
for i in range(int(h)):
    t+=random.choice(aplha)
    s+="_"
print(s)
for i in range(int(h)):
    go=input("Guess the letter: ")
    if go in t:
        for i in range(len(t)):
            if(t[i]==go):
                s[i]=go
        print(s)
    else:
        print("wrong")
    
    
    
    




        