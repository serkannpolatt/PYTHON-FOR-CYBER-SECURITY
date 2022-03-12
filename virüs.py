import random

for i in range(5):
    açılcacak_dosya=open("sil"+str(i)+".txt","w")
    for i in range(50):
        açılcacak_dosya.write(str(random.randint(14241243124124142,124125123521351)))