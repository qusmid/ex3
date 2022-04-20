word = input("Введите слово: ")


def palindrome(word):
    reverse = word[::-1]
    if word == reverse:
        print("Слово является палиндромом.")
    else:
        print("Слово не является палиндромом.")


palindrome(word)
