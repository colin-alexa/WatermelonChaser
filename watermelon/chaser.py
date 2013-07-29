#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, codecs, loadSpam
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

from dcavarCorpus import *
from math import log

open("spam_report.wc", 'w').close()

for i in range(1,6):
  spamFiles, testData = loadSpam.split_data(i,5,loadSpam.spamPath)
  spam = []
  for file in spamFiles:
   print(file)
   sFile = open(file, 'r')
   try:
    spam = spam + tokenize(sFile.read().lower())
   except UnicodeDecodeError:
    sFile.close()
    print("error.")
    continue
   sFile.close()
   print("done.")

  temp = loadSpam.split_data(i,5,loadSpam.hamPath)
  hamFiles = temp[0]
  testData = testData + temp[1]
  
  ham = []
  for file in hamFiles:
   hFile = open(file, 'r')
   try:
    ham = ham + tokenize(hFile.read().lower())
   except UnicodeDecodeError:
    hFile.close()
    print("error.")
    continue
   hFile.close()
   
   
  N = 1
  spamFP = getNGramModel(spam, N)
  relativizeFP(spamFP)
  
  hamFP = getNGramModel(ham, N)
  relativizeFP(hamFP)
  
  test = []
  for file in testData:
   tFile = open(file, 'r')
   try:
    test = test + [(file , tokenize(tFile.read().lower()))]
   except UnicodeDecodeError:
    tFile.close()
    print("error.")
    continue
   tFile.close()
   
  for message in test:
    spamProb = 0.0
    hamProb = 0.0
    wiggle = 1.05
    for token in message[1]:
        spamProb -= log(spamFP.get(token, 0.000000000001))
        hamProb -= log(hamFP.get(token, 0.000000000001))
        # I changed the += to a -= so that the resulting probabilities would be positive and I could use the wiggle uncertainty check later. Because of that, the comparisons below are reversed.
        

    likelihoodMessage = "Spam likelihood: " + str(spamProb) + "\nHam likelihood: " + str(hamProb) + "\n\n"
    outputFile = open("spam_report.wc", 'a')
    
    if spamProb < (hamProb * wiggle):
        print( message[0] + "; This message is probably spam.", likelihoodMessage, sep='\n', file=outputFile)
    elif hamProb < (spamProb * wiggle):
        print( message[0] + "; This message looks good!", likelihoodMessage, sep='\n', file=outputFile)
    else:
        print( message[0] + "; The classifier is uncertain about this message.", likelihoodMessage, sep='\n', file=outputFile)