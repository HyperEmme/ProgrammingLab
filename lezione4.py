
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
        valori.append(elements)
    for i in range(len(valori)):
      print('{}'.format(valori[i]).split(' , '))
    #for i in range(len(valori_prezzo)):
      #print('{}'.format(valori_prezzo[i]))
    #for i in range(len(valori_data)):
      #print('{}'.format(valori_data[i]))
    
    my_file.close()

#valori_prezzo = []
#valori_data = []
valori = []

fileCSV = CSVFile('a')
print('Questo è il nome del file ----> {}'.format(fileCSV.name))
fileCSV.get_data()
