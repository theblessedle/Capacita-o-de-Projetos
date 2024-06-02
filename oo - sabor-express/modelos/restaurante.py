class Restaurante:   #classificando oq é restaurante
    nome = ''
    categoria = ''        #atributos/caracteristicas
    ativo = False

restaurante_praca = Restaurante()   #variáveis --- criou objetos
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'


restaurante_pizza = Restaurante()  #restaurantes cadastrados

restaurantes = [restaurante_praca,restaurante_pizza]  #lista

#print(dir(restaurante_praca))    #mostrando objetos da classe restaurantes
                                     # dir: show atributes of an object


#print(vars(restaurante_praca))    #vars: dicionario de atributos 


print(restaurante_praca.ativo)  #aparece então o atvio False