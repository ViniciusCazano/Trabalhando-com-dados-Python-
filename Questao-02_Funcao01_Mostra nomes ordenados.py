#***Autor: Vinicius H. Cazano
#***Programa:valida os dados convertidos
#***Função:Mostrar nomes ordenados

def mostraNomeCategoria(listaDados):#passa como parametro o dicionario inteiro
    nomeCategoria=[]
    nomeCategoria.append(listaDados[0]['category'])
    for aux in range(10):#for que pega todas as categorias salvas
        if not listaDados[aux]['category'] in nomeCategoria:
            nomeCategoria.append(listaDados[aux]['category']);
    #fim do for que pega todas as categorias salvas
    nomeCategoria=sorted(nomeCategoria, key=str)#Organiza a categoria
    
    for categoriaPesquisar in nomeCategoria:#Percorre toda a lista que foi salva as categorias
        listaSalvaId=[]#Cria uma nova lista toda vez que mudar de categoria
        print(categoriaPesquisar)#Imprime qual categoria sera exibida
        for auxContagem in range(10):#for de pesquisa produto
                if listaDados[auxContagem]['category'] == categoriaPesquisar: #adciona todo id que seja igual a categoria pesquisada
                    listaSalvaId.append(listaDados[auxContagem]['id'])#salva o valor do id numa lista
                    
                if auxContagem==9:#se for a ultima passada ela imprimira os valores
                    listaSalvaId=sorted(listaSalvaId, key=int)#Organiza por ordem crescente
                    for PesquisaId in listaSalvaId:#Percorre toda a lista que foi salvo o id
                        for auxMostra in range(10):#Pesquisa nos produtos o id selecionado
                            if listaDados[auxMostra]['id'] == PesquisaId:#verifica se o produto tem o mesmo id
                                print(listaDados[auxMostra])
                                print();
                                break;#pausa a procura
                        #Fim do for que pesquisa nos produtos o id selecionado
                    #Fim do for que percorre toda a lista que foi salvo o id
        #Fim do for de pesquisar produto
    #Fim do for que percorre toda a lista que foi salva as categorias