#***Autor: Vinicius H. Cazano
#***Programa:Recupera os dados corrompidos
#***Função:Corrige os nomes corrompidos

def corrigeErroNome(obj):#passa como parametro uma posiçao do dicionario e retorna uma posiçao do dicionario
    SalvaNomeCorrompido = obj['name']; #salva o valor da chave do dicionario
    #troca os valores
    SalvaNomeCorrompido = SalvaNomeCorrompido.replace("æ", "a"); 
    SalvaNomeCorrompido = SalvaNomeCorrompido.replace("¢", "c");
    SalvaNomeCorrompido = SalvaNomeCorrompido.replace("ø", "o");
    SalvaNomeCorrompido = SalvaNomeCorrompido.replace("ß", "b");
    #fim de troca os valores
    obj['name'] =SalvaNomeCorrompido; # salva em cima do valor da chave do dicionario
    return obj;