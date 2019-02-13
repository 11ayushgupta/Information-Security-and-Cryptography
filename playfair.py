import random

def key_generator():
    s="a b c d e f g h i k l m n o p q r s t u v w x y z".split()
    random.shuffle(s)
    key=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    k=0
    for i in range(5):
        for j in range(5):
            key[i][j]=s[k]
            k+=1
    return (key)

def keytodict(key):
    dict_key={}
    for i in range(5):
        for j in range(5):
            dict_key[key[i][j]]=[i,j]
    return (dict_key)

def plaintext_con(P):
    new=""
    for i in range(len(P)-1):
        if P[i]=="j":
            new+="i"
        else:
            new+=P[i]
        if P[i]==P[i+1]:
            new+='x'
    new+=P[-1]
    if len(new)%2!=0:
        new+='z'
    return (new)

def encrypting(P,k,K):
    print(P,len(P))
    for i in range(5):
            print (k[i])
    print(K)
    
    new=""
    
    for i in range(0,len(P),2):
        if K[P[i]][0]==K[P[i+1]][0]:
            new+=k[K[P[i]][0]][(K[P[i]][1]+1)%5]
            new+=k[K[P[i+1]][0]][(K[P[i+1]][1]+1)%5]
        elif K[P[i]][1]==K[P[i+1]][1]:
            new+=k[(K[P[i]][0]+1)%5][K[P[i]][1]]
            new+=k[(K[P[i+1]][0]+1)%5][K[P[i+1]][1]]
        else:
            new+=k[K[P[i]][0]][K[P[i+1]][1]]
            new+=k[K[P[i+1]][0]][K[P[i]][1]]

    return (new)

def test():

    text="hello"#input("enter plain text\n")
    key=key_generator()
    key_dict=keytodict(key)
    encr=encrypting(plaintext_con(text).lower(),key,key_dict)
    #decr=decrypting(plaintext_con(text).lower(),key,key_dict)
    print(encr)
    #print(decr)



test()

