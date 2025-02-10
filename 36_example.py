st = input("enter the message : ")
words = st.split(" ")
coding =input("1 for Coding or 0 for Decoding")
coding = True if(coding=='1') else False
print(coding)
if(coding):
    nwords =[]
    for word in words:    
        if(len(word)>=3):
            r1 ="hlo"
            r2 ="bye"
            stNew =r1+ word[1:] +word[0]+r2
            nwords.append(stNew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))

else:
    nwords =[]
    for word in words:
        if(len(word)>=3):
            stNew = word[3:-3]
            stNew = stNew[-1]+ stNew[:-1] 
            nwords.append(stNew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))