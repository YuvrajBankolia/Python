def func1():
    try:
        l = [1,3,5,6,9]
        i =  int(input("enter the index"))
        print(l[i])
        return 1
    except:
        print("some error occured ")
        return 0

    finally:
        print("i am always executed")   #finally mtlb ye toh executed hoga hi hoga kuch bhi ho jaye....
x =func1()
print(x)