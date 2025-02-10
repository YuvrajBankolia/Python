dic= {
    "Harry ": "human" , 
    "spoon" : "obj"
}
print(dic.get("Harry"))     # agr dictionary m nhi hua toh none show krega 
print(dic["Harry "])          # aur ye error show krega

print(dic.keys())
print(dic.values())