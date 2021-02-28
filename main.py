#list
#rite a program, which asks you enter 5 characters. Characters should be added to list. Output: in the first line - first 3 charakters, in the second line - last 2 characters, in the thid line - the oposite order of list.

a = []

b1 = input("Iveskite pirma simboli")
a.append(b1)
b2 = input("Iveskite antra simboli")
a.append(b2)
b3 = input("Iveskite trecia simboli")
a.append(b3)
b4 = input("Iveskite ketvirta simboli")
a.append(b4)
b5 = input("Iveskite penkta simboli")
a.append(b5)

print (a[0:3])
print (a[3:5])

list.reverse(a)

print (a)
