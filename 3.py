# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# c=a
# print(a is b)
# print(a is c)

# a=8
# b=5
# print(a & b)
# print(a | b)
# print(a ^b)

# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# c=int(input("Enter the number:"))
# if(a>c and a>b):
#     print("A is greater")
# elif(b>a and b>c):
#     print("B is greater")
# else:
#     print("C is greater")

# if(a>b):
#     if(a>c):
#         print(a)
#     else:
#         print(c)
# else:
#     if(b>c):
#         print(b)
#     else:
#         print(c)

# a = input().lower()
# vowels = ['a', 'e', 'i', 'o', 'u']
# if a in vowels:
#     print("Vowel")
# else:
#     print("Consonant")

# b=input()
# print('Consonent'if b ot in 'AEIOUaeiou' else 'Yes')


# marks = input("Enter your marks: ")
    
# if marks.isdigit():
#     marks = int(marks) 
# else:
#     print("Invalid input")


# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# l=["name","age","address","phone","email","branch","cgpa","year","skills","projects"]
# d={}
# for i in l:
#     d[i]=len(l[i])
# print(d)


def Mahesh(arr,target):

    for i in arr:
        if target in arr:
            return True
    else:
        return False
    
    

arr=list(map(int,input().split()))
target=int(input())
  
out=Mahesh(arr,target)
print(out)









