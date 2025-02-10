# marks = [12,56,87,34,1,4,95]

# index =0
# for mark in marks:
#     print(mark)
#     if(index ==3):
#         print("done")
#     index +=1             # YAHA PRR INDEX+=1 KRNA PD RHA H ISS SE BDIYA ENUMERATE FUNCTION KO USE KR LO
marks = [12,56,87,34,1,4,95]

index =0             #   ENUMERATE FUNCTION IS HELP US TO GET THE INDEX VALUE OF EACH ELEMENT IN THE SEQUENCE ST THE ASME TIME.
for index ,  mark in enumerate(marks):
    print( index ,mark)
    if(index ==3):
        print("done")