def is_palindrome(word):
    return word == word[::-1]

words = input("enter:").split()

for word in words:
    if is_palindrome(word):
        print(word)
        break
else:
    print("")
