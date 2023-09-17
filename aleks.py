#from textblob import TextBlob
import textblob

prompt = input("Введите текст:")

#blob = TextBlob(prompt)
#print(len((blob.Sentence))


b = len([i for i in prompt.split('. ')])


word_count = prompt.count(" ") + 1


count = 0
vowels = "аяюоеёэиыaeiou"
for letter in prompt:
    if letter in vowels:
        count += 1



print("Количество слов в строке:", word_count)
print(count)
print(b)

