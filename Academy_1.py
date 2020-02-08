import random

print("Task 1")
arg="Vlad"
def function(arg):
    print("Hello %s!"% arg)
function(arg)
print("Task 2")
def summery(list):
    summer=0
    for i in list:
        summer+=i
    return summer
def mulptiply(list):
    mylty=1
    for i in list:
        mylty*=i
    return mylty
list=[1,2,3,4]
print ("The summer is: ",summery(list),"\nThe Multiply is:",mulptiply(list) )
print("Task 3")
def reverse_fun(string):
    new_string=""
    for i in range(len(string)-1,-1,-1):
        new_string+=string[i]
    return new_string

line="I am testing"
print(''.join(reversed(line)))
print(reverse_fun(line))
print("Task 4")
def isPalindrome(strings):
    first_part=""
    second_part=""
    char_symbol=False
    if len(strings)%2!=1:
        return False
    else:
        for i in range(0,len(strings)//2):
            first_part+=strings[i]
        for i in range(len(strings)-1,len(strings)//2,-1):
            second_part+=strings[i]
        if first_part==second_part:
            return True
        else: return False
print("Polindrom: ",isPalindrome("ridar"))
print("Task 5")
def histogram(list):
    for j in list:
        print("*"*j)
histogram([4,9,7])
print("Task 6")
def caesarCipher(string,key):
    alphabet=['a','b','c','d','e','f','g','k','l','m','n','o','p','r','s','t']
    cipher=""
    for i in string.lower():
        if alphabet.index(i)+1+key>len(alphabet):
            cipher+=alphabet[alphabet.index(i)+key-len(alphabet)]
        else:
            cipher+=alphabet[alphabet.index(i)+key]
    return cipher
print(caesarCipher("prst",1))
print("Task 7")
def diagonalReverse(matrix):
    new_matrix=[[None,None,None],[None,None,None],[None,None,None]]
    print (new_matrix)
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            new_matrix[j][i]=matrix[i][j]
    return new_matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(diagonalReverse(matrix))
print("Task 8")

def game(start,stop):
    char=False
    guess_r=int(random.randrange(start,stop))
    print(guess_r)

    while not char:
        guess=int(input("Guess a number:"))
        print(guess)
        if guess==guess_r:
            print("You are right!")
            char=True
        else:
            print("Try again \n If you want to exit: print \"q\" ")
            if input()=='q':
                break
game(1,10)
print("Task 9")
def closing_brackets():
    string=input("Input string: ")
    open_case="["
    close_case="]"
    open_num=0
    for i in string:
        if i==open_case:
            open_num+=1
        elif i==close_case:
            if open_num>0:
                open_num-=1
            elif open_num==0:
                open_num=1
                break

    if open_num==0:
        return string,"Ok"
    else:
        return string, "Not Ok"
print(closing_brackets())
print("Task 10")
def charFreq():
    string_l=input("Input line: ")
    diction={}
    for i in string_l:
        if i in diction.keys():
            diction[i]+=1
        else:
            diction[i]=1
    return diction
print(charFreq())
print("Task 11")
def decToBin():
    decimal=int(input("Input decimal: "))
    binary=""
    num=0
    while num!=1:
        binary+=str(decimal%2)
        print(binary)
        decimal=decimal//2
        num=decimal
    binary+="1"
    return reverse_fun(binary)
print(decToBin())

print("Task 12")
def ship_battle():
    order=int(input("Enter the order integer: "))
    matrix = []
    for i in range(0,order):
        matrixs = []
        for j in range(0,order):
            x = "*"
            matrixs.append(x)
        matrix.append(matrixs)
    print (matrix)
    x=int(random.randrange(0,order))
    print(x+1)
    y=int(random.randrange(0,order))
    print(y+1)
    matrix[x][y]=0
    print (matrix)
    char=True
    while char:
        guess_x=int(input("Try x coordinate from 1 to %s: "% str(order)))-1
        guess_y=int(input("Try y coordinate from 1 to %s: "% str(order)))-1
        if x==guess_x and y==guess_y:
            print("You win!")
            char=False
        else:
            print("Try more")
            matrix[guess_x][guess_y]=1
            for i in matrix:
                print(" ".join(str(j) for j in i))
ship_battle()




