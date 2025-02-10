letter ="Hey my name is {} and I am from {}"
name = "yuvraj"
country = "India"
print(letter.format(name , country))
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {country}")

price= 76.0
text = f"for only {price:.2f} dollars!"   # f string
print (text)
print(f"{2*4}")     # f string