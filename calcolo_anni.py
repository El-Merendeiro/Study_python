annocorrente=int(input("in che anno stai facendo questo test? ▶"))
eta=annocorrente - int(input('in che anno sei nato?▶'))
numero=int(input("qual'e' il tuo numero preferito?"))
y=0 if input("sei maschio o femmina?[m/f]") =='f' else 1
traquantianni=int(input('quanti anni avrai nel...▶'
)) - annocorrente
x=0 if numero % 2 ==0 else 1
import time
ruota = ['|','/','-',"\\"]
for _ in range (20):
    for t in ruota:
        print ('sto calcolando il risultato attendi',t,end='\r', flush=True)
        time.sleep(0.3)
print ("nell'anno",traquantianni + annocorrente,
'avrai esattamente',eta +traquantianni,'anni')
if eta+traquantianni >=80 and y ==1:
    print ('molto probabilmente sarai gia morto')
    if x==1:
        print ('ma molto probabilmente non ti interessa')
    else :
        print ('mi dispiace molto per te')
elif y==0 and eta+traquantianni >=85:
    print ('molto probabilmente sarai gia morto')
    if x==1:
        print ('ma molto probabilmente non ti interessa')
    else :
        print ('mi dispiace molto per te')
else: print ('complimenti probabilmente sarai ancora vivo')
