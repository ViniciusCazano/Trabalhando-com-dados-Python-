#***Autor: Vinicius H. Cazano
#***Programa:Recupera os dados corrompidos
import json

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

def corrigeErroPrice(obj): #passa como parametro uma posiçao do dicionario
    obj['price']=float(obj['price']) #Transforma todo o valor dentro da chave 'price' em decimal
    return obj;

def gravarArquivo(lista):#passa como parametro o dicionario
    with open('./broken-database_Convertido.json', 'w', encoding="utf-8") as f:
        json.dump(lista, f)#Converte para um obj json e salva no arquivo 
        
def salvarArquivo(string):#passa como parametro uma string
    conteudo = open(string, encoding="utf8").read()
    retorno = json.loads(conteudo)
    return retorno #retorna um dicionario de dados


listaDados=salvarArquivo('./broken-database.json')
quantDados=10; #Caso a lista aumentar
for contador in range(quantDados):#entra varrendo cada posiçao do dicionario
    obj =listaDados[contador]
    obj =corrigeErroNome(obj);
    obj =corrigeErroPrice(obj);
    listaDados[contador] =corrigeErroQuantidade(obj);
#fim do for que entra varrendo cada posiçao do dicionario
gravarArquivo(listaDados)

#testa o arquivo salvo
conteudoConvertido = salvarArquivo('./broken-database_Convertido.json')
for obj in conteudoConvertido:
    print(obj);
    print();

input("Pressione enter:")