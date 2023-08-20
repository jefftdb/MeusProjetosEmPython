#HP = (Base Stam + Stam IV) * Lvl(CPScalar)
#CP = (Base Atk + Atk IV) * (Base Def + Def IV)0.5 * (Base Stam + Stam IV)0.5 * Lvl(CPScalar)2 / 10
#Lvl(CPScalar)= TotalCpMultiplier (~0.095*Sqrt(PokemonLevel)
#https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(GO)


class Pokemon(object):
    def __init__(self,nome,tipo,descricao,atk_base,def_base,energia_base,nivel,atk_IV,def_IV,energia_IV):
        
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.atk_base = atk_base
        self.def_base = def_base
        self.energia_base = energia_base
        self.nivel = nivel        
        self.atk_IV = atk_IV
        self.def_IV = def_IV
        self.energia_IV = energia_IV
        self.CP = int(self.getCP())
        self.HP = int(self.getHP())
        self.ganha  = self.Vantagem()
        self.perde = self.Desvantagem()
        

    def Vantagem(self):
        vantagem = []
        if self.tipo.classe or self.tipo.elemento == "Planta":
            vantagem = ["Terrestre", "Pedra","Água"]
            
        elif self.tipo.classe or self.tipo.elemento == "Veneno":
            vantagem = ["Fada", "Planta"]

        elif self.tipo.classe or self.tipo.elemento == "Dragão":
            vantagem = ["Dragão"]
            
        elif self.tipo.classe or self.tipo.elemento == "Fogo":
            vantagem =  ["Inseto", "Planta", "Gelo"]
            
        elif self.tipo.classe or self.tipo.elemento == "Água":
            vantagem = ["Fogo", "Terrestre","Pedra"]

        return vantagem


    def Desvantagem(self):
        desvantagem = []
        if self.tipo.classe or self.tipo.elemento == "Planta":
            desvantagem = ["Inseto", "Fogo", "Voador", "Gelo","Venenoso"]

            
        elif self.tipo.classe or self.tipo.elemento == "Veneno":
            desvantagem = ["Terrestre", "Psíquico"]

        elif self.tipo.classe or self.tipo.elemento == "Dragão":
            desvantagem = ["Dragão", "Fada", "Gelo","Aço"]
            
        elif self.tipo.classe or self.tipo.elemento == "Fogo":
            desvantagem =  ["Pedra", "Terrestre","Água"]

   
        return desvantagem



    def lvlScalar(self):
        lvlScalar = (0.095*(self.nivel**0.5))

        return lvlScalar

    def getHP(self):
        HP = (self.energia_base + self.energia_IV) * self.lvlScalar()
        return HP

    def getCP(self):
        CP = (self.atk_base + self.atk_IV) * ((self.def_base + self.def_IV)**0.5) * ((self.energia_base + self.energia_IV)**0.5) * self.lvlScalar()*2 /10
        return CP



class Tipo:
    def __init__(self,classe,elemento):
        self.classe = classe
        self.elemento = elemento


tipo_Planta_Veneno = Tipo("Planta","Veneno")       
tipo_Dragao_fogo = Tipo("Dragão","Fogo")
tipo_Agua = Tipo("Água","Água")
charmander = Pokemon('Charmander',tipo_Dragao_fogo,'descricao',116,93,118,40,15,15,15)
bulbasaur = Pokemon('Bulbasaur',tipo_Planta_Veneno,'descricao',118,111,128,40,15,15,15)
squirtle = Pokemon('Squirtle',tipo_Agua,'descricao',94,121,127,40,15,15,15)

print("Nome: ",charmander.nome)
print("HP: ",charmander.HP)
print("CP: ",charmander.CP)
print("Tipo: ",charmander.tipo.classe)
print("Elemento: ",charmander.tipo.elemento)
print("Ganha: ",charmander.ganha)
print("Perde: ",charmander.perde)


'''print(bulbasaur.HP)
print(bulbasaur.CP)
print(bulbasaur.tipo.classe)
print(bulbasaur.tipo.elemento)

print(squirtle.HP)
print(squirtle.CP)
print(squirtle.tipo.classe)
print(squirtle.tipo.elemento)'''



        





        
