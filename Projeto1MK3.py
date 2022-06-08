#1111111111111111111111111111111111111111111111111111111111111111111111111111111

def corrigir_palavra(Texto):
    
    '''
    Função transforma o input num Tuple e atualiza a variável associada ao tuplo
    com um novo tuplo sem as letras que são detetadas como buggy.
    As letras são detetas a partir de uma comparação, se forem a mesma letra, 
    mas forem simbolos diferentes então são detetadas como erros, cada vez que 
    um erro é detetado o n dá reset de modo a percorrer mais uma vez a função
    de modo a verificar se não se criaram novos Bugs.
    Após se atualizar o tupolo por inteiro faz-se a conversão do tuplo para
    uma string.
    '''
      
    Texto = tuple(Texto)
    l = len(Texto)
    n = 0
    while n < len(Texto) - 1:
        
        if str.lower(Texto[n])==str.lower(Texto[n+1]) and Texto[n]!=Texto[n+1]:
            Texto = Texto[:n] + Texto[n+2:]
            n = n - 1   
            
        else: n = n +1

    res = "".join(Texto)   
    
    return(res)


def eh_anagrama(word1,word2):
    
    '''
    Função transforma todos os caracteres em mínusculas e transforma as palavras
    em listas com as letras organizadas alfabéticamente. Se ambas as listas 
    criadas forem iguais retorna True, caso contrário retorna False
    '''
    word1 = str.lower(word1)
    word2 = str.lower(word2)
    word1sorted = sorted(word1)
    word2sorted = sorted(word2)
    
    if (word1sorted == word2sorted and word1 != word2): 
        return True
    else: 
        return False


def corrigir_doc(doc):
    
    '''
    Função executa a função corrigir_palavra e verifica se algum elemento do 
    tuplo dcorrigido contém números e se sim dá raise a ValueError.
    Caso contrário após a executar a primeira função começa por retirar
    todos os anagramas deixando os que são anagramas mas simultaneamente 
    são a mesma palavra.
    '''
    if type(doc) != str:
        raise ValueError ("corrigir_doc: argumento invalido")
    for elementos in doc:
        if str.isalpha(elementos) != True and elementos != " ":
            raise ValueError ("corrigir_doc: argumento invalido")
    
    doc = tuple(str.split(corrigir_palavra(doc)))
    n = 0
    m = 1
    
    while n < len(doc) - 2:
        while m < len(doc):
            if eh_anagrama(doc[n],doc[m]) == False: 
                m = m + 1
            else: doc = doc[:m] + doc[m+1:]
        n = n + 1
        m = 0
    doc = " ".join(doc)
    
    return(doc) 

doc = "Programacao com objetos e bojetos"

corrigir_doc(doc)



#2222222222222222222222222222222222222222222222222222222222222222222222222222222


def obter_posicao(direcao,tecla):
        
    if (direcao == "C") and (tecla > 3): 
        tecla = (tecla - 3)
            
    elif (direcao == "B") and (tecla < 7):
        tecla = (tecla + 3)
            
    elif (direcao == "D") and ((tecla % 3) != 0):
        tecla = (tecla + 1)
            
    elif (direcao == "E") and ((tecla != 1) and (tecla !=4) and (tecla != 7)):
        tecla = (tecla - 1)

    return(tecla)


def obter_digito(movimento,tecla):
    
    movimento = tuple(movimento) 
    l = len(movimento)
    n = 0
    
    while n < l:
        
        tecla = obter_posicao(movimento[n],tecla)
        n = n + 1
        
    return(tecla)

def obter_pin(movimentos):
    
    movimentos_possiveis = ("C","B","E","D")
    l = len(movimentos)
    res = ()
    t = 5
    n = 0
    
    if (type(movimentos) != tuple) or (l > 10) or (l < 4):
        raise ValueError ("obter_pin: argumento invalido")
    for elementos in movimentos:
        if type(elementos) != str:
            raise ValueError ("obter_pin: argumento invalido")    
    m = "".join(movimentos)
    for keyword in m:
        if keyword not in movimentos_possiveis:
            raise ValueError ("obter_pin: argumento invalido")
             
    while n < l:
        res = res+(obter_digito(movimentos[n],t),)
        t = obter_digito(movimentos[n],t)
        n = n + 1
        
    return(res)


#3333333333333333333333333333333333333333333333333333333333333333333333333333333


def eh_entrada(entrada):
    
    if len(entrada) != 3:
        return False    
    
    entrada_0 = tuple(entrada[0])
    entrada_1 = tuple(entrada[1])
    entrada_2 = entrada[2]

    #ENTRADA_0
    
    n = 0
    if (entrada_0[0] == "-") or (entrada_0[len(entrada_0) - 1] == "-"):
        return False
    while n < len(entrada_0):
        
        if (str.lower(entrada_0[n]) != str(entrada_0[n])):
            return False  
        elif (str.isalpha(entrada_0[n]) == False) and (entrada_0[n] != "-"):
            return False 
        elif (entrada_0[n] == "-") and (entrada_0[n+1] == "-"):
            return False
        n = n + 1
        
    #ENTRADA_1
       
    if len(entrada_1) != 7 or entrada_1[0] != "[" or entrada_1[6] != "]" or\
    str(entrada[1]) != str.lower(entrada[1]):
        return False
    for elementos in entrada_1[1:6]: 
        if (str.isalpha(elementos) == False):
            return False
    
#ENTRADA_2
    
    n = 0
    if (type(entrada_2) != tuple) or (len(entrada_2) < 2):
        return False
    for elementos in entrada_2: 
        if type(elementos) != int: 
            return False
        
    #FIM
    
    return True


def validar_cifra(entrada_0,entrada_1):
    
    entrada_0 = tuple([x for x in tuple(entrada_0) if not "-" in x])
    entrada_1 = tuple((entrada_1)[1:6]) 
    dic = {}
    n = 0
    
    for elementos in entrada_1:
        if elementos not in entrada_0:
            return (False)

    for elementos in entrada_0:
        dic.update({elementos:entrada_0.count(elementos)})
    
    for n in range (0,5): 
        
        for elementos in dic.keys():   
            if (dic[entrada_1[n]] < dic[elementos]) or\
               (dic[entrada_1[n]] == dic[elementos] and \
                [entrada_1[n],elementos] != sorted(entrada_1[n]+elementos)):
                return False
        
        dic.pop(entrada_1[n])
               
    return True

def filtrar_bdb(lista):
    
    n = 0
    
    if (type(lista) != list) or (lista == []):
        raise ValueError ("filtrar_bdb: argumento invalido")
    while n < len(lista):
        if validar_cifra(lista[n][0],lista[n][1]) == True:
            lista.remove(lista[n])
        else: n = n + 1
            
    return (lista)


#4444444444444444444444444444444444444444444444444444444444444444444444444444444


def obter_num_seguranca(tuplo):
    
    tuplo = sorted(tuplo)
    l = len(tuplo)
    dif_min = tuplo[1] - tuplo[0]
    n = 0
    
    while n < l-1:
        
        dif = tuplo[n + 1] - tuplo[n]
        if dif < dif_min:
            dif_min = dif
        n = n + 1
        
    return (dif_min)

def decifrar_texto(string,inteiro):
    
    string = list(string)
    l = len(string)
    n = 0
    
    while n < l:
        if string[n] == "-":
            string[n] = " "
        
        elif n % 2 == 0:
            string[n]=chr(((ord(string[n])+inteiro-96)%26)+97)
                
                
        else: 
            string[n]=chr(((ord(string[n])+inteiro-98)%26)+97)
        n = n + 1

    return ("".join(string))

def decifrar_bdb(lista):
    
    res = []
    
    if filtrar_bdb(lista) != lista:
        raise ValueError ("decifrar_bdb: argumento_invalido")
    
    for elementos in lista:

        num_seg = obter_num_seguranca(elementos[2])
        res = res + [decifrar_texto(elementos[0],num_seg)]
        
    return (res)


#5555555555555555555555555555555555555555555555555555555555555555555555555555555


def eh_utilizador(entrada):
    
    keys = ("name","pass","rule")
    rule_keys = ("vals","char")
    
    if type(entrada) != dict or len(entrada) != 3:
        return False
    for elementos in entrada.keys():
        if elementos not in keys:
            return False
    if type(entrada["name"]) != str or len(entrada["name"]) < 1 or\
       type(entrada["pass"]) != str or len(entrada["pass"]) < 1:
        return False
    for elementos in entrada["rule"]:
        if elementos not in rule_keys:
            return False
    if type(entrada["rule"]["vals"]) != tuple or\
       len(entrada["rule"]["vals"]) != 2 or\
       type(entrada["rule"]["vals"][0]) != int or\
       type(entrada["rule"]["vals"][1]) != int or\
       type(entrada["rule"]["char"]) != str or\
       len(entrada["rule"]["char"]) != 1:
        return False

    return True 


def eh_senha_valida(string,dic):
    
    n = 0
    vogais = ("a","e","i","o","u")
    rep_vogais = 0
    
    while n <= len(string) - 1:        
        if string[n] == string[n+1]:
            break
        elif n == len(string) - 2:
            return False
        n = n + 1
    
    for elementos in vogais:
        rep_vogais = rep_vogais + (string.count(elementos))
    if rep_vogais < 3:
        return False
    
    rep_char = string.count(dic["char"])
    if (dic["vals"][0] <= rep_char <= dic["vals"][1]) == False:
        return False
    
    return True
    
def filtrar_senhas(lista):
    
    res = []
    
    if (type(lista) != list) or (lista == []):
        raise ValueError ("filtrar_senhas: argumento invalido")
    
    for elementos in lista:
        if eh_utilizador(elementos) == False:
            raise ValueError ("filtrar_senhas: argumento invalido")
        if eh_senha_valida(elementos["pass"],elementos["rule"]) == False:
            res = [elementos["name"]] + res 
            
            
    return (sorted(res))


tes = ((
                {
                    "name": "bruce.wayne",
                    "pass": "mynameisbatman",
                    "rule": {"vals": (2, 1), "char": "m"},
                }
            )
        )
