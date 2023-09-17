from textblob import TextBlob
prompt = input("Введите текст:")
blob = TextBlob(prompt)
polarity = blob.polarity
subjectivity = blob.subjectivity
print(polarity)
print(subjectivity)
print(blob)
