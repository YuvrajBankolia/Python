# String are Immutable
a= "!!Yuvraj!! !!!!!!!! YYYYY !!! Yuvraj "
print(len(a))
print(a.upper())        # sbhi ko capital kr dega 
print(a.lower())        # sbhi ko small kr dega

print(a.rstrip("!"))    #  baad wale ! mark ko print nhi honge dega phle wla toh hoga 
print(a.replace("Yuvraj" ,"Steive"))  #yuvraj se steive m  replace kr dega 
print(a.split())        #split kr dega

blogHeading = "hii my Self Yuvraj"
print(blogHeading.capitalize())    # starting word ko capital aur baaki sbko ko small m convert kr dega 

str1 = "welcome to console!!!"
print(len(str1))
print(len(str1.center(50)))   # length 21 thi aur extend krke 50 kr diya 
print(a.count("Yuvraj"))     # count krega yuvraj kitni baar aa rha h

str1 = "welcome to console!!!"
print(str1.endswith("console!!!"))  # ki str1 ka last word console!!! h ya nhi 

str1 = "welcome to console!!!"
print(str1.endswith("to" , 4,10))

str1 = "welcome to console!!!"
print(str1.find("you"))     # ye present nhi h toh -1 return kr dega 
print(str1.find("to"))     # ye present h toh uska index de dega mtlb 10 return kr dega 
#print(str1.index("ahh"))   # index ek exception raise krta h  subs srting not found

str1 = "WelcomeToConsole"   # sb kuch sahi likha hina chiye toh true otherwise false
print(str1.isalnum()) 

str1 = "welcoome"
print(str1.isalpha()) 

str1 = "welcoome35345"
print(str1.isalpha())

str1 = "welcome world"
print(str1.islower()) 
str1 = "welcome worldYYY"
print(str1.islower()) 

str1 = "welcome world\n"   #false isliye kyo ki \n dikhega nhi print krne pr 
print(str1.isprintable()) 

str1 = "     "
print(str1.isspace())

str1 = "Welcome World Health"
print(str1.istitle()) 

str1 = "welcome world"
print(str1.startswith("welcome"))

str1 = "welcome world"
print(str1.swapcase()) 

str1 = "welcome world name is Dan"
print(str1.title()) 