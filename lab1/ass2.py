





def search_for_word(word,letter):
    myList=[]
    myindex=[]
    count=-1;
    for ch in word:
        if ch is letter:
            count=count+1;
            myindex.append(count)
            myList.append(ch)
          
        else:
           
            count=count+1;
           
 
   
    return myindex


print(search_for_word("fggttrv",'g'))