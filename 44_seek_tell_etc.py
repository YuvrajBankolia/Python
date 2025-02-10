# with open ('43_file.txt' ,'r') as f:
#     print(type(f))
#     f.seek(10)  # seek() ka mtlb h ki direct us number ke word prr aa jayega phir waha se 5 aage read krega
#     print(f.tell())  # tell() ye bata dega ki start kaha se ho rha h
#     data = f.read(5)
#     print(data)
    

with open ('43_file.txt' ,'w') as f:
    f.write('Hello World')
    f.truncate(5)    # iske se starting ke 5 print kr dega 
with open ('43_file.txt' ,'r') as f:
    
    print(f.read())
    