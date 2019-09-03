# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:48:57 2019

@author: Gummo
"""

import sys        # command line arguments

if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

# remove unwanted characters
def replace(string):
    string = string.lower()
    remove = ['!', ',', '.', '-', ';', ':', '%', '\"', '\\', '\'', '\\r', '\\n']
    for c in remove:
        if c in string:
            string = string.replace(c,' ')
    return string
 
# open file split into list
# this should be able to go in less lines
def rf(arg1):
    f1 = open(arg1, "r")
    text = f1.read()
    text = replace(text)
    text = sorted(text.split())
    return toDic(text)
 
# from a word list add new keys 
def toDic(fList):
    fDic = {}
    for word in fList:
        if word in fDic:
            fDic[word] += 1
        else:
            fDic[word] = 1
    return fDic
 
def writeDict(dic, fileName):
    for stuff, moreStuff in dic.items():
        fileName.write(stuff + " " + str(moreStuff) + "\n")
 
dic = rf(textFname)
#printDict(dic)
 
writeDict(dic, open(outputFname, "w"))
