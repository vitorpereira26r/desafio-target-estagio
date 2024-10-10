
def there_is_a(word):
    count = word.lower().count('a')

    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string"


word = input("Enter a string: ")
print(there_is_a(word))