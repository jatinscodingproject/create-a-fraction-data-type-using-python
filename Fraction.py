class Fraction:
    def __init__(self,nem,dem):
        self.num = nem
        self.den = dem
        
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __sub__(self,other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __truediv__(self,other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        return '{}/{}'.format(new_num,new_den)
    
    def convert_to_decimal(self):
        return self.num/self.den
    
    
fr1 = Fraction(2,3)
fr2 = Fraction(4,5)
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)