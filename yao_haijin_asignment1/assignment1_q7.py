#question 7
#Write a function that determines if
#a given year is a leap year. Test it in your program.



def is_leapyear(n):
    if n%4 == 0 and n%100 !=0:
        return(n,'is a leap year')
    elif n%400 == 0:
        return(n,'is a leap year')
    else:
        return(n,'is not a leap year')

print(is_leapyear(2000))
print(is_leapyear(2100))
print(is_leapyear(1900))
print(is_leapyear(2012))
print(is_leapyear(1896))
print(is_leapyear(1999))
