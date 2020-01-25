#***Autor: Vinicius H. Cazano
#***Programa:valida os dados convertidos
#***Função:Mostra soma do valor dos produtos por categoria

def somaCategoriaFuncao(listaDados):#passa como parametro o dicionario inteiro
    nomeCategoria=[]
    nomeCategoria.append(listaDados[0]['category'])
    for aux in range(10):#for que pega todas as categorias salvas
        if not listaDados[aux]['category'] in nomeCategoria:
            nomeCategoria.append(listaDados[aux]['category']);
    #fim do for que pega todas as categorias salvas
    
    for categoriaPesquisar in nomeCategoria:#Percorre toda a lista que foi salva as categorias
        soma=0.0#Toda vez que mudar de categoria a variavel é zerada
        for auxContagem in range(10):#for de pesquisa produto
            if listaDados[auxContagem]['category'] == categoriaPesquisar:
                soma+=listaDados[auxContagem]['price']*listaDados[auxContagem]['quantity'];
                
            if auxContagem == 9:#caso seja a ultima passada ele imprime a soma 
                print(categoriaPesquisar+": "+ str(soma))
        #fim do for de pesquisa produto
