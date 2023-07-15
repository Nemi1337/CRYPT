import random
import string
digits = string.digits
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
punctuation = string.punctuation
ambiguous_chars = 'il1Lo0O'

def generate_password(length, chars):

    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

def main():
    num_passwords = int(input("Введіть кількість паролів для створення: "))
    password_length = int(input("Введіть бажану довжину кожного пароля: "))
    include_digits = input("Додати цифри (0123456789)? (y/n): ").lower() == 'y'
    include_uppercase = input("Додати великі літери (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (y/n): ").lower() == 'y'
    include_lowercase = input("Додати малі літери (abcdefghijklmnopqrstuvwxyz)? (y/n): ").lower() == 'y'
    include_punctuation = input("Додати розділові знаки (!#$%&*+-=?@^_.)? (y/n): ").lower() == 'y'
    exclude_ambiguous = input("Виключіть неоднозначні символи (il1Lo0O)? (y/n): ").lower() == 'y'
    chars = ''
    if include_digits:
        chars += digits
    if include_uppercase:
        chars += uppercase_letters
    if include_lowercase:
        chars += lowercase_letters
    if include_punctuation:
        chars += punctuation
    if exclude_ambiguous:
        for c in ambiguous_chars:
            chars = chars.replace(c, '')

    for i in range(num_passwords):
        password = generate_password(password_length, chars)
        print(f"Пароль: {i+1}: {password}")

if __name__ == '__main__':
    main()
    
a=input()