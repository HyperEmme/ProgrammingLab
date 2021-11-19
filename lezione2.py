def sommaLista(my_list):
    somma = 0
    for i in range(len(my_list)):
        somma = somma + my_list[i]
    return somma

def sottrazioneLista(my_list):
    sottrazione = 0
    for i in range(len(my_list)):
        sottrazione = sottrazione - my_list[i]
    return sottrazione
    
def prodottoLista(my_list):
    prodotto = 1
    for i in range(len(my_list)):
        prodotto = prodotto * my_list[i]
    return prodotto

my_list = [14, 35, 66, 89]
print('La somma è: {}'.format(sommaLista(my_list)))
print('La differenza è: {}'.format(sottrazioneLista(my_list)))
print('Il prodotto è: {}'.format(prodottoLista(my_list)))