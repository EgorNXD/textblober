#Egor Nechaev
#Aleksey Polevik
from textblob import TextBlob
from googletrans import Translator
translator = Translator()

prompt = input("Введите текст:")
blob = TextBlob(prompt)
sentences = len([i for i in prompt.split('. ')])
word_count = prompt.count(" ") + 1
count = 0
vowels = "аяюоеёэиыaeiou"
for letter in prompt:
    if letter in vowels:
        count += 1
ASL = word_count/sentences
ASW = count/word_count

blob = translator.translate(prompt, dest='en')
true_language = blob.src
blob = TextBlob(blob.text)
polarity = blob.polarity
subjectivity = blob.subjectivity

if true_language == "ru":
    FRE = 206.835 - 1.52*ASL - 65.14*ASW
else:
    FRE = 206.835 - 1.015*ASL - 84.6*ASW

if polarity <= -0.7:
    pola = "негативный"
elif polarity >= 0.7:
    pola = "позитивный"
else:
    pola = "нейтральный"

if FRE>80:
    diff = "Очень легко читается"
elif 50<FRE<=80:
    diff = "Довольно простой язык"
elif 25<FRE<=50:
    diff = "Немного трудно читать"
elif FRE<=25:
    diff = "Очень трудно читать"

subj = (1 - float(subjectivity))*100

print("Предложений:", sentences)
print("Слов:", word_count)
print("Слогов:", count)
print("Средняя длина текста в словах:", ASL)
print("Средняя длина текста в слогах", ASW)
print("Индекс удобочитаемости Флеша:", FRE)
print(diff)
print("Тональность текста:", pola)
print("Объективность:", subj, "%")
