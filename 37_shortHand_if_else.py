#     SYNTAX ==   { result = value_if_true if condition else value_if_false }

a =900
b =300
print("A") if a>b else print ("=") if a==b else print("B")
c = 9 if a>b else 0
print(c) 