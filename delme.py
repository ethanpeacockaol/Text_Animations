import os
import numpy as np

howmany = int(input("how many:"))
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
alphabet += ['1','2','3','4','5','6','7','8','9','0']
alphabet += ['+','=','?','!','~','*']

for i in range(howmany):
	sel = np.random.randint(0,len(alphabet))
	os.system(f"figlet {alphabet[sel]} | lolcat")
