import random

for i in range(5):
    acilacak_dosya = open(f"sil{i}.txt", "w")
    for j in range(50):
        acilacak_dosya.write(str(random.randint(14241243124124142, 124125123521351)))
    acilacak_dosya.close()
