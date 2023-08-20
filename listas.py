def menuPrincipal():   


    while True:
        print('*****************************')
        print('** Algoritmos de Ordenação **')
        print('*****************************')

        print('1 - Selection Sort')
        print('2 - Insert Sort')
        print('3 - Bobble Sort')
        print('4 - Sair')
        escolha = input("Digite sua escolha:")
    
        if escolha == '1':
            Selection_Sort()
        
        elif escolha == '2':
            Insert_Sort()
        
        elif escolha == '3':
            Bobble_Sort()

        elif escolha == '4':
        
            break
    
        else:
            menuPrincipal()

def Selection_Sort():

    while True:
        print('********************')
        print('** Selection Sort **')
        print('********************')

        print('1 - Gerar lista valores')
        print('2 - Executar algoritmo')
        print('3 - Listar conteúdo')
        print('4 - Voltar para o menu anterior')
        
        escolha = input("Digite sua escolha:")
        
        if escolha == '1':
            A= []
            numero = None
            
            while numero != 'Sair':
            
                numero =input('Digite um número ou Sair: ')
                if numero != 'Sair':
                    A.append(numero)
             
            
        
        elif escolha == '2':            
            n = len(A)
            # Percorre o arranjo A.
            for i in range(n):
            # Encontra o elemento mínimo em A.
                minimo = i
                for j in range(i + 1, n):
                    if A[minimo] > A[j]:
                        minimo = j
                        print(A)
                # Coloca o elemento mínimo na posição correta.
                        A[i], A[minimo] = A[minimo], A[i]
        
        elif escolha == '3':
            print(A)

        elif escolha == '4':
            break
            menuPrincipal()
            

def Insert_Sort():
    
    while True:
        print('********************')
        print('** Insert Sort **')
        print('********************')

        print('1 - Gerar lista valores')
        print('2 - Executar algoritmo')
        print('3 - Listar conteúdo')
        print('4 - Voltar para o menu anterior')
        
        escolha = input("Digite sua escolha:")
        
        if escolha == '1':
            A= []
            numero = None
            
            while numero != 'Sair':
            
                numero =input('Digite um número ou Sair: ')
                if numero != 'Sair':
                    A.append(numero)
             
            
        
        elif escolha == '2':
                n = len(A)
                # Percorre o arranjo A.
                for j in range(1, n):
                    chave = A[j]
                    i = j - 1
                    # Insere o elemento A[j] na posição correta.
                    while i >= 0 and A[i] > chave:
                        A[i + 1] = A[i]
                        i = i - 1
                    A[i + 1] = chave
                    print(A)

        
        elif escolha == '3':
            print(A)

        elif escolha == '4':
            break
            menuPrincipal()
            

    
def Bobble_Sort():
        
    while True:
        print('********************')
        print('** Bobble Sort **')
        print('********************')

        print('1 - Gerar lista valores')
        print('2 - Executar algoritmo')
        print('3 - Listar conteúdo')
        print('4 - Voltar para o menu anterior')
        
        escolha = input("Digite sua escolha:")
        
        if escolha == '1':
            A= []
            numero = None
            
            while numero != 'Sair':
            
                numero =input('Digite um número ou Sair: ')
                if numero != 'Sair':
                    A.append(numero)
             
            
        
        elif escolha == '2':
                n = len(A)
                
                for i in range(n):
                    for j in range (0,len(A)-1):  
                        if (A[j]>A[j+1]):
                            temp = A[j]  
                            A[j] = A[j+1]  
                            A[j+1] = temp
                            print(A)

        
        elif escolha == '3':
            print(A)

        elif escolha == '4':
            break
            menuPrincipal()


menuPrincipal()
