# -*- coding: utf-8 -*-
"""22L-6804-lab1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dB-4N3bM_h2H5_eF7UwhzT2p_wqDYxDH
"""

#1
user_input=input("enter your name and age\n")
print("The name and age of user is", user_input)

#2
hehe=input("enter input\n")
if '.' in hehe:

  print(f"Input '{hehe}' is a float.")
else:

  print(f"Input '{hehe}' is an integer.")
#3
listt=[1,2,3,4,5,6]
print(f"List before any modifications is: ",listt)

listt.append(40)
print(f"List after appenidng 40 is: ",listt)
listt.remove(4)
print(f"List after removing 4 is: ",listt)
print(listt)

#4
hehee=(1,2,3,44,5)

first,second,*remianing=hehee
print(first)
print(second)

#5
students=dict(aneeb='a',ramisha='a',ahmad='b',aadil='a',hussain='a')
print(students)

#6
l=input("input list 1")
l2=input("input list 2")
l=l.split(' ')
l2=l2.split(' ')
for i, num in enumerate(l):
  l[i]=int(num)
for i, num in enumerate(l2):
  l2[i]=int(num)



set1 = set(l)
set2 = set(l2)



print(f"List 1: {l}")
print(f"List 2: {l2}")
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference (set1 - set2): {set1.difference(set2)}")
print(f"Difference (set2 - set1): {set2.difference(set1)}")

#7
num=input("enter a num")
if int(num)>0:
 print("its a positive number")
elif int(num)<0:
 print("its a negative number")
else:
 print ("its a zero")

if int(num)%2==0:
  print("its an even number")
else:
   print("its an even number")

#8
for i in range(1,50):
  if(int(i)%5==0 and int(i)%3==0):
    print("fizzbuzz")
  elif (int(i)%5==0):
    print("bbuzz")
  elif (int(i)%3==0):
    print("fizz")
  else:
    print(i)



#9
def fac(n):
    facc=1
    for i in range(1,n+1):
      facc*=i
    return facc
n=input("enter a number")
factorial=fac(int(n))
print(f"the factorial is: ",factorial)

#10
import math
num=input("enter a number")
num=int(num)
primee=1
for i in range(2,int(math.sqrt(num))):
  if(num%i==0):
    primee=0
if primee==1:
  print("the number is prime")
else:
  print("the number is not prime")

#11
l=input("enter a list ")
l=l.split(' ')
for i, num in enumerate(l):
  l[i]=int(num)
squares= [num**2 for num in l]
print(squares)



#12
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d1.update(d2)
#overwrites the duplicate keys with value of second dictionaries key
print(d1)

#13
a = [1, 2,4,6,56,34,56,87,56,3,5]
res = []
for val in a:
  if val not in res:
      res.append(val)

print(res)

#14
palindrome = lambda s: s == s[::-1]
print(palindrome('hehe'))

#15
num=input("enter a num")
num=int(num)
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= num:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2

#17
for  i in range(1,11):
  for j in range(1,11):
    print (f"{i} x {j}= {i*j}")
  print("\n")

#16
l=input("enter a list ")
l=l.split(' ')
sum=0
c=0
for i, num in enumerate(l):
  l[i]=int(num)
  sum+=l[i]
  c+=1
avg=sum/c
print(f"average is : ",avg)

login=[
    {'name': 'ramisha', 'password':'ummheh'},
    {'name': 'suneela', 'password':'blabla'}
]
flag=False
name=input("enter your name\n")
passwordd=input("enter your password\n")
for user in login:
  if user['name']==name and user['password']==passwordd:
    flag=True
if flag:
  print("you have logged in succesfully")
else:
  print("ooopssssssssssssss")

#17
def fToc(temp):
 newtemp=(temp - 32) * 5/9
 return newtemp
def cTof(temp):
  temp=(temp * 9/5) + 32
  return temp
temp=input("enter temperature:\n ")
choice=input("do you want to convert into farenheit or celcius? type  c and f\n")
if 'c' in choice:
  new=fToc(int(temp))
elif 'f' in choice:
  new=cTof(int(temp))
else:
  print("you have entered wrong choice")
print(f"new temp after conversion is: ", new)

#18
def frequency(listt):
  word_count = {}
  for word in listt:
     word_count[word] = word_count.get(word, 0) + 1
  return word_count


Inputt = input("Enter a list of words separated by spaces: ")
words_list = Inputt.split(' ')
freq=frequency(words_list)
for word, count in freq.items():
        print(f"{word}: {count}")

