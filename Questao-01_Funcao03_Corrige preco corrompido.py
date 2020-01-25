#***Autor: Vinicius H. Cazano
#***Programa:Recupera os dados corrompidos
#***Função:Corrige os dados do preço corrompidos

def corrigeErroPrice(obj): #passa como parametro uma posiçao do dicionario
    obj['price']=float(obj['price']) #Transforma todo o valor dentro da chave 'price' em float
    return obj;