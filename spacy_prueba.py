import spacy

nlp = spacy.load("en_core_web_md")


apples = nlp("sorrowful")
oranges = nlp("sad")
apples_oranges = apples.similarity(oranges)
oranges_apples = oranges.similarity(apples)
print(apples_oranges)
print(oranges_apples)
assert apples_oranges == oranges_apples