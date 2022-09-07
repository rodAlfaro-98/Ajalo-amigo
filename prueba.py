import spacy
import pandas as pd
import numpy


nlp = spacy.load("en_core_web_sm")


emociones = pd.read_csv("./archive/train.txt", sep=';', names=["text","emotion"])
print(emociones["emotion"].unique())
emociones2 = pd.read_csv("./archive/val.txt", sep=';', names=["text","emotion"])
emociones_total = emociones.append(emociones2, ignore_index=True)

sadness = emociones_total[emociones_total["emotion"] == "sadness"]
anger = emociones_total[emociones_total["emotion"] == "anger"]
fear = emociones_total[emociones_total["emotion"] == "fear"]

emociones_total = pd.concat([sadness,anger,fear], ignore_index = True)



print("Sadness: {0}".format(sadness.shape[0]))
print("Anger: {0}".format(anger.shape))
print("Fear: {0}".format(fear.shape))
print("Final {0}".format(emociones_total.shape))

sadness_1 = "My day went by full of happiness and hope I thought live was beautiful"

sadness_1 = sadness_1.split(" ")
word_category = []
for i in sadness_1:
  doc = nlp(i)
  word_category.append((i.lower(),doc[0].tag_) if doc[0].tag_ != 'PROPN' else (i,doc[0].tag_))

palabras_final = [i[0] for i in word_category if i[1] != "DET" and i[1] != "ADP" and i[1] != "CCONJ" and i[1] != "CC" and i[1] != "NUM" and i[1] != "PRON"]
print(palabras_final)
print(len(palabras_final))

string_saddness_1 = ""
for i in palabras_final:
    string_saddness_1 += " " + i

similitudes = {}

for i in range(2,anger.shape[0]):

    sadness_2 = anger.iloc[i]["text"]

    sadness_2 = sadness_2.split(" ")

    word_category = []
    for j in sadness_2:
        doc = nlp(j)
        word_category.append((j.lower(),doc[0].tag_) if doc[0].tag_ != 'PROPN' else (i,doc[0].tag_))

    palabras_final = [j[0] for j in word_category if j[1] != "DET" and j[1] != "ADP" and j[1] != "CCONJ" and j[1] != "CC" and j[1] != "NUM" and j[1] != "PRON"]
    
    string_saddness_2 = ""
    for j in palabras_final:
        string_saddness_2 += " " + j

    apples = nlp(string_saddness_1)
    oranges = nlp(string_saddness_2)
    apples_oranges = apples.similarity(oranges)
    oranges_apples = oranges.similarity(apples)

    print(i)
    if(apples_oranges >= 0.70):
        print("Cadena 1: {0}, cadena 2:{1}, similitud: {2}".format(string_saddness_1,string_saddness_2,apples_oranges))
        print(anger.iloc[i]["text"])
        similitudes[anger.iloc[i]["text"]] = ["Cadena 1: {0}, cadena 2:{1}, similitud: {2}".format(string_saddness_1,string_saddness_2,apples_oranges)]
    
for i in range(2,sadness.shape[0]):

    sadness_2 = sadness.iloc[i]["text"]

    sadness_2 = sadness_2.split(" ")

    word_category = []
    for j in sadness_2:
        doc = nlp(j)
        word_category.append((j.lower(),doc[0].tag_) if doc[0].tag_ != 'PROPN' else (i,doc[0].tag_))

    palabras_final = [j[0] for j in word_category if j[1] != "DET" and j[1] != "ADP" and j[1] != "CCONJ" and j[1] != "CC" and j[1] != "NUM" and j[1] != "PRON"]
    
    string_saddness_2 = ""
    for j in palabras_final:
        string_saddness_2 += " " + j

    apples = nlp(string_saddness_1)
    oranges = nlp(string_saddness_2)
    apples_oranges = apples.similarity(oranges)
    oranges_apples = oranges.similarity(apples)

    sadness_id = sadness.iloc[i]["text"]
    print(i)
    if(apples_oranges >= 0.70):
        print("Cadena 1: {0}, cadena 2:{1}, similitud: {2}".format(string_saddness_1,string_saddness_2,apples_oranges))
        print(sadness.iloc[i]["text"])
        if sadness_id in similitudes.keys():
            similitudes[sadness.iloc[i]["text"]] += ["Cadena 1: {0}, cadena 2:{1}, similitud: {2}".format(string_saddness_1,string_saddness_2,apples_oranges)]
        else:
            similitudes[sadness.iloc[i]["text"]] = ["Cadena 1: {0}, cadena 2:{1}, similitud: {2}".format(string_saddness_1,string_saddness_2,apples_oranges)]

for i in similitudes.keys():
    print(similitudes[i])
    print("\n\n")


