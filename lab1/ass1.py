

def dell(text):
    

    myList=[]
    for ch in text:
        if ch is "a" or ch is "o" or ch is "i" or ch is "u" or ch is "e":
            pass
      
        else:
      
            myList.append(ch)

    return "".join(myList)
print(dell("yasmeen"))
#############################

def delVowels(text):
    vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'U', 'I']
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result
print(delVowels("yasmeen"))


#for ch in word:
    #if ch is "a" or ch is "o" or ch is "i" or ch is "u" or ch is "e":
        #word=word.replace(ch,"")
#print(word)
#######################333
#from test3 import fun
#d={'name':'salma','age':20}
#fun(**d)