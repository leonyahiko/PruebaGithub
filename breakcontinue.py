import os
os.system ("cls")
#break
print("Instrucción con el break")
i=0
while i < 6 :
    i+=1
    if i==3:
        break
    print("Dentro del ciclo ", i)
print("Fuera del ciclo")
print("")
#continue
print("Instrucción con el continue")
i=0
while i < 6 :
    i+=1
    if i==3:
        continue
    print("Dentro del ciclo " , i)
print("Fuera del ciclo")
