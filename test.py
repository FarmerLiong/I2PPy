#!/usr/bin/python3
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return __class__.__name__+repr((self._x, self._y))
    
class ColorPoint(Point):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self._color = color

    def __repr__(self):
        return __class__.__name__+repr((self._x, self._y, self._color))
    
    
        



# import re
# 
# def readStringToDict(inList, splitSymbol):
#     resultDict = {}
#     for e in inList:
#         if e[1:] in resultDict.keys():
#             resultDict[e[1:]] += 1
#         else:
#             resultDict[e[1:]] = 1
#     return(resultDict)
# 
# def sortDic(inDic):
#     sortList = []
#     sortList = sorted(inDic.items(), key = lambda x:(x[1], x[0]), reverse = True)
#     return sortList
# 
# with open("name.txt", encoding = 'utf-8') as fh:
#     resultArray = []
#     for line in fh.readlines():
#         line = line.strip()
#         resultArray.append(line)
# 
# wordDic = readStringToDict(resultArray, "[., ;]")
# print(sortDic(wordDic))

# def readStringToDict(inputStr,splitSymbol):	
#   inList=inputStr.split(splitSymbol)
#   resultDict={}
#   for element in inList:
#     if (element in resultDict.keys()):
#       resultDict[element]=resultDict[element]+1
#     else:
#       resultDict[element]=1	
#   return(resultDict)

# def sortDic(inDic):
#   sortList = []
#   sortList = sorted(inDic.items(), key = lambda pair:pair[0], reverse= True)
#   return (sortList)

# longText= """Let me tell you what this book is not. It is not about religion.
# It is not about telling you how to live your life. It is not about taking on a new set of beliefs.
# Plain and simple, it's about how to relate to your own thoughts and emotions in a way that makes
# your life more enjoyable, more free, brighter, clearer and wiser. We like to think we understand what
# is happening around us; that we can determine the path our life takes.
# But often, things do not go that way - in fact, they rarely do. What helps us respond to life as it unfolds?
# To live freely, stay humble and find comfort in difficult times? In the Swedish sensation I May Be Wrong,
# former forest monk Björn Natthiko Lindeblad shares his advice on how to face the uncertainty and doubt
# that is a natural part of life. We don't choose our thoughts. We don't control the shape they take,
# or what pops into our minds. We can only choose whether or not to believe them. Infusing the
# everyday with heart, grace and gentle humour, this is a book to help us all navigate the realities of modern life."""

# inputtextDic=readStringToDict(longText," ")
# sorted_textCount1=sortDic(inputtextDic)
# top_10_words = sorted_textCount1[:10]




