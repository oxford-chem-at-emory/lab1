#02_2_string
#print ("hello world")
#print ('hello world')
#print ("""hello world""")
#print ('''hello world''')
# say = '"Python is very easy." he says.'
# print (say)
# say = "\"Python's favorite food is perl\" he said."
# print (say)
# multiline = "Life is too short\nYou need Python."
# print (multiline)

# multiline = """
# Life is too short
# You need Python
# """
# print (multiline)

# head = "Python"
# tail = " is fun!"
# print (head + tail)

# a = "Python"
# expo = (a * 2)
# print (expo)

# print("=" * 50)
# print("My Program")
# print("=" * 50)

#len() calculates the length of the string including spaces.
# a = "Life is too short."
# print(len(a))

#indexing
# a = "Life is too short, you need Python"
# print(a[0])
# print(a[12])
# print(a[-1])
# print(a[-0])
# print(a[-2])
# print(a[-5])
# b = a[0] + a[1] + a[2] + a[3]
# print(b)
# print(a[0:4])
# #0:4 --> 0<= a < 4
# print(a[0:5])
# print(a[19:])
# print(a[:17])
# print(a[19:-7])

# a = "20240305Cloudy"
# year = a[:4]
# date = a[4:8]
# weather = a[8:]
# print (year)
# print (date)
# print (weather)

# a = "Pithon"
# print (a[1])
# print (a[:1]+ 'y' + a[2:])

# *** FORMATING ***
# print("I eat %s apples." % "five")
# print ("I eat %d apples." % 3)

# number = 3
# print ("I eat %d apples." % number)

# number = 10
# day = "three"
# print("I eat %d apples. so I was sick for %s days" % (number, day))

# print("I have %d apples" % 3)

# print("rate is %s" % 3.234)

# print("Error is %d%%." %98)

# print ("%10s" % "hi")

# print ("%-10sjane" % "hi")

# print("%.3f" % 3.42134234)

# print("%10.4f" % 3.42134234)

# print("I eat {0} apples" .format(3))

# print("I eat {0} apples" .format("five"))

# number = 3
# day = "three"
# print ("I eat {0} apples. so I was sick for {1} days." .format(number, day))

# print("I ate {number} apples. so I was sick for {days} days" .format(number=10, days=3))

# print("I ate {0} apples. so I was sick for {days} days." .format(10, days=3))

# print("{0:<10}" .format("hi"))

# print("{0:>10}" .format("hi"))

# print("{0:^10}" .format("hi"))

# print("{0:=^10}" .format("hi"))

# print("{0:!<10}" .format("hi"))

# print("{0:!>10}" .format("hi"))

# print("{0:!^10}" .format("hi"))

# y = 3.42134234
# print("{0:0.4f}" .format(y))
# print("{0:10.4f}" .format(y))

# print("{{ and }}" .format())

#f string formating
# name = 'John Doe'
# age = 30
# print(f'My name is {name}, age is {age}.')

# age = 30
# print(f'나는 내년이면 {age + 1}살이 된다.')

# d = {'name':'홍길동', 'age':30}
# print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

# print(f'{"hi":<10}')
# print(f'{"hi":>10}')
# print(f'{"hi":^10}')
# print(f'{"hi":<10}')

# #what is the difference betweeen () and {}?
# age = 30
# formatted_string = f'My age is {age:02d}'  # Zero-padded to width 2
# print(formatted_string)  # Output: My age is 30

# name = '홍길동'
# age = 30
# name_age = f'나의 이름은 {name:<5}입니다. 나이는 {(age +1):<5.2f}입니다.'
# print(name_age)

# y = 3.42134234
# number = f'{y:^10.3f}'
# print (number)

# word = f'{"python":!^12}'
# print(word)

# a = 'hobby'
# count = a.count('b')
# print(count)

# a = 'Python is the best choice'
# find = a.find('c')
# print(find)

# findb = a.find('k')
# print(findb)

# z = "password"
# find = z.find('r')
# print(find)
        
# a = 'Life is too short'
# index = a.index('k')
# print(index)

# result = ", ".join('abcd')
# print(result)

# a = "hi"
# upper = a.upper()
# print(upper)

# a = "HI"
# lower = a.lower()
# print(lower)

# a = "   hi   "
# lstrip = a.strip()
# print(lstrip)

# a = "Life is too short"
# replace = a.replace("Life", "Your Leg")
# print(replace)

# a = "Life is too short"
# split = a.split()
# print(split)

# b = "a:b:c:d"
# bsplit = b.split(':')
# print(bsplit)

a = 'hi'
aupper = a.upper()
print (aupper)
print(a)
a = a.upper()
print(a)