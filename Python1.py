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

#関数の定義
##def関数名(引数)

def say_hello(greeting):
    print(greeting)

say_hello("hello world")

hello = say_hello
hello("Good Morning")


def add(num01,num02):
    print(num01+num02)

add(6,2)


def add2(num01,num02):
    return(num01+num02)

print(add2(5,2))


def add3(num01,num02):
    return(num01+num02)

add_result=add3(2,7)
print(add_result)

####################クラス####################

#クラス内での「変数」＝「アトリビュート」
#クラス内での「関数」＝「メソッド」

class Student:
    #メソッドは関数と違って必ず1つ引数が必要
    #メソッドに渡したい引数が無い場合、selfを記述する
    #メソッドに渡したい引数が1つの場合、selfを含めた合計2つの引数が必要 def avg(self,引数1)
    
    def avg(self,math,english):
        print((math + english) / 2)

#クラスはクラスから作られたインスタンスを変数に代入してから使う(インスタンス化,オブジェクト化,オブジェクト生成)
#クラスはインスタンスになって初めて使える

a001 = Student()
a001.avg(30,70)
a001.name = "sato" #アトリビュートの定義
print(a001.name)

#print(a001.gender) #未定義のアトリビュートなのでエラー


class Student:

#コンストラクタの定義
#コンストラクタ～インスタンス化するときに、自動的に実行されるメソッド    
    def __init__(self):
        self.name = ""
    
    def avg(self,math,english):
        print((math + english) / 2)

a001 = Student()
a001.name = "ito"
print(a001.name)

a002 = Student()
print(a002.name) 