quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    word_list = message.split()
    return word_list[-3]

print(penult_word(quote_1))
print(penult_word(quote_2))
print(penult_word(quote_3))