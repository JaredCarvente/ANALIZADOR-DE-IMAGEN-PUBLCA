#THIS MODULE PROVIDES ALL FUNCTIONS TO ANALIZE TEXT PARAMETERS

def words_frequency(words_list):
    words_count={} 
    for word in words_list:
        if word in words_count:
            words_count[word]=words_count[word]+1
        else:
            words_count[word]=1
    return words_count #RETURNS A DICTIONARY INDICATING A SPECIFIC WORD ALONG WITH ITS FREQUENCY

def most_frequent(words_count, top): 
    aux={}
    for element in words_count:
        aux[element]=words_count[element]#este se le irán eliminando elementos dinamicamente
        #recuerda que al ir recorriendo un diccionario se irá recorriendo por medio de la clave y no del valor
     
    aux2={}   #aqui se iran guardando los elementos de mayor frecuencia
    try:
        for element in range(top):
            clave_max=max(aux,key=aux.get) #GET THE MOST FREQUENT WORD IN THE AUX DICT
            aux2[clave_max]=aux[clave_max]
            aux.pop(clave_max)              
        return aux2                     #RETURNS A DICT WITH THE TOP(top) WORDS
    except:
        for element in range(len(aux)):
            clave_max=max(aux,key=aux.get)
            aux2[clave_max]=aux[clave_max]
            aux.pop(clave_max)
        return aux2                     #RETURNS A DICT WITH THE TOP(LEN(AUX)) WORDS