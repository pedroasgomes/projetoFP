#TAD Posição--------------------------------------------------------------------

#Construtores

def cria_posicao(x,y):
    
    '''
    A função recebe dois inputs não especificos e após verificar se são ambos 
    inteiros não negativos retorna os inputs em forma de tuplo. 
    A função retorna um tuplo.
    '''
    
    if (type(x) != int or x < 0) or (type(y) != int or y < 0):
        raise ValueError ("cria_posicao: argumentos invalidos")
    return (x,y) 


def cria_copia_posicao(p):
    
    '''
    A função recebe um tuplo que representa uma posição e retorna cada elemento
    em forma de tuplo de modo a criar um novo tuplo.
    A função retorna um tuplo
    '''
    
    return(obter_pos_x(p),obter_pos_y(p)) 


#Seletores

def obter_pos_x(posicao):
    
    '''
    A função recebe um tuplo que representa uma posição e retorna o primeiro
    elemento em forma de inteiro.
    A função retorna um intiero.
    '''
    
    return (posicao[0])
    
    
def obter_pos_y(posicao):
    
    '''
    A função recebe um tuplo que representa uma posição e retorna o segundo
    elemento em forma de inteiro.
    A função retorna um intiero.
    '''    
    
    return (posicao[1])


#Reconhecedores

def eh_posicao(univ):
    
    '''
    A função recebe um input qualquer e verifica se o input verifica as 
    condições do formato interno das posições. Verifica se é tuplo, tamanho
    igual a 2 e se ambos os elementos são inteiros não negativos.
    A função retorna um booleano.
    '''
    
    return (type(univ) == tuple and len(univ) == 2 and\
       type(obter_pos_x(univ)) == int and obter_pos_x(univ) >= 0 and\
       type(obter_pos_y(univ)) == int and obter_pos_y(univ) >= 0)
      
        
#Teste
        
def posicoes_iguais(posicao1,posicao2):
    
    '''
    A função recebe dois tuplos que podem representam posições. Após verificar 
    se as representações são iguais às de uma posição vai comprar ambas
    as posições de modo a verificar se são iguais.
    A função retorna um booleano
    '''
    
    if (eh_posicao(posicao1) == True) and (eh_posicao(posicao2) == True):
        return (posicao1 == posicao2)
    else: return (False) 
    
    
#Transformador
    
def posicao_para_str(posicao):
    
    '''
    A função recebe um tuplo que representa um posição e transforma-o numa
    string.
    A função retorna um string
    '''
    
    return str(posicao) 


#Funções de alto nível associdadas a este TAD
        
def obter_posicoes_adjacentes(posicao):
    
    '''
    A função recebe uma posição. A função vai verificar se as posições em cima, 
    em baixo, à direita, e à esquerda têm elementos não negativos e retorna
    os que verificarem essa condição. As posições são obtidas subtraindo 
    ou somando uma unidade a cada elemento da posição de cada vez.
    A função retorna um tuplo de posições.
    '''
    
    res = ()
    x = obter_pos_x(posicao)
    y = obter_pos_y(posicao)
    
    if y > 0: res += (cria_posicao(x,y-1),)
    res += (cria_posicao(x+1,y),)
    res += (cria_posicao(x,y+1),)
    if x > 0: res += (cria_posicao(x-1,y),)
    
    return(res)


def ordenar_posicoes(tuplo):
    
    '''
    A função recebe um tuplo de posições. A função vai criar um loop onde vai
    verificar por ordem crescente o segundo valor de cada posição e adicionar
    por essa ordem a um novo tuplo. Se houver posições com o mesmo segundo
    elemento a função vai verificar o primeiro elemento e ordenar por ordem
    crescente baseando-se no primeiro elemento. A função termina quando o tuplo
    inicial for de tamanho igual ao novo.
    A função retorna um tuplo de posições ordenadas 
    '''
   
    res = ()
    ys = ()
    n = 0
    
    while len(tuplo) != len(res):
        for posicao in tuplo:
            if obter_pos_y(posicao) == n:
                ys = ys + ((obter_pos_x(posicao),obter_pos_y(posicao)),)
        res = res + ((tuple(sorted(ys))))
        n = n + 1
        ys = ()
            
    return (res)


#TAD Animais--------------------------------------------------------------------


#Construtor

def cria_animal(s,r,a):
    
    '''
    A função recebe três inputs não especificos. Após verificar se o primeiro
    é uma string não vazia, se o segundo é um inteiro positivo e se o terceiro
    é um inteiro não negatvio, a função vai criar um dicionário com 5 entradas
    onde duas têm valor 0 de origem que representam a fome e a idade, uma é
    a especie e o valor é o primeiro input, outra é a frequencia de reprodução
    que é representada pela segunda entrada, e a ultima é a frequencia de
    alimentação e é representada pelo terceiro input.
    A função retorna um dicionário
    '''    
    
    if type(s) != str or type(r) != int or type(a) != int or\
       s == "" or r < 1 or a < 0:
        raise ValueError ("cria_animal: argumentos invalidos")
    return ({"especie":s,"idade":0,"f_rep":r,"fome":0,"f_ali":a})


def cria_copia_animal(animal):
    
    '''
    A funçaõ recebe um dicionário de um animal e retorna uma copia do animal.
    A função retorna um dicionário.
    '''
    return (animal.copy())


#Seletores

def obter_especie(animal):
    
    '''
    A função recebe um dicionário que representa um animal e retorna o valor da
    entrada "especie".
    A função retorna uma string que representa a especie.
    '''
    
    return (animal["especie"])


def obter_freq_reproducao(animal):
    
    '''
    A função recebe um dicionário que representa um animal e retorna o valor da
    entrada "f_rep".
    A função retorna um inteiro que representa a frequencia de alimentacao.
    '''
    
    return (animal["f_rep"])


def obter_freq_alimentacao(animal):
    
    '''
    A função recebe um dicionário que representa um animal e retorna o valor da
    entrada "f_ali".
    A função retorna um inteiro que representa a frequencia de alimentacao.
    '''    
    
    return (animal["f_ali"])


def obter_idade(animal):
    
    '''
    A função recebe um dicionário que representa um animal e retorna o valor da
    entrada "idade".
    A função retorna um inteiro que representa a idade.
    '''      
    
    return (animal["idade"])


def obter_fome(animal):
    
    '''
    A função recebe um dicionário que representa um animal e retorna o valor da
    entrada "fome".
    A função retorna um inteiro que representa a fome.
    '''       
    
    return (animal["fome"])


#Modificadores

def aumenta_idade(animal):
    
    '''
    A função recebe um dicionário que representa um animal e atualiza o valor
    da entrada "idade" por 1.
    A função retorna um dicionário que representa o animal inicial com
    incremento de 1 na idade
    '''
    
    animal.update({"idade":animal["idade"]+1})
    return (animal)


def reset_idade(animal):
    
    '''
    A função recebe um dicionário que representa um animal e atualiza o valor
    da entrada "idade" como 0.
    A função retorna um dicionário que representa o animal inicial com
    idade igual a 0.
    '''    
    
    animal.update({"idade":0})
    return(animal)


def aumenta_fome(animal):
    
    '''
    A função recebe um dicionário que representa um animal e atualiza o valor 
    da entrada "fome" por 1.
    A função retorna um dicionário que representa o animal inicial com
    incremento de 1 na fome.
    '''    
    
    if obter_freq_alimentacao(animal) == 0:
        return (animal)
    else:
        animal.update({"fome":animal["fome"]+1})
        return (animal)


def reset_fome(animal):
    
    '''
    A função recebe um dicionário que representa um animal e atualiza o valor 
    da entrada "fome" como 0.
    A função retorna um dicionário que representa o animal inicial com
    fome igual a 0.
    '''        
    
    if obter_freq_alimentacao(animal) == 0:
            return (animal)    
    else:
        animal.update({"fome":0})
        return(animal)


#Reconhecedores 

def eh_animal(universal):
    
    '''
    A função recebe um input qualquer e vai verificar várias condições de modo
    a filtrar entradas erradas. Primeiro filtra o tipo e o tamanho, de seguida
    filtra as chaves e por último os valores de cada chave. Caso se verifique
    todas as condições a função retorna True, caso contrário False.
    A função retorna um booleano. 
    '''
    
    chaves = ("especie","f_rep","f_ali","idade","fome")
    
    if type(universal) != dict or len(universal) != 5:
        return(False) 
    
    for elementos in universal.keys():
        if elementos not in chaves:
            return(False)   
        
    if type(obter_especie(universal)) != str or\
        type(obter_freq_reproducao(universal)) != int or\
        type(obter_freq_alimentacao(universal)) != int or\
        type(obter_idade(universal)) != int or\
        type(obter_fome(universal)) != int or\
        obter_freq_reproducao(universal) < 1 or\
        obter_freq_alimentacao(universal) < 0 or\
        obter_idade(universal) < 0 or obter_fome(universal) < 0:
        return(False)
    
    return(True)


def eh_predador(animal):
    
    '''
    A função recebe um dicionário que pode representar um possivel animal. Após
    verificar se é realmente a representação de um animal a função verifica
    se a chave "freq_ali" é diferente 0, se for é um predador.
    A função retorna um booleano.
    '''    
    
    return (eh_animal(animal) and obter_freq_alimentacao(animal) != 0)


def eh_presa(animal):
    
    '''
    A função recebe um dicionário que pode representar um possivel animal. Após
    verificar se é realmente a representação de um animal a função verifica
    se a chave "freq_ali" é 0, se for é um presa.
    A função retorna um booleano.
    '''
    
    return (eh_animal(animal) and obter_freq_alimentacao(animal) == 0)


#Teste

def animais_iguais(animal1,animal2):
    
    '''
    A função recebe dois dicionários que pode representar dois possiveis 
    animais. Após verificar se são mesmo representações de animais com a função
    eh_animal a função vai verificar se ambas as representações contêm a mesma 
    informação (True) ou não (False).
    A função retorna um booleano
    '''
    
    return (eh_animal(animal1) and eh_animal(animal2) and animal1==animal2)


#Transformadores

def animal_para_char(animal):
    
    '''A função recebe um dicionário que representa um animal e retorna a 
    primeira letra do valor da chave "especie" e altera a capitalização 
    dependendo se é predador (maiuscula) ou presa (minuscula).
    A função retorna uma string
    '''
    
    if eh_presa(animal):
        return (str.lower(obter_especie(animal)[0]))
    else:
        return (str.upper(obter_especie(animal)[0]))
    
    
def animal_para_str(animal):
    
    '''
    A função recebe um dicionário que representa um animal e retorna a sua 
    representação externa.
    A função retorna uma string
    '''
    
    if eh_presa(animal):
        return(obter_especie(animal)+" "+"["+str(obter_idade(animal))+"/"+\
               str(obter_freq_reproducao(animal))+"]")
     
               
    return(obter_especie(animal)+" "+"["+str(obter_idade(animal))+"/"+\
               str(obter_freq_reproducao(animal))+";"+ str(obter_fome(animal))+\
               "/"+str(obter_freq_alimentacao(animal))+"]")


#Funções de alto nível associdadas a este TAD

def eh_animal_fertil(animal):
    
    '''
    A função verifica se o animal tem idade igual ou superior à sua frequência 
    de reprodução.
    A função retorna o um booleano
    '''    

    return (obter_idade(animal) >= obter_freq_reproducao(animal))      


def eh_animal_faminto(animal):
    
    '''
    A função verifica se o animal é predador com a função eh_predador, já que 
    só os predadores ficam famintos, e verifica se a sua fome é igual
    (ou superior) à sua frequência de alimentação.
    A função retorna o um booleano
    '''
    
    if eh_predador(animal):
        return (obter_fome(animal) >= obter_freq_alimentacao(animal))
    return (False)


def reproduz_animal(animal):
    
    '''
    A função chama a função reset_idade para mudar o value da "idade" para 0 
    e cria uma cópia cujo valor "fome" é alterada para 0 com a função
    reset_fome.
    A função retorna o animal copiado
    '''
    
    reset_idade(animal)
    return (reset_fome(cria_copia_animal(animal)))


#TAD Prado----------------------------------------------------------------------


#Construtor

def cria_prado(d,r,a,p):
    
    '''
    A função recebe quatro inputs que podem ser valores para as chaves do
    diconário que representa internamente o prado. Após verificar se os
    argumentos são coerentes com o tipo de valores que se espera em cada chave
    a função cria um dicionário que representa internamente o prado.
    A função retorna um dicionário.
    '''
    
    if not eh_posicao(d):
        raise ValueError ("cria_prado: argumentos invalidos") 
    
    if not (type(r)==type(a)==type(p)==tuple):
        raise ValueError ("cria_prado: argumentos invalidos")
    
    for elementos in r:
        if not eh_posicao(elementos) or not \
           0 < obter_pos_x(elementos) < obter_pos_x(d) or not\
           0 < obter_pos_y(elementos) < obter_pos_y(d):
            raise ValueError ("cria_prado: argumentos invalidos") 
            
    for elementos in a: 
        if not eh_animal(elementos):
            raise ValueError ("cria_prado: argumentos invalidos")
        
    for elementos in p:
        if not eh_posicao(elementos):
            raise ValueError ("cria_prado: argumentos invalidos")
        
    if len(a) != len(p):
        raise ValueError ("cria_prado: argumentos invalidos")
    
    if ordenar_posicoes(p)+(d,) != ordenar_posicoes(p+(d,)):
        raise ValueError ("cria_prado: argumentos invalidos")    

    return({"limite":d,"obstaculos":r,"animais":a,"posicoes":p})


def cria_copia_prado(prado):
    
    '''
    A função recebe um dicionário que representa um prado e cria uma cópia do
    prado.
    A função retorna um dicionário.
    '''
    
    return ({"limite":prado["limite"],"obstaculos":prado["obstaculos"],\
             "animais":prado["animais"],"posicoes":prado["posicoes"]})


#Seletores

def obter_tamanho_x(prado):
    
    '''
    A função recebe um dicionário que representa um prado e devolve o seu 
    tamanho em função do eixo do x.
    A função retorna um inteiro.
    '''
    
    return(obter_pos_x(prado["limite"])+1)
           
           
def obter_tamanho_y(prado):
    
    '''
    A função recebe um dicionário que representa um prado e devolve o seu 
    tamanho em função do eixo do y. A função retorna um inteiro.
    '''
    
    return(obter_pos_y(prado["limite"])+1)
           
           
def obter_numero_predadores(prado):
    
    '''
    A função recebe um dicionário que representa um prado e vai verificar o 
    número de predadores chamando a função eh_predador.
    A função retorna um inteiro
    '''
    
    res = 0
    
    for elementos in prado["animais"]:
        if eh_predador(elementos):
            res += 1
    return (res)


def obter_numero_presas(prado):
    
    '''
    A função recebe um dicionário que representa um prado e vai verificar o 
    número de presas chamando a função eh_presa.
    A função retorna um inteiro
    '''    
    
    res = 0
    
    for elementos in prado["animais"]:
        if eh_presa(elementos):
            res += 1
    return (res)


def obter_posicao_animais(prado):
    
    '''
    A função recebe um dicionário que representa um prado e retorna todas as 
    posições que são ocupadas por animais de forma ordenada chamando a 
    função ordenar_posicoes.
    A função retorna um tuplo de posições.
    '''
    
    return(ordenar_posicoes(prado["posicoes"]))


def obter_animal(prado,posicao):
    
    '''
    A função recebe um dicionário que representa um prado e um tuplo que 
    representa uma posição e retorna o animal que ocupa a posição.
    A função retorna um diconário que representa o animal.
    '''    
    
    n = (prado["posicoes"].index(posicao))
    return (prado["animais"][n])


#Modificadores

def eliminar_animal(prado,posicao):
    
    '''
    A função recebe um dicionário que representa um prado e um tuplo que 
    representa uma posição e vai eliminar o animal e a respetiva posição dos 
    valores do prado.
    A função retorna o novo dicionário que representa o prado sem o animal e a
    respetiva posição.
    '''
    
    n = (prado["posicoes"].index(posicao))
    prado["animais"] = prado["animais"][:n] + prado["animais"][n+1:]
    prado["posicoes"] = prado["posicoes"][:n] + prado["posicoes"][n+1:]
    
    return(prado)


def mover_animal(prado,p_inicio,p_fim):
    
    '''
    A função recebe um dicionário que representa um prado e dois tuplos que 
    representam posições e vai alterar o valor da posicao do animal que
    se encontra na primeira posição fornecida pela segunda posição fornecida.
    A função retorna o novo dicionário que representa o prado com a posição do 
    animal atualizada.
    '''
    
    n = (prado["posicoes"].index(p_inicio))
    prado["posicoes"] = prado["posicoes"][:n]+(p_fim,)+prado["posicoes"][n+1:]
    return (prado)


def inserir_animal(prado,animal,posicao):
    
    '''
    A função recebe um dicionário que representa um prado, um dicionário que 
    representa um animal e um tuplo que representa uma posição e vai adicionar
    ao dicionário do prado o animal e a respetiva posição.
    A função retorna o novo dicionário que representa o prado com o novo animal.
    '''
    
    prado["posicoes"] = prado["posicoes"]+(posicao,)
    prado["animais"] = prado["animais"]+(animal,)
    return(prado)


#Reconhecedores

def eh_prado(univ):
    
    '''
    A função recebe um input qualquer e vai verificar várias condições de modo
    a filtrar entradas erradas. Verifica o tipo, o tamanho e os valores
    das entradas de modo a filtrar entradas que mão sejam representações 
    internas coerentes de um prado.
    A função retorna um booleano. 
    '''
    
    chaves = ("limite","obstaculos","animais","posicoes")
    
    if type(univ) != dict or len(univ) != 4: 
        return False   
    
    for elementos in univ.keys():
        if elementos not in chaves:
            return False
        
    if not eh_posicao(univ["limite"]):
        return False
    
    if not type(univ["obstaculos"])==type(univ["animais"])==\
       type(univ["posicoes"])==tuple:
        return False         
            
    if univ["obstaculos"] != ():    
        for elementos in univ["obstaculos"]:
            if not eh_posicao(elementos) or not\
               0 < obter_pos_x(elementos)< obter_pos_x(univ["limite"])\
               or not\
               0 < obter_pos_y(elementos)< obter_pos_y(univ["limite"]):
                return False
            
    for elementos in univ["animais"]:
        if not eh_animal(elementos):
            return False
        
    for elementos in univ["posicoes"]:
        if not eh_posicao(elementos):
            return False
        
    if len(univ["animais"]) != len(univ["posicoes"]):
        return False
    
    if ordenar_posicoes(univ["posicoes"])+((univ["limite"]),) !=\
       ordenar_posicoes(univ["posicoes"]+(univ["limite"],)):
        return False
    
    return True


def eh_posicao_animal(prado,posicao):
    
    '''
    A função recebe um dicionário que representa um prado e um tuplo que 
    representa uma posição e verifica se essa posição é ocupada por um animal.
    A função retorna um booleano.
    '''
    
    return (posicao in obter_posicao_animais(prado))


def eh_posicao_obstaculo(prado,posicao):
    
    '''
    A função recebe um dicionário que representa um prado e um tuplo que 
    representa uma posição e verifica se essa posição é ocupada por um 
    obstaculo.
    A função retorna um booleano.
    '''    
    
    x = obter_pos_x(posicao)
    y = obter_pos_y(posicao)
    
    return (x <= 0 or y <= 0 or\
       x >= (obter_tamanho_x(prado)-1) or y >= (obter_tamanho_y(prado)-1) or\
       posicao in prado["obstaculos"])


def eh_posicao_livre(prado,posicao):
    
    '''
    A função recebe um dicionário que representa um prado e um tuplo que 
    representa uma posição e verifica se essa posição está livre, ou seja, 
    não tem nenhum animal ou obstáculo.
    A função retorna um booleano.
    '''        

    return (posicao not in obter_posicao_animais(prado) and not\
            eh_posicao_obstaculo(prado,posicao))


#Testes

def prados_iguais(prado1,prado2):
    
    '''
    A função recebe dois dicionários que representam prados e verifica se 
    ambos têm a mesma representação não tendo em conta a ordem dos valores das
    entradas de cada dicionário.
    A função retorna um booleano.
    '''
    
    return(eh_prado(prado1) and eh_prado(prado2) and\
            prado1["limite"] == prado2["limite"] and\
            sorted(prado1["obstaculos"]) == sorted(prado2["obstaculos"]) and\
            prado1["animais"] == prado2["animais"] and\
            prado1["posicoes"] == prado2["posicoes"])
            

#Transformador

def prado_para_str(prado):
    
    '''
    A função recebe um dicionário que representa um prado e vai dividir cada
    "linha" do prado em listas. Cada lista vai representar todos os elementos
    com o mesmo y. Primeiro é criada a linha limite e a partir daí
    são criadas sucessivamente linhas com os limites ("|") e preenchidas no meio
    por ".". No final são verificadas as posições dos animais e obstáculos
    e o elemento número x da lista é subtituido pela representação do 
    objeto ou animal que tem x igual ao número do elemento. No final é criada
    a linha limite inferior.
    A função retorna uma string que representa o prado.
    '''
    
    prado_inteiro = ["+"]+["-"]*(obter_tamanho_x(prado)-2)+["+\n"]
    
    for n in range(1,obter_tamanho_y(prado)-1):
        
        prado_linha = ["|"]+["."]*(obter_tamanho_x(prado)-2)+["|\n"]
        
        for elementos in prado["obstaculos"]:
            if obter_pos_y(elementos) == n:
                prado_linha[obter_pos_x(elementos)] = "@"
                
        for elementos in obter_posicao_animais(prado):
            if obter_pos_y(elementos) == n:
                prado_linha[obter_pos_x(elementos)] =\
                    animal_para_char(obter_animal(prado,elementos))
                
        prado_inteiro += prado_linha
        
    prado_inteiro += ["+"]+["-"]*(obter_tamanho_x(prado)-2)+["+"]
    return("".join(prado_inteiro))



#Funções de alto nível associdadas a este TAD



def obter_valor_numerico(prado,posicao):
    
    '''
    A função recebe um dicionário que representa um prado e um tuplo que 
    representa uma posição e devolve o valor númerico da posição.
    A função retorna um inteiro.
    '''
    
    return(obter_pos_y(posicao)*(obter_tamanho_x(prado))+\
           obter_pos_x(posicao))
    
    
    
def obter_movimento(prado,posicao):
    
    '''
    A função recebe um dicionário que representa um prado e um tuplo que 
    representa uma posição e vai verificar qual será a moviemntação do
    animal nessa posição. Primeiro verifica se é predador, se for e tiver presas
    à sua volta vai devorar uma e ocupar o seu lugar. Caso não haja presas ou
    o próprio animal seja uma presa vai deslocar-se para uma posição adjacente
    se houver posições livres, se não houver o animal não se move.
    Quando há múltiplas posições para escolher o animal segue uma regra.
    A função retorna um inteiro.
    '''

    posicoes = ()
    if eh_predador(obter_animal(prado,posicao)):
        for elementos in obter_posicoes_adjacentes(posicao):
            if eh_posicao_animal(prado,elementos) and\
               eh_presa(obter_animal(prado,elementos)):
                posicoes += (elementos,)
        if posicoes != ():
            return(posicoes[obter_valor_numerico(prado,posicao)%len(posicoes)])
    for elementos in obter_posicoes_adjacentes(posicao):
        if eh_posicao_livre(prado,elementos):
                posicoes += (elementos,)
    if posicoes != ():
        return(posicoes[obter_valor_numerico(prado,posicao)%len(posicoes)])
    return(posicao)
    
    
#Funcoes Adicionais-------------------------------------------------------------


def geracao(prado):
    
    '''
    A função recebe um prado e vai aplicar a cada animal a transformação 
    descrita na função obter_movimento, seguindo a ordem do
    obter_valor_numerico. No inicio de cada turno todos os animais aumentam 
    a sua idade e no caso dos predadores a fome. Se um animal fertil 
    se mover vai deixar para trás um descedente e vai resetar a sua idade.
    Se um predador devorar uma presa, essa presa é eliminada e a fome do animal
    reseta. Se no fim do seu turno um predador tiver faminto é eliminado.
    A função retorna um dicionário que representa o prado com as transformações.
    '''

    posicoes = list(ordenar_posicoes(obter_posicao_animais(prado)))
    while len(posicoes) != 0:
        
        
        next_move = obter_movimento(prado,posicoes[0])
        aumenta_idade(obter_animal(prado,posicoes[0]))
    
    
        if eh_presa(obter_animal(prado,posicoes[0])):
            if eh_animal_fertil(obter_animal(prado,posicoes[0])) and not\
                                      posicoes_iguais(posicoes[0],next_move):
                inserir_animal(prado,reproduz_animal\
                        (obter_animal(prado,posicoes[0])),posicoes[0])
            mover_animal(prado,posicoes[0],next_move)
           
    
        else: 
            aumenta_fome(obter_animal(prado,posicoes[0]))
            if eh_posicao_animal(prado,next_move) and not\
                                      posicoes_iguais(posicoes[0],next_move):
                eliminar_animal(prado,next_move)
                reset_fome(obter_animal(prado,posicoes[0]))
                if next_move in posicoes:
                    posicoes.remove (next_move)
                
            if eh_animal_fertil(obter_animal(prado,posicoes[0])) and not\
                                          posicoes_iguais(posicoes[0],next_move):
                inserir_animal(prado,reproduz_animal\
                            (obter_animal(prado,posicoes[0])),posicoes[0])
            mover_animal(prado,posicoes[0],next_move) 
            
            if eh_animal_faminto(obter_animal(prado,next_move)):
                eliminar_animal(prado,next_move)
        posicoes = posicoes[1:]

                 
    return(prado)

def simula_ecossistema(ficheiro,inteiro,booleano):
    
    '''
    A função recebe um ficheiro que contém as informações do prado, um inteiro
    que representa o número de gerações e um booleano que define o modo 
    (silencioso ou verboso). Primeiro a função vai pegar nos argumentos
    do ficheiro e converter num prado.
    Após a criação do prado a função vai verficar o valor do booleano. Se for
    True, significa que foi ativado o modo verboso e cada vez que o número 
    de predadores ou presas for alterado vai dar print à representação
    externa do prado e ao número que indica a quantidade de animais.
    Se o booleano for Fasle a função apenas dá print à primeira e última 
    representação do prado com as informações da quantidade de animais.
    A função retorna um tuplo que representa o número final de predadores e 
    presas.
    '''
    
    file = open(ficheiro, "r", encoding = "UTF-8")
    limite = eval(file.readline())
    limite = cria_posicao(obter_pos_x(limite),obter_pos_y(limite))
    obstaculos_posicao = ()
    obstaculos = eval(file.readline())
    for elementos in obstaculos:
        obstaculos_posicao += ((cria_posicao(obter_pos_x(elementos),obter_pos_y(elementos))),)
    animais_posicoes = file.readlines()
    n = 0
    prado = cria_prado(limite,obstaculos_posicao,(),())
    for elem in animais_posicoes:
        elem = eval(elem)
        inserir_animal(prado,cria_animal(elem[0],elem[1],elem[2]),elem[3])
    file.close()


    print("Predadores: "+str(obter_numero_predadores(prado))+\
          " vs Presas: "+str(obter_numero_presas(prado))+" (Gen. 0)\n"+\
          (prado_para_str(prado)))
    
    
    if not booleano:
        for n in range(1,inteiro+1):
            geracao(prado)
        print("Predadores: "+str(obter_numero_predadores(prado))+\
          " vs Presas: "+str(obter_numero_presas(prado))+" (Gen. "+str(n)+")\n"+\
          (prado_para_str(prado)))
        return((obter_numero_predadores(prado)),(obter_numero_presas(prado)))
    
    
    for n in range(1,inteiro+1):
        predadores = (obter_numero_predadores(prado))
        presas = (obter_numero_presas(prado))
        geracao(prado)
        predadores_depois = (obter_numero_predadores(prado))
        presas_depois = (obter_numero_presas(prado))
        if presas != presas_depois or predadores != predadores_depois:
            print("Predadores: "+str(obter_numero_predadores(prado))+\
                  " vs Presas: "+str(obter_numero_presas(prado))+\
                  " (Gen. "+str(n)+")\n"+\
                  (prado_para_str(prado)))  
    return((obter_numero_predadores(prado)),(obter_numero_presas(prado)))

