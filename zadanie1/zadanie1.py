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
        self.all_cities_number=0
        self.conn_number=0
        self.max_wage=0
        self.connections=[]
        self.initial_connections=[]
        self.filename='../dane/sets/'+filename
        self.all_cities_number, self.conn_number,self.max_wage,self.connections=self.load_data(self.filename)
        self.all_city_names=set()
        self.connection_net={}
        
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
        self.initial_connections= drogi[:]   
        return miasta,liczba_drog,max_wagi,drogi
    
    def show_data(self):
        print 'all_cities_number:',self.all_cities_number
        print 'conn_number  :',self.conn_number
        print 'max_wage     :',self.max_wage
        print 'connections  :',self.connections 
        print 'all cities   :',list(self.all_city_names)
        print self.all_cities_number, self.conn_number,self.max_wage,self.connections
         
    def get_list_of_all_cities(self):
        for conn_city in self.connections:
          for city in conn_city.split():
            self.all_city_names.add(city)
    
    def get_neigbours_for_city(self,city_name):
        direct_connections=[]
        for conn_city in self.connections:
            if city_name in conn_city.split():
                direct_connections.append\
                (conn_city.replace(city_name,'').strip())
        return direct_connections         
    
    def get_all_direct_connections_for_cities(self):
        for city in self.all_city_names:
            print city,self.get_neigbours_for_city(city)
    
    def _check_connecton(self,city_a,city_b,liczba_prob):
        if self.connected==True:
            return
        if liczba_prob>10:
            return False
        liczba_prob+=1
#         print 'liczba_zaglebin={}'.format(liczba_prob)
        if city_b in self.get_neigbours_for_city(city_a):
#             print 'podlaczone bezposrednio !!'
            self.connected=True
            return
        else:
            for neighbour_city in self.get_neigbours_for_city(city_a):
#                 print 'miasto {}:sasiad {},zaglebienie {}'.format(
#                                                                   city_a,
#                                                                   neighbour_city,
#                                                                   liczba_prob)
                self._check_connecton(neighbour_city,city_b,liczba_prob)
            
    def check_city_connection(self,miastoA,miastoB):
        self.connected=False
#         print 'checking connection from {} to {}'.format(miastoA,
#                                                       miastoB) 
        liczba_prob=0
        a=self._check_connecton(miastoA,miastoB,liczba_prob)
        return self.connected
    
    def check_connection_in_aglomeration(self):
        for city in self.all_city_names:
            all_except_this=self.all_city_names-set(city)
            print '###'*20
            print 'creating conn dict', city,list(all_except_this)
            conn_dict={}
            for other_city in list(all_except_this):
                print 'connected:',self.check_city_connection(city,other_city)
                conn_dict[other_city]=self.check_city_connection(city,other_city)
            self.connection_net[city]=  conn_dict  
        print 'self.connection_net',self.connection_net      
 
    def restore_all_connections(self):
        '''removal of connection'''
        self.connections=self.initial_connections
        print 'restoring connections to initial ones :,',self.initial_connections
    
    def remove_a_connection(self,connection2remove):
        '''removal of connection'''
        print 'connection2remove ,',connection2remove
        i=0
        for element in self.connections:
            if element ==connection2remove:
                print "removing:,", i
                del self.connections[i]
            i+=1
        self.show_all_connections()
        
    def show_all_connections(self):    
        print '{} all connections: {}'.format(len(self.connections),
                                      self.connections)
    def measure_flooded(self):
        number_of_unpaired=0
        for city,other_connection in self.connection_net.items() :
            for connection_result in other_connection.values():
                if connection_result==False:
                    number_of_unpaired+=1
        print 'Total number of flooded cities : {}'.format(number_of_unpaired)            
        return number_of_unpaired     
        
if __name__=='__main__':
    print get_B32_cityname(701)     
    print get_dec_from_B32('FQ')     
    print 'welcome in main '
    zadanie1=B32_aglomeration('flood00.in')
    zadanie1.show_data()
    zadanie1.get_list_of_all_cities()
    #############################################
#     zadanie1.restore_all_connections()
#     zadanie1.check_connection_in_aglomeration()
#     zadanie1.measure_flooded()
#     zadanie1.show_all_connections()
    #############################################
    zadanie1.remove_a_connection('b c')
    zadanie1.check_connection_in_aglomeration()
    zadanie1.measure_flooded()
    zadanie1.show_all_connections()
    
    
    
    