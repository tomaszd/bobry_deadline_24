import sys
sys.path.append("..")
sys.path.append("../dane/sets/")
import common

'''tutaj leci kod''' 

"""wczytane dane = common.load_data('cos')"""

B32_2_dec={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,
     'k':8,'l':9,'m':10,'n':11,'p':12,'q':13,'r':14,
     's':15,'A':16,'B':17,'C':18,'D':19,'E':20,'F':21,
     'G':22,'H':23,'K':24,'L':25,'M':26,'N':27,'P':28,
     'Q':29,'R':30,'S':31
     }

dec_2_B32= dict (zip(B32_2_dec.values(),B32_2_dec.keys()))

def _Decimal_2_B32(array,decimal):
    array.append(decimal%32)
    div=decimal/32
    if div==0:
        return
    _Decimal_2_B32(array,div)


def get_B32_cityname(decimal):
    B32number=[]
    _Decimal_2_B32(B32number,decimal)
    converted=[dec_2_B32[i]for i in B32number]
    
    return ''.join(converted[::-1])
    
def get_dec_from_B32(B32_number):
    power=0
    total=0
    for letter in B32_number[::-1]:
        total+= B32_2_dec[letter]*(32**power)
        power+=1
    return total
    


class B32_aglomeration():
    
    def __init__(self,filename='flood00.in'):
        print 'welcome in B32_planet'
        self.cities_number=0
        self.conn_number=0
        self.max_wage=0
        self.connections=[]
        self.filename='../dane/sets/'+filename
        self.cities_number, self.conn_number,self.max_wage,self.connections=self.load_data(self.filename)
        self.all_city_names=set()
        
        
    def load_data(self,filename):
        '''file to load data'''
        with open(filename, 'r') as f: #open the file
            contents = f.readlines() #put the lines to a variable.
        for i in contents:
             i.replace('\n','')
        miasta,liczba_drog,max_wagi=contents[0].split()   
        drogi=[]
        for i in contents[1:]:
            drogi.append(i.replace('\n',''))   
        return miasta,liczba_drog,max_wagi,drogi
    
    def show_data(self):
        print 'cities_number:',self.cities_number
        print 'conn_number  :',self.conn_number
        print 'max_wage     :',self.max_wage
        print 'connections  :',self.connections 
        print 'all cities   :',list(self.all_city_names)
        print self.cities_number, self.conn_number,self.max_wage,self.connections
         
    def get_list_of_all_cities(self):
        for conn_city in self.connections:
          for city in conn_city.split():
            self.all_city_names.add(city)
        
        
if __name__=='__main__':
    print get_B32_cityname(701)     
    print get_dec_from_B32('FQ')     
    print 'welcome in main '
    zadanie1=B32_aglomeration('flood00.in')
    zadanie1.show_data()
    zadanie1.get_list_of_all_cities()
    zadanie1.show_data()


