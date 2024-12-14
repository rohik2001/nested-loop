'''i = 1 #initialise
while i<=5: #iterate loop till i is less than or equal to 5 
    j=1
    while j<=10:
          print(j,end="")
          j=j+1 #increament of columns
    i=i+1 #increament in rows
    print()

#taking input of a word
string = input("Please enter your own word: ")
#taing input of a carecter
char = input("please enter your own carecter: ")
i=0
count=0

while(i<len(string)):
     if(string[i]==char):
          count=count+1
     i=i+1
#display
print("The total number of times",char,"has occured = ",count)
lower = int(input("Enter a lower case"))
upper = int(input("Enter a upper case"))
print("prime number between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)'''

def product_of_midpoints (number):
    product = 1
    for x1, x2 in number:
        mid = (x1 + x2) / 2
        product = product*mid

    return product

number = [(2, 4), (6, 10)]
print( product_of_midpoints (number))
    