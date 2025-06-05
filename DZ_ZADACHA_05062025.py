text = input("Введите строку: ")
vowels = "аеиоуыэюяАЕИОУЫЭЮЯ"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha() and char.lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"\nКоличество гласных букв: {vowel_count}")
print(f"Количество согласных букв: {consonant_count}")
words = text.split()
longest_word = ""
for word in words:
    clean_word = word.strip(".,!?;:-()\"\'")
    if len(clean_word) > len(longest_word):
        longest_word = clean_word

print(f"\nСамое длинное слово: {longest_word}")

search_word = input("\nВведите слово для поиска: ").lower()
word_count = 0

for word in words:
    clean_word = word.strip(".,!?;:-()\"\'").lower()
    if clean_word == search_word:
        word_count += 1

print(f"Слово '{search_word}' встречается {word_count} раз(а)")