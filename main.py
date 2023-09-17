from textblob import TextBlob
from googletrans import Translator
translator = Translator()
blob = input("Введите текст:")

blob = translator.translate(blob, dest='en')
blob = TextBlob(blob.text)
polarity = blob.polarity
subjectivity = blob.subjectivity


print(polarity)
print(subjectivity)
print(blob)
