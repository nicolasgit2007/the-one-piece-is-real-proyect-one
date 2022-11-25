def main_numeros_random():
    import random 
    num = random.randint(0,100)
    while True:
    	numero = int(input())
    	if numero==num:
    		print("es correcto")
    	if numero>num:
    		print("es mayor")
    	if numero<num:
    		print("es menor")