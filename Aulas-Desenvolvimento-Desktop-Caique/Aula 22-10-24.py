# Atividade (17/10)

# Criar um sistema de classificação de animais vertebrados usando programação orientada a objetos (POO) em Python, representando subdivisões até chegar a classes específicas como Ornitorrinco, 
# Morcego e Baleia.

# Criação das Classes Principais:

# Inicie com a classe geral Animal que conterá características comuns a todos os animais (ex: nome científico).
# Crie subclasses que representem Vertebrados e, a partir daí, vá subdividindo em classes menores (por exemplo, Mamíferos, Répteis, etc.).
# Características Específicas:

# Cada classe deve conter atributos e métodos específicos de cada subdivisão. Por exemplo:
# Mamíferos: método amamentar().
# Aves: método voar().
# Chegue até as classes mais específicas: Ornitorrinco, Morcego e Baleia.
# Atributos e Métodos:

# Atributos como esqueleto, habitat e alimentacao devem ser herdados pelas subclasses.
# Métodos devem ser implementados para ações comuns (ex: seMovimentar()) e específicas (ex: botarOvo() para algumas classes).
class Animal:
    def __init__(self, nome_cientifico, esqueleto, habitat, alimentacao):
        self.nome_cientifico = nome_cientifico
        self.esqueleto = esqueleto
        self.habitat = habitat
        self.alimentacao = alimentacao

    def movimentar(self):
        print(f"{self.nome_cientifico} se remecheu.")

class Vertebrado(Animal):
    def __init__(self, nome_cientifico, esqueleto, habitat, alimentacao):
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)

class Mamifero(Vertebrado):
    def __init__(self, nome_cientifico, esqueleto, habitat, alimentacao):
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)

    def amamentar(self):
        print(f"{self.nome_cientifico} a amamentar.")

class Ave(Vertebrado):
    def __init__(self, nome_cientifico, esqueleto, habitat, alimentacao):
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)

    def voar(self):
        print(f"{self.nome_cientifico} voa voa.")

class Reptil(Vertebrado):
    def __init__(self, nome_cientifico, esqueleto, habitat, alimentacao):
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)

    def botar_ovo(self):
        print(f"{self.nome_cientifico} a botar.")

class Ornitorrinco(Mamifero):
    def __init__(self):
        super().__init__("Ornithorhynchus anatinus", "endossqueleto", "rios e lagos", "insetos e crustáceos")

    def botar_ovo(self):
        print(f"{self.nome_cientifico} mamifero botando ovo???? ueee.")
    
    def mimir(self):
        print(f"{self.nome_cientifico} a mimir")

class Morcego(Mamifero):
    def __init__(self):
        super().__init__("Chiroptera", "endossqueleto", "cavernas e florestas", "frutas e insetos")

    def voar(self):
        print(f"{self.nome_cientifico} a voar.")

    def mimir(self):
        print(f"{self.nome_cientifico} a mimir")

class Baleia(Mamifero):
    def __init__(self):
        super().__init__("Cetacea", "endossqueleto", "oceano", "plâncton e peixes")

    def nadar(self):
        print(f"{self.nome_cientifico} a nadar.")

    def mimir(self):
        print(f"{self.nome_cientifico} a mimir")

ornitorrinco = Ornitorrinco()
morcego = Morcego()
baleia = Baleia()

ornitorrinco.movimentar()
ornitorrinco.amamentar()
ornitorrinco.botar_ovo()
ornitorrinco.mimir()

morcego.movimentar()
morcego.amamentar()
morcego.voar()
morcego.mimir()

baleia.movimentar()
baleia.amamentar()
baleia.nadar()
baleia.mimir()
