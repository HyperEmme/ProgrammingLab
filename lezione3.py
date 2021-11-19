def sommaElementiFile(lista_valori):
    somma = 0
    for item in lista_valori:
        somma=somma+item
    return somma

# Inizializzo una lista vuota per salvare i valori
lista_valori = []
# Apro e leggo il file, linea per linea
my_file = open('shampoo_sales.txt', 'r') 
for line in my_file:
# Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
# Se NON sto processando l’intestazione...
    if elements[0] != 'Date':
        # Setto la data e il valore
        date  = elements[0]
        value = elements[1]
        # Aggiungo alla lista dei valori questo valore
        lista_valori.append(float(value))
print('La somma è: {}'.format(sommaElementiFile(lista_valori)))
my_file.close()