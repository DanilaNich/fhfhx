numbers = [1,2,3,4,5]
sum = sum(numbers)
print(sum)

spicok = [6,8,7,9,12]
a = max(spicok)
print(a)

spicochek = [2,2,4,9,12,7,4]
delit = list(set(spicochek))
print(delit)

listik1 = [234,242,269,61]
listik2 = [1,4,7,0,9]
listik3 = listik1 + listik2
print(listik3)

korteg = input()
korteg5 = []
for ab in korteg.split(" "):
    korteg5.append(ab)
print(korteg5)
tr = input('введите элемент для поиска')
if tr in korteg5:
   n = korteg5.index(tr)
   print(n)
else:
   print('нет такого элемента')

korteg1 = (2,6,9)
korteg2 = (1,7,8)
korteg3 = korteg1 + korteg2
print(korteg3)

tupl1 = "a", "b", "c", 1, "t", "r", "c", "a"
print(tupl1)
tupl1 = tupl1[:2] + tupl1[3:]
print(tupl1)
list1 = list(tupl1) 
list1.remove("c") 
tupl1 = tuple(list1)
print(tupl1)

def Count(tup, ch):
    return tup.count(ch)
tup = (1,4,8,1,1,9,3,2,6,1,7,16,5)
ch = 6
ch1 = 1
ch2 = 19
print(Count(tup, ch), "times")
print(Count(tup, ch1), "times")
print(Count(tup, ch2), "times")