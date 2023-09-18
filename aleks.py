from textblob import TextBlob

prompt = input("Введите текст:")

blob = TextBlob(prompt)
sentences = len(blob.Sentence)

b = len([i for i in prompt.split('. ')])


word_count = prompt.count(" ") + 1

count = 0
vowels = "аяюоеёэиыaeiou"
for letter in prompt:
    if letter in vowels:
        count += 1

g = b/sentences

h = count/sentences

print("Количество предложений в тексте:", b)
print("Количество слов в строке:", word_count)
print("Количество слогов в тексте:", count)
print("Средняя длина текста в словах:", g)
print("Средняя длина текста в слогах", h)

