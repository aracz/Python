"""num_list = [30,4,44]

def double_list(lst):
    double = [num * 2 for num in lst]
    print(double) 

double_list(num_list)

word_list = ["red","black","blue","velvet","betty","stag","jack"]

def words(lst):
    word2_list = [word + word_list[3] for word in lst]
    print(word2_list)

words(word_list)

def compound():
    lst = []
    lst2 = [[num + 1] for num in range(0,30)]
    print(lst2)

compound()

d = {"1":"New Hope", "2":"Return of the Jedi"}

#"3":"The Empire Strikes Back"

def f(x,y):
    print(x,y)

lst = [2,4,7,12,17,18,20,21,36,47,52,66]
lst2 = []
lst3 = []
lst5 = []

def divisor(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst2.append(lst[i])
        if lst[i] % 3 == 0:
            lst3.append(lst[i])
        if lst[i] % 5 == 0:
            lst5.append(lst[i])
    print(lst2)
    print(lst3)
    print(lst5)

divisor(lst)"""

#dct = {"Barna": "Accounting","Bence":"Selling","Dani":"HR"}

#print(dct.items())
#dct.items()

L=[1,2,3,4,5,6,"Monday"]

for index, item in enumerate(L):
        print(index, item)





    