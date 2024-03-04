# functii si exceptii

# 1. Creem o metoda care returneaza suma a 2 numere

def suma_2numere(a, b):
    suma = a + b
    return suma


total = suma_2numere(-3, 5)
print(total)

print('-------' * 10)


# 2.Creati o metoda care returneaza rezultatul inmultirii a 3 numere

def inmultire_3numere(a, b, c):
    inmultire = a * b * c
    return inmultire


total = inmultire_3numere(2, 3, 4)
print(total)

#3. Creati un scurt program care sa consulte cuvinte citite de la tastatura in dictionar
dict = {
    "apa": " Lichid incolor, fără gust și fără miros, compus hidrogenat al oxigenului, care formează unul dintre învelișurile Pământului.",
    "pamant": "Scoarța globului terestru, partea de uscat a globului terestru; suprafața lui (împreună cu atmosfera) pe care trăiesc oamenii și alte vietăți.",
    "zebra": "Nume generic dat speciilor de cai sălbatici africani cu blana vărgată cu benzi alternative, deschise și închise; animal care face parte din aceste specii"
}

cuvant = input("introduceti un cuvant:")
try:
    print(dict[cuvant])
except:
    print('Cuvantul nu se gaseste in dictionar')
#print(dict.values())
