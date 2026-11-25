class BankHisobi:
    def init(self, egasi, balansi=0):
        self.egasi =egasi
        self.balansi = balansi

    def str(self):
        return(f"Mijoz: {self.egasi} - {self.balansi}")

    def kirim(self, pul):
        self.balansi+=pul
        print(f"{self.egasi} - {pul} so'm qo'shildi \n  Umumiy balans - {self.balansi}")

    def chiqim(self, pul):
        if self.balansi>pul:
             self.balansi -=pul
             print(f"{self.balansi} - Pul olindi")
        else:
            print("Mablag' yetarli emas")
        
    def balansniKorish(self):
        print(f"{self.egasi} - hisobingizda- {self.balansi} bor")

hisob=BankHisobi("ali", 200000)
hisoblar = []


def add_Mijoz():
    ism = input("Mijoz ismini kiriting: ")
    pul = int(input("Mijoz balansini kiritng: "))
     
    hisob=BankHisobi(ism, pul)
    hisoblar.append(hisob)
    print(f" {ism} - {pul} - qo'shildi")

def show_Mijoz():
    for mijoz in hisoblar:
        print(mijoz)


def kirim():
    for i, mijoz in enumerate(hisoblar, start=1):
        print(f"{i}.{mijoz.egasi}")
    
    ism = input("Pul qo'shadigan mijozni ismini kiriting: ")
        
    for mijoz in hisoblar:
        if ism == mijoz.egasi:
            pul = int(input("kirim summasini kiriting: "))
            mijoz.kirim(pul)


def chiqim():
    for i, mijoz in enumerate(hisoblar, start=1):
        print(f"{i}.{mijoz.egasi}")
    
    ism = input("Pul olinadigan  mijozni ismini kiriting: ")
        
    for mijoz in hisoblar:
        if ism == mijoz.egasi:
            pul = int(input("chiqim summasini kiriting: "))
            mijoz.chiqim(pul)

def umumiy_balans():
    jami=0
    for mijoz in hisoblar:
        jami += mijoz.balansi
        print(jami)

while True:
    print("==================================")
    print("1. Yangi mijoz qo'shish")
    print("2. Mijozni ko'rish")
    print("3. Kirimni qilish")
    print("4. Chiqimni qilish")
    print("5. Umumiy balansni hisoblash")
    print("0. Dasturni tugatish")
    print("===================================")
    tanlov = int(input("Tanlov kiriting: "))

    if tanlov == 1:
        add_Mijoz()

    elif tanlov == 2:
        show_Mijoz()
    elif tanlov == 3:
        kirim()
    elif tanlov == 4:
        chiqim()
    elif tanlov ==5:
        umumiy_balans()
    elif tanlov == 0:
        break
    else:
        print("Noto'g'ri tanlov")