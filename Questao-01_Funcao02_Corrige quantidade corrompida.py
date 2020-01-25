#***Autor: Vinicius H. Cazano
#***Programa:Recupera os dados corrompidos
#***Função:Corrige os dados da quantidade corrompidos

def corrigeErroQuantidade(obj):#passa como parametro uma posiçao do dicionario
    if not 'quantity' in obj: #testa se no dicionario contem a chave 'quantity'
        retorno='{"id": "", "name": " ", "quantity": " ", "price": " ","category": ""}' #cria um modelo dos dados do arquivo em string
        retorno= json.loads(retorno) #transforma o modelo em um arquivo json
        #Salva no modelo os valores do dicionario
        retorno['id']=obj['id'] 
        retorno['name']=obj['name']
        retorno['quantity']=0 #coloca na posiçao quantity o valor 0
        retorno['price']=obj['price']
        retorno['category']=obj['category']
        return retorno;#Retorna o modelo criado
        #Fim do salva no modelo os valores do dicionario
    else:#caso contrario retorna o mesmo valor passado pelo parametro
        return obj

