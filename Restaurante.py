class Restaurante:
    def __int__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False 


    def __str__(self):
        return f'{self.nome} | {self.categoria}'


restaurante_praca = Restaurante('Praca','Gourmat')
restaurante_pizza = Restaurante('Pizza','Italiana')

restaurante =[restaurante_pizza,restaurante_praca]

print(restaurante_praca)
print(restaurante_pizza)


