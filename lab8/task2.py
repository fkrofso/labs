programming_languages = {
    "Python": 1991,
    "C++": 1985,
    "Java": 1995,
    "JavaScript": 1995,
    "PHP": 1995
}

language = input("Введіть назву мови програмування: ")

try:
    year = programming_languages[language]
    print(f"Мова {language} була створена у {year} році.")
except KeyError:
    print(f"Помилка: Мови '{language}' немає у словнику.")
