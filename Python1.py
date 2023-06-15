##############変数#############

print("Good morning")
print("Good evening")
print("Good afternoon")

num = 1
num01 = 2
num_01 = 3
NUM = 4
print(num)
print(num01)
print(num_01)
print(NUM)

#############データ型##############

num02 = 1.23
string_a = "Hello,World"
a = 10
b = 1
bool01 = (a > b)

print(type(num02)) #type()はデータ型を表示
print(string_a)
print(type(string_a))
print(bool01)
print(type(bool01)) #ブール型はTrue or Falseのどちらかを持つ

#############リスト######################

lista = ["idei","onituka","kang"]

print(lista)
print(lista[2])

lista[2] = "kataoka"

print(lista[2])

listb = [["kim","chong"],["ri","pak"]]

print(listb[0][0])

#############演算子################

x = 10
y = 2

print(x > y)
print(x < y)

print(x >= 4 and x <= 6)
print(y >= 3 or y <= 4)

x += 10

print(x)

#############条件分岐################

age = 0

if age >= 20:
    print("adult")
elif age == 0:
    print("baby")
else:
    print("child")

#############繰り返し################

for i in range(5): #range(x)は要素x個のリストと考える、リストの中身はインデックス
    print(i)

for i in range(5):
    if i == 2:
        continue
    elif i == 4:
        break
    print(i)

for i in range(3):
    for j in range(3):
        print(i,j, sep="-")

arr = [2,4,6,8,10]
for i in arr: #inの後にリストを書くことによって、リストの中身がカウンタ変数に一つずつ格納
    print(i)

#############関数################