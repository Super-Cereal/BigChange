from transliterate import translit


def convert_ru_to_eng(text):
    return translit(text, 'ru', reversed=True)
