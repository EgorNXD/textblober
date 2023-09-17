from textblob import TextBlob
prompt = input("Введите текст:")

blob = TextBlob(prompt)
print(len((blob.sentences)))

word_count = prompt.count(" ") + 1
print("Количество слов в строке:", word_count)

average_length = word_count%