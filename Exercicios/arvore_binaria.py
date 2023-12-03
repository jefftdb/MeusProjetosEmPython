def Desenvolvedores():
      devs = ['Jefferson Conceição do Nascimento','Adriano Corrêa e Castro']

      return devs

def Menu_principal():
    print('------------Menu principal-------------------------')
    print('1 - Incluir nó: ')
    print('2 - Excluir nó: ')
    print('3 - Consultar nó: ')
    print('4 - Maior nó: ')
    print('5 - Menor nó: ')
    print('6 - Imprimir árvore: ')
    print('7 - Gravar árvore em disco: ')
    print('8 - Desenvolvedores: ')
    print('9 - Abandonar programa: ')
    print('---------------------------------------------------')

class No:
    def __init__(self, chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        
    def __repr__(self):
        return "%s <- %s -> %s" % (self.esquerda and self.esquerda.chave, 
                             self.chave, 
                             self.direita and self.direita.chave) 

def visita_ordem(raiz):
    # ponto de parada da função
    if not raiz:
        return
    
    # Visita, primeiramente, o nó-filho da esquerda
    visita_ordem(raiz.esquerda)  
    # Visita o nó corrente (pai ou raiz)
    print(raiz.chave)
    # Visita, por último, o nó-filho da direita
    visita_ordem(raiz.direita)

def insere(raiz, no):
    # o nó deve ser inserido na raiz
    if raiz is None:
        raiz = no
    # Caso o valor do nó tenha que ser armazenado na direita
    elif raiz.chave < no.chave:
        if raiz.direita is None:
            raiz.direita = no
        else:
            insere(raiz.direita, no)     
    # Caso o valor do nó tenha que ser armazenado na esquerda
    else:
        if raiz.esquerda is None:
            raiz.esquerda = no
        else:
            insere(raiz.esquerda, no)

def busca(raiz, chave):
    """Procurar a chave especificada na árvore"""    
    #Caso a chave não exista
    if raiz is None:
        return None
    
    #Caso encontre a chave
    if raiz.chave == chave:
        return raiz
    
    # A chave procurada é maior do que a raiz
    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    # A chave procurada é menor do que a raiz
    return busca(raiz.esquerda, chave)

# Encontrar o menor valor em uma Árvore binária de busca (BST)
def menor(raiz):
    no = raiz
    while no.esquerda is not None:
        no = no.esquerda
    return no.chave

def maior(raiz):
    no = raiz
    while no.direita is not None:
        no = no.direita
    return no.chave

def remove(raiz, chave):
    if raiz is None:
        return raiz
    
    
    if chave < raiz.chave:
        raiz.esquerda = remove(raiz.esquerda, chave)
    
    elif chave > raiz.chave:
        raiz.direita = remove(raiz.direita, chave)
    
    
    else:
    
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
            temp = raiz.esquerda
            raiz = None
            return temp
        
        
        temp = menor(raiz.direita)
        
        
        raiz.chave = temp
        
        
        raiz.direita = remove(raiz.direita, temp)
    
    return raiz


def serializar_arvore(raiz, arquivo):
    if raiz is None:
        arquivo.write("None\n")
    else:
        arquivo.write(str(raiz.chave) + "\n")
        serializar_arvore(raiz.esquerda, arquivo)
        serializar_arvore(raiz.direita, arquivo)


raiz = None
permanecer = 'S'

while True:  
    Menu_principal()
    menuPrincipal = int(input('Escolha uma opção: '))        

    if(menuPrincipal == 1):
        while True:
                    
            no = int(input('Insira um nó: '))
            if raiz is None:
                raiz = No(no)
            else:
                insere(raiz,No(no))
          
            permanecer = input('Deseja inserir outro nó? S [Sim] ou N [Não]: ') 
            if permanecer.upper() != 'S':
                break
            
    
    elif(menuPrincipal == 2):
        while True:
                    
            no = int(input('Digite o nó a ser excluído: '))
            raiz = remove(raiz, no)

            permanecer = input('Deseja excluir outro nó? S [Sim] ou N [Não]: ')
            if permanecer.upper() != 'S':
                break

    elif(menuPrincipal == 3):
        while True:
                    
            no = int(input('Digite o nó a ser consultado: '))

            result = busca(raiz, no) 
            if result:
                 print("Busca pelo valor {}: Sucesso!!!".format(result)) 
            else:
                 print("Busca pelo valor {}: Falhou!!!".format(No(no)))

            permanecer = input('Deseja consultar outro nó? S [Sim] ou N [Não]: ')
            if permanecer.upper() != 'S':
                break

    elif(menuPrincipal == 4):
        while True:
                    
            print(maior(raiz))
            permanecer = input('Deseja exibir novamente? S [Sim] ou N [Não]: ')
            if permanecer.upper() != 'S':
                break

    elif(menuPrincipal == 5):
        while True:
                    
            print(menor(raiz))
            permanecer = input('Deseja exibir novamente? S [Sim] ou N [Não]: ')
            if permanecer.upper() != 'S':
                break

    elif(menuPrincipal == 6):
        while True:
                    
            visita_ordem(raiz)
            permanecer = input('Deseja exibir novamente?? S [Sim] ou N [Não]: ')
            if permanecer.upper() != 'S':
                break

    elif(menuPrincipal == 7):
        while True:
                    
            with open("arvore.txt", "w") as file:
                serializar_arvore(raiz, file)

            permanecer = input('Deseja Salvar novamente? S [Sim] ou N [Não]: ')
            if permanecer.upper() != 'S':
                break

    elif(menuPrincipal == 8):
        while True:
            devs = Desenvolvedores()
            for dev in devs:
                    print(dev)
            permanecer = input('Exibir novamente? S [Sim] ou N [Não]: ')
            if permanecer.upper() != 'S':
                break                   

                


    elif(menuPrincipal == 9):
        print('Programa finalizado!!')
        break