name = "Çınar"
surname = "Yılmaz"
age = 41

print ("My name is {} {}".format(name, surname))
#My name is Çınar Yılmaz
print ("My name is {0} {1}".format(name, surname))
#My name is Çınar Yılmaz
print ("My name is {1}, {0}".format(name, surname))
#My name is Yılmaz, Çınar
print ("My name is {s} {n}".format(n=name, s=surname))
#My name is Yılmaz Çınar
print ("My name is {} {} and I'm {} years old".format(name, surname, age))
#My name is Çınar Yılmaz and I'm 41 years old
print (f"My name is {name} {surname} and I'm {age} years old")
#My name is Çınar Yılmaz and I'm 41 years old

result = 200 / 700
print ("The result is: {}".format(result))
#The result is: 0.2857142857142857
print ("The result is: {r:1.3}".format(r=result))
#The result is: 0.286

