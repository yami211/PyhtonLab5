
# Програма 1. Правильне сортування


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

    ukr_letters = "абвгґдежзийіїєклмнопрстуфхцчшщьюя"
    ukr_first = word[0].lower()

    
    if ukr_first in ukr_letters:
        return (0, word.lower())

    else:
        return (1, word.lower())

# Сортування списку
sorted_words = sorted(words, key=custom_sort)

print("\nВідсортований список:")
print(sorted_words)