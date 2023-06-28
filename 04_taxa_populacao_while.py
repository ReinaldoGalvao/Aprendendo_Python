"""
Pais A 80000
    3% ano

Pais B 200000    
    1.5% ano
    
    """
    
a = 80000
b = 200000
anos = 0
while a < b:
    a = a + a * (3/100)
    b = b + b * (1.5/100) 
    anos += 1
    
print(anos)