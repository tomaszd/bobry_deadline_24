import sys
sys.path.append("..")
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


def get_B32_city_name(decimal):
    B32number=[]
    _Decimal_2_B32(B32number,decimal)
    converted=[dec_2_B32[i]for i in B32number]
    
    return ''.join(converted[::-1])
    
    
    
    
    
print get_B32_city_name(700)     
    
