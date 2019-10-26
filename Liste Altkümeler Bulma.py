"""Elemanları ınteger olan bir array içerisinde birbirine komşu
olmayan elemanlarından oluşan alt kümeler oluşturularak bu alt kümeler
arasındaki toplamı en büyük olan alt kümeyi bulunuz"""

def max_kume(liste):
    uzun=len(liste)
    if uzun<3:
        return "Daha Uzun Liste Giriniz"
    else:
        altkumeler=[]        
        for i in range(uzun-2):
            if i in [eleman for eleman in range(uzun-4)]:
                altkumeler.append([liste[w] for w in range(i,uzun,2)])
            for q in range(2,uzun-i):
                altkumeler.append([liste[i],liste[i+q]])
        max_toplam=max([sum(a) for a in altkumeler])
        
        return altkumeler,max_toplam

try:
    girdi=input("Sayıları Aralarında Boşluk Bırakarak Giriniz(En az 3):").split(" ")
    girdi=[int(x) for x in girdi]
    print(max_kume(girdi))
except(Exception):
    print("Hatalı Giriş!!")
    




    
    
