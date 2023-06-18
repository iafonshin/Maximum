def is_palindrome(string):
    return string == string[::-1]
input_string = input("Введите строку: ")
result = is_palindrome(input_string)
print(result)