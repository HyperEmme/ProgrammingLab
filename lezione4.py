import os

class CSVFile():

  def __init__(self, name):
    self.name=name
  
  def get_data(self):
    my_file = open('shampoo_sales.txt', 'r') 
    
    for line in my_file:
      elements = line.split(',')
      if elements[0] != 'Date':
        #date  = elements[0]
        #value = elements[1]
        #valori_prezzo.append(float(value))
        #valori_data.append(date)
        elements[-1]=elements[-1].strip()
        valori.append(elements)
    for i in range(len(valori)):
      #print('{}'.format(valori[i]).split(' , '))
      print('{}'.format(valori[i]))
    

    
    my_file.close()


valori = []

nome = input('Inserisci il nome che si vuole dare al file: ')
fileCSV = CSVFile(nome)
os.system('cls' if os.name == 'nt' else 'clear')  #parte di codice per cancellare il contenuto della shell. Ricordati che sopra ho importato os tramite: import os. Funzione trovata su internet e funziona 
print('Questo è il nome del file ----> {} \n'.format(fileCSV.name))
fileCSV.get_data()
