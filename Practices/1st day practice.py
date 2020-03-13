'''
a = "I am nilanjana  "
print(a)

c = "i" in a
print(c)
print(len(a))

b = a.split()
print(b)

d = a[3:9]
print(d)


e = "     iamnilanjana plus kid           "
f = e.strip()
print(f)
g = f.split()
print(g)
h = e.replace('kid', 'naughty')
print(h)
e += 'iam'
print(e)

j = 'iam' +a
print(j)
'''
'''

a = "I am a laptop"
for x in a:
 print (x)


if "a"  not in a:
 t = x + "*"
else:
 t = x + '$'
 print (t)
'''

my_list = [20, 30, 40, 50, 22, 50]
for x in my_list:
    print(x)

my_list.pop()
print(my_list)
my_list.append(100)
print(my_list)
my_list.insert(3, 100)
print(my_list)
