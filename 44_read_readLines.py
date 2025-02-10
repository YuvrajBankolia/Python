f = open('43_file.txt', 'r')
i = 0
while True:
    i= i + 1
    line = f.read()   # ye ek baar hi read krega phir print krega 
    line = f.readline()   # sbko read krke prinr krwa dega 
    if not line:
        break 
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in maths is : {m1}")
    print(f"Marks of student {i} in EVS is : {m2}")
    print(f"Marks of student {i} in SST is : {m3}")
    print(line)