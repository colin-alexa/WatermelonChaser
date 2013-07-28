#!/usr/bin/env python3


from corpus import getTextFromFile, tokenize, makeFrequencyProfile, removeJunk, prettyPrintFRP


for x in range (1,6):
    loadSpam.split_data( x , 5, spamPath)

for file in spamList:
    mytokens = tokenize(getTextFromFile(file) )

mydict = makeFrequencyProfile(mytokens)

junk = " ,;:-+=()[]'\"?!%.<>"

removeJunk(mydict, junk)

if "" in mydict:
   del mydict[""]

prettyPrintFRP (mydict)
