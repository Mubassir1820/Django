# -*- coding: utf-8 -*-
"""Various_methods.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FVD3YINchkyvzXfnhcmc0yN-rZdNB1ai

**String**

Find()
"""

demo = "This is a string"

pos = demo.find('is')
print(pos)

"""# Split"""

demo = "This is a string"
demo1 = "This-is-a-string"

pos = demo.split()
print(pos)

demo1.split("-")

"""# Join()
only works when every list members is string
"""

ls = ['This', 'is', 'a', 'string']

new_str = " ".join(ls)

print(new_str)

",".join(ls)

user_bad_input = "This               is an     bad input"
user_good_input = " ".join(user_bad_input.split())

user_good_input

"""#startswith()"""

country = "Bangladesh"

country.startswith("Bangla")

"""#Endswith()"""

user_email = "abc@gmail.com"

user_email.endswith("gmail.com")

"""#isdigit() isalpha() isspace()"""

s1 = "1234"
s2 = "123A"
s3 = "ABCD"
s4 = "AVCD$"
s5 = " A1b2c3"
s6 = '  '

s1.isdigit()

s2.isdigit()

s3.isalpha()

s4.isalpha()

s5.isalpha()

s6.isspace()

"""#List

##slicing
"""

ls = [1,2,3,5,6,7,80]

ls[2:5]

"""##len()"""

len(ls)

ls.append("100")
ls

ls.append(100)

ls

"""#Extend()"""

ls1 = [10,20,30]
ls2 = [50,60,70]

ls1.extend(ls2)
ls1

"""#insert()
for inserting in a specific index
"""

ls1.insert(0, 9999)
ls1

ls1.insert(5, 8888)
ls1

"""#remove()"""

ls1.remove(9999)

ls1

"""#pop()"""

ls1.pop()

ls1.pop(0)

ls1

"""#clear()"""

ls1.clear()

ls1

"""#enumerate()"""

ls = ['A', 'B', 'C']
for index, value in enumerate(ls):
  print(f"index: {index} | value: {value}")

ls = ['A', 'B', 'C', 'A']
ls.index('A')

"""#count()"""

ls = ['mango', 'banana', 'apple','mango','mango']
ls.count('mango')

"""#sort()"""

ls.sort()

ls

"""#reverse()"""

ls.reverse()
ls
