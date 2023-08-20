#Jefferson Conceição do Nascimento 202222112

from random import randint 

def geraPontos():
    v1 = randint(1,6)
    v2 = randint(1,6)
    v3 = randint(1,6)

    return v1 + v2 + v3

class Heroi(object):
    def __init__(self,classe):        
        self.nome = ""
        self.classe = classe
        self.forca = geraPontos()
        self.destreza = geraPontos()
        self.constituicao = geraPontos()
        self.inteligencia = geraPontos()
        self.carisma = geraPontos()
        self.vida = 100

    def Ataca(self,inimigo):
        inimigo.Dano(geraPontos())
        print(self.nome, " Atacou ", inimigo.nome,".")
       

    def AtacaEspecial(self,inimigo):
       
        chance = randint(1,5)

        if(chance == 3):
            inimigo.Dano(50)
            print("Parabéns!! você acertou o especial")           
           
        else:            
            print("Infelizmente você errou o especial")

 
    def Reconstituir(self):
        chance = randint(1,6)

        if(chance <= 2):
           self.vida += 0
        elif(chance > 2 and chance <= 5 ):
            self.vida += 2
            print(self.nome, "Restaurou 2 de vida")
        elif(chance == 6):
            self.vida += 4
            print(self.nome, "Restaurou 4 de vida")
        

    def Dano(self,dano):
       
       self.vida -= dano
       print(self.nome, "sofreu", dano, "de dano, resta", self.vida,"de vida.")
       
       if(self.vida <= 0):
           print(self.nome , " Foi eliminado")
           print("***************GAME OVER*****************")

 
    def Mensagem(self):
        return "Nome: %s + Classe: %s + Vida: %i" %(self.nome,self.classe,self.vida)



#chamada do codigo
contBatalha = 1
contBoss = 0
contHeroi = 0

boss = Heroi("Bárbaro")
boss.nome = "Boss"


while True:

    
    print("***Escolha seu herói***")
    print("1 - Bárbaro")
    print("2 - Mágo")
    print("3 - Ladrão")
    print("4 - Elfo")
    print("5 - Clérigo")
    escolha = int(input("Escolha uma Classe: "))

    if(escolha >= 1 and escolha <= 5):        
        break

if escolha == 1:
    heroi = Heroi("Bárbaro")
elif escolha == 2:
    heroi = Heroi("Mágo")
elif escolha == 3:
    heroi = Heroi("Ladrão")
elif escolha == 4:
    heroi = Heroi("Elfo")
elif escolha == 5:
    heroi = Heroi("Clérigo")


nome =input("Digite o Nome do Heroi:")   
heroi.nome = nome

        

while (boss.vida >0 and heroi.vida > 0):
    print("-----------batalha", contBatalha,"-----------")
    contBatalha+=1
    
    atacante = randint(0,1)
    if atacante ==0:
        boss.Ataca(heroi)        
        contBoss+=1

    if(contBoss == 3):
        contBoss = 0
        boss.Reconstituir()
    elif atacante == 1:
        print("Sua vez de atacar!!!")
        print("Escolha sabiamente.")
        print("Vida do Boss:", boss.vida)
        print("Sua Vida:", heroi.vida)
        print("1- Ataque básico")
        print("2- Ataque Especial")
        tipoAtaque = int(input(":"))

        if(tipoAtaque == 1 or tipoAtaque==2):
            if(tipoAtaque == 1 ):
                heroi.Ataca(boss)
                contHeroi+=1
            elif(tipoAtaque == 2):
                heroi.AtacaEspecial(boss)
                contHeroi+=1
        else:
            print("Número inválido, seu ataque foi básico.")
            heroi.Ataca(boss)
            contHeroi+=1

    if(contHeroi == 3):
        contHeroi = 0
        heroi.Reconstituir()

    print("--------------------------------------------")



  


