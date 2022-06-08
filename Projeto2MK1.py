
#TAD Posição--------------------------------------------------------------------

#Construtores

def cria_posicao(x,y):
    
    if (type(x) != int or x < 0) or (type(y) != int or y < 0):
        raise ValueError ("cria_posicao: argumentos invalidos")
    return (x,y) 

def cria_copia_posicao(p):
    
    return(p) 

#Seletores

def obter_posicao_x(posicao):
    
    return (posicao[0])
    
def obter_posicao_y(posicao):
    
    return (posicao[1])

#Reconhecedores

def eh_posicao(univ):
    
#univ stands for universal to shorten the lines of the code   
    
    return (type(univ) == tuple and len(univ) == 2 and\
       type(obter_posicao_x(univ)) == int and obter_posicao_x(univ) >= 0 and\
       type(obter_posicao_y(univ)) == int and obter_posicao_y(univ) >= 0)
        
#Teste
        
def posicao_iguais(posicao1,posicao2):
    
    if (eh_posicao(posicao1) == True) and (eh_posicao(posicao2) == True):
        return (posicao1 == posicao2)
    else: return (False) 
    
#Transformador
    
def posicao_para_str(posicao):
    
    return str(posicao) 

#Funções de alto nível associdadas a este TAD
        
def obter_posicoes_adjacentes(posicao):
    
    res = ()
    x = obter_posicao_x(posicao)
    y = obter_posicao_y(posicao)
    
    if y > 0: res += (cria_posicao(x,y-1),)
    res += (cria_posicao(x+1,y),)
    res += (cria_posicao(x,y+1),)
    if x > 0: res += (cria_posicao(x-1,y),)
    
    return(res)

def ordenar_posicoes(tuplo):
   
    res = ()
    ys = ()
    n = 0
    
    while len(tuplo) != len(res):
        for posicao in tuplo:
            if obter_posicao_y(posicao) == n:
                ys = ys + ((obter_posicao_x(posicao),obter_posicao_y(posicao)),)
        res = res + ((tuple(sorted(ys))))
        n = n + 1
        ys = ()
            
    return (res)


#TAD Animais--------------------------------------------------------------------

#Construtor

def cria_animal(s,r,a):
    
    if type(s) != str or type(r) != int or type(a) != int or\
       s == "" or r < 1 or a < 0:
        raise ValueError ("cria_animal: argumentos invalidos")
    return ({"especie":s,"idade":0,"f_rep":r,"fome":0,"f_ali":a})

def cria_copia_animal(animal):
    return (animal.copy())

#Seletores

def obter_especie(animal):
    
    return (animal["especie"])

def obter_freq_reproducao(animal):
    
    return (animal["f_rep"])

def obter_freq_alimentacao(animal):
    
    return (animal["f_ali"])

def obter_idade(animal):
    
    return (animal["idade"])

def obter_fome(animal):
    
    return (animal["fome"])

#Modificadores

def aumenta_idade(animal):
    
    animal.update({"idade":animal["idade"]+1})
    return (animal)

def reset_idade(animal):
    
    animal.update({"idade":0})
    return(animal)

def aumenta_fome(animal):
    
    if obter_freq_alimentacao(animal) == 0:
        return (animal)
    else:
        animal.update({"fome":animal["fome"]+1})
        return (animal)

def reset_fome(animal):
    
    if obter_freq_alimentacao(animal) == 0:
            return (animal)    
    else:
        animal.update({"fome":0})
        return(animal)

#Reconhecedores 

def eh_animal(universal):
    
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
    
    return (eh_animal(animal) and obter_freq_alimentacao(animal) != 0)

def eh_presa(animal):
    
    return (eh_animal(animal) and obter_freq_alimentacao(animal) == 0)

#Teste

def animais_iguais(animal1,animal2):
    
    return (eh_animal(animal1) and eh_animal(animal2) and animal1==animal2)

#Transformadores

def animal_para_char(animal):
    
    if eh_presa(animal):
        return (str.lower(obter_especie(animal)[0]))
    else:
        return (str.upper(obter_especie(animal)[0]))
    
def animal_para_str(animal):
    
    if eh_presa(animal):
        return(obter_especie(animal)+" "+"["+str(obter_idade(animal))+"/"+\
               str(obter_freq_reproducao(animal))+"]")
     
               
    return(obter_especie(animal)+" "+"["+str(obter_idade(animal))+"/"+\
               str(obter_freq_reproducao(animal))+";"+ str(obter_fome(animal))+\
               "/"+str(obter_freq_alimentacao(animal))+"]")

#Funções de alto nível associdadas a este TAD

def eh_animal_fertil(animal):

    return (obter_idade(animal) >= obter_freq_reproducao(animal))      

def eh_animal_faminto(animal):
    
    if eh_predador(animal):
        return (obter_fome(animal) >= obter_freq_alimentacao(animal))
    return (False)

def reproduz_animal(animal):
    
    reset_idade(animal)
    return (reset_fome(cria_copia_animal(animal)))


#TAD Prado----------------------------------------------------------------------

#Construtor

def cria_prado(d,r,a,p):
    
    if not eh_posicao(d):
        raise ValueError ("cria_prado: argumentos invalidos") 
    
    if not (type(r)==type(a)==type(p)==tuple):
        raise ValueError ("cria_prado: argumentos invalidos")
    
    for elementos in r:
        if not eh_posicao(elementos):
            raise ValueError ("cria_prado: argumentos invalidos") 
            
    for elementos in a: 
        if not eh_animal(elementos):
            raise ValueError ("cria_prado: argumentos invalidos")
        
    for elementos in p:
        if not eh_posicao(elementos):
            raise ValueError ("cria_prado: argumentos invalidos")
        
    if len(a) != len(p):
        raise ValueError ("cria_prado: argumentos invalidos")   

    return({"limite":d,"obstaculos":r,"animais":a,"posicoes":p})

def cria_copia_prado(prado):
    
    return (prado.copy())

#Seletores

def obter_tamanho_x(prado):
    
    return(obter_posicao_x(prado["limite"])+1)
           
def obter_tamanho_y(prado):
    
    return(obter_posicao_y(prado["limite"])+1)
           
def obter_numero_predadores(prado):
    
    res = 0
    
    for elementos in prado["animais"]:
        if eh_predador(elementos):
            res += 1
    return (res)

def obter_numero_presas(prado):
    
    res = 0
    
    for elementos in prado["animais"]:
        if eh_presa(elementos):
            res += 1
    return (res)

def obter_posicao_animais(prado):
    
    return(ordenar_posicoes(prado["posicoes"]))

def obter_animal(prado,posicao):
    
    n = (prado["posicoes"].index(posicao))
    return (prado["animais"][n])

#Modificadores

def eliminar_animal(prado,posicao):
    
    n = (prado["posicoes"].index(posicao))
    prado["animais"] = prado["animais"][:n] + prado["animais"][n+1:]
    prado["posicoes"] = prado["posicoes"][:n] + prado["posicoes"][n+1:]
    
    return(prado)

def mover_animal(prado,p_inicio,p_fim):
    
    n = (prado["posicoes"].index(p_inicio))
    prado["posicoes"] = prado["posicoes"][:n]+(p_fim,)+prado["posicoes"][n+1:]
    return (prado)

def inserir_animal(prado,animal,posicao):
    
    prado["posicoes"] = prado["posicoes"]+(posicao,)
    prado["animais"] = prado["animais"]+(animal,)
    return(prado)

#Reconhecedores

def eh_prado(univ):
    
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
            if not eh_posicao(elementos):
                return False
            
    for elementos in univ["animais"]:
        if not eh_animal(elementos):
            return False
        
    for elementos in univ["posicoes"]:
        if not eh_posicao(elementos):
            return False
        
    if len(univ["animais"]) != len(univ["posicoes"]):
        return False
    
    return True

def eh_posicao_animal(prado,posicao):
    
    return (posicao in obter_posicao_animais(prado))

def eh_posicao_obstaculo(prado,posicao):
    
    x = obter_posicao_x(posicao)
    y = obter_posicao_y(posicao)
    
    return (x <= 0 or y <= 0 or\
       x >= (obter_tamanho_x(prado)-1) or y >= (obter_tamanho_y(prado)-1) or\
       posicao in prado["obstaculos"])

def eh_posicao_livre(prado,posicao):

    return (posicao not in obter_posicao_animais(prado) and not\
            eh_posicao_obstaculo(prado,posicao))

#Testes

def prados_iguais(prado1,prado2):
    
    return (eh_prado(prado1) and eh_prado(prado2) and prado1==prado2) 

#Transformador

def prado_para_str(prado):
    
    prado_inteiro = ["+"]+["-"]*(obter_tamanho_x(prado)-2)+["+\n"]
    
    for n in range(1,obter_tamanho_y(prado)-1):
        
        prado_linha = ["|"]+["."]*(obter_tamanho_x(prado)-2)+["|\n"]
        
        for elementos in prado["obstaculos"]:
            if obter_posicao_y(elementos) == n:
                prado_linha[obter_posicao_x(elementos)] = "@"
                
        for elementos in obter_posicao_animais(prado):
            if obter_posicao_y(elementos) == n:
                prado_linha[obter_posicao_x(elementos)] =\
                    animal_para_char(obter_animal(prado,elementos))
                
        prado_inteiro += prado_linha
        
    prado_inteiro += ["+"]+["-"]*(obter_tamanho_x(prado)-2)+["+\n"]
    return("".join(prado_inteiro))

#Funções de alto nível associdadas a este TAD

def obter_valor_numerico(prado,posicao):
    
    return(obter_posicao_y(posicao)*(obter_tamanho_x(prado))+\
           obter_posicao_x(posicao))
    
    
def obter_movimento(prado,posicao):

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

    posicoes = ordenar_posicoes(obter_posicao_animais(prado))
    for elementos in posicoes:
        aumenta_idade(obter_animal(prado,elementos))
        if eh_predador(obter_animal(prado,elementos)):
            aumenta_fome(obter_animal(prado,elementos))
            if eh_animal_faminto(obter_animal(prado,elementos)):
                eliminar_animal(prado,elementos)
                continue 
        if eh_animal_fertil(obter_animal(prado,elementos)) and\
          obter_movimento(prado,elementos) != elementos:
            inserir_animal(prado,reproduz_animal\
                           (obter_animal(prado,elementos)),elementos)
        mover_animal(prado,elementos,obter_movimento(prado,elementos))

    return(prado)  

def conta_predadores(prado):
    predadores = 0
    posicoes = obter_posicao_animais(prado)
    for elementos in posicoes:
        if eh_predador(obter_animal(prado,elementos)):
            predadores += 1
    return(predadores)
def conta_presas(prado):
    presas = 0
    posicoes = obter_posicao_animais(prado)
    for elementos in posicoes:
        if eh_presa(obter_animal(prado,elementos)):
            presas += 1
    return(presas)

def simula_ecossistema(ficheiro,inteiro,booleano):
    
    file = open(ficheiro, "r", encoding = "UTF-8")
    limite = eval(file.readline())
    obstaculo = eval(file.readline())
    animais_posicoes = file.readlines()

    prado = cria_prado(limite,obstaculo,(),())
    for elem in animais_posicoes:
        elem = eval(elem)
        inserir_animal(prado,cria_animal(elem[0],elem[1],elem[2]),elem[3])
    file.close()

    print("Predadores: "+str(conta_predadores(prado))+\
          " vs Presas: "+str(conta_presas(prado))+" (Gen. 0)\n"+\
          (prado_para_str(prado)))
    
    if not booleano:
        for n in range(1,inteiro+1):
            geracao(prado)
        return(print("Predadores: "+str(conta_predadores(prado))+\
          " vs Presas: "+str(conta_presas(prado))+" (Gen. "+str(n)+")\n"+\
          (prado_para_str(prado))))
    elif booleano:
        for n in range(1,inteiro+1):
            predadores = (conta_predadores(prado))
            presas = (conta_presas(prado))
            geracao(prado)
            predadores_depois = (conta_predadores(prado))
            presas_depois = (conta_presas(prado))
            if presas != presas_depois or predadores != predadores_depois:
                print("Predadores: "+str(conta_predadores(prado))+\
                      " vs Presas: "+str(conta_presas(prado))+\
                      " (Gen. "+str(n)+")\n"+\
                      (prado_para_str(prado)))  
        return(print("Predadores: "+str(conta_predadores(prado))+\
            " vs Presas: "+str(conta_presas(prado))+\
            " (Gen. "+str(n)+")\n"+(prado_para_str(prado))))            