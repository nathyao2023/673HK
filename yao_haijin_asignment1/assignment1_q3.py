#question 3
#3)Write a program that prints a multiplication table for numbers up to 12
#

def multiplication_table():
    for x in range(1,13):
        for y in range(1,13):
            if x>=y:
                print(x,'*',y,'=',x*y,end='\t')
        print()
multiplication_table()







