# sorting.py
# Програма 1. Правильне сортування

# Вихідний список
words = [
    "English",
    "інформація",
    "android",
    "Windows",
    "Добрий день",
    "матриця",
    "актова зала",
    "біоресурси",
    "єдиний",
    "кава",
    "Їжак",
    "Історія"
]

print("Заданий список:")
print(words)

# Функція визначення порядку сортування
def custom_sort(word):
    # Розрізняємо українські та англійські літери
    ukr_letters = "абвгґдежзийіїєклмнопрстуфхцчшщьюя"
    ukr_first = word[0].lower()

    # Якщо слово починається з української літери
    if ukr_first in ukr_letters:
        return (0, word.lower())
    # Якщо з латинської
    else:
        return (1, word.lower())

# Сортування списку
sorted_words = sorted(words, key=custom_sort)

print("\nВідсортований список:")
print(sorted_words)