#
#question4

#Write a function that tests whether a string is a palindrome and test it in your program

##


def test_palindrome(s):
    return s==s[::-1]

test_s=['hello','world','level','dad']
for s in test_s:
    result = test_palindrome(s)
    print(f'{s}:{result}')



