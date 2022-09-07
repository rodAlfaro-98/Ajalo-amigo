import spacy
import pandas as pd
import numpy

def getSimilarities(input):

    if ("suicide" in input) or ("murder" in input) or ("kill" in input) or ("selfharm" in input):
        return 5000

    nlp = spacy.load("en_core_web_md")

    emociones = pd.read_csv("./archive/train.txt", sep=';', names=["text","emotion"])
    print(emociones["emotion"].unique())
    emociones2 = pd.read_csv("./archive/val.txt", sep=';', names=["text","emotion"])
    emociones_total = emociones.append(emociones2, ignore_index=True)
    
    sadness = emociones_total[emociones_total["emotion"] == "sadness"]
    anger = emociones_total[emociones_total["emotion"] == "anger"]
    fear = emociones_total[emociones_total["emotion"] == "fear"]
    
    emociones_total = pd.concat([sadness,anger,fear], ignore_index = True)
    
    sadness_1 = input
    
    sadness_1 = sadness_1.split(" ")
    word_category = []
    for i in sadness_1:
        doc = nlp(i)
        word_category.append((i.lower(),doc[0].tag_) if doc[0].tag_ != 'PROPN' else (i,doc[0].tag_))
    
    palabras_final = [i[0] for i in word_category if i[1] != "DET" and i[1] != "ADP" and i[1] != "CCONJ" and i[1] != "CC" and i[1] != "NUM" and i[1] != "PRON" and (i[0] != "feel" or i[0] != "felt")]
    
    string_saddness_1 = ""
    for i in palabras_final:
        string_saddness_1 += " " + i
    
    similitudes = 0
    
    for i in range(2,anger.shape[0]):
    
        sadness_2 = anger.iloc[i]["text"]
    
        sadness_2 = sadness_2.split(" ")
    
        word_category = []
        for j in sadness_2:
            doc = nlp(j)
            word_category.append((j.lower(),doc[0].tag_) if doc[0].tag_ != 'PROPN' else (i,doc[0].tag_))
    
        palabras_final = [j[0] for j in word_category if j[1] != "DET" and j[1] != "ADP" and j[1] != "CCONJ" and j[1] != "CC" and j[1] != "NUM" and j[1] != "PRON"  and (j[0] != "feel" or j[0] != "felt")]
        
        string_saddness_2 = ""
        for j in palabras_final:
            string_saddness_2 += " " + j
    
        similitud1 = nlp(string_saddness_1)
        similitud2 = nlp(string_saddness_2)
        similitud = similitud1.similarity(similitud2)
    
        print(i)
        if(similitud >= 0.90):
            #print("Cadena 1: {0}, cadena 2:{1}, similitud: {2}".format(string_saddness_1,string_saddness_2,similitud))
            #print(anger.iloc[i]["text"])
            similitudes += 1
        
    for i in range(2,sadness.shape[0]):
    
        sadness_2 = sadness.iloc[i]["text"]
    
        sadness_2 = sadness_2.split(" ")
    
        word_category = []
        for j in sadness_2:
            doc = nlp(j)
            word_category.append((j.lower(),doc[0].tag_) if doc[0].tag_ != 'PROPN' else (i,doc[0].tag_))
    
        palabras_final = [j[0] for j in word_category if j[1] != "DET" and j[1] != "ADP" and j[1] != "CCONJ" and j[1] != "CC" and j[1] != "NUM" and j[1] != "PRON"  and (j[0] != "feel" or j[0] != "felt")]
        
        string_saddness_2 = ""
        for j in palabras_final:
            string_saddness_2 += " " + j
    
        similitud1 = nlp(string_saddness_1)
        similitud2 = nlp(string_saddness_2)
        similitud = similitud1.similarity(similitud2)
    
        print(i)
        if(similitud >= 0.90):
            #print("Cadena 1: {0}, cadena 2:{1}, similitud: {2}".format(string_saddness_1,string_saddness_2,similitud))
            #print(sadness.iloc[i]["text"])
            similitudes += 1
    
    return len(similitudes)
