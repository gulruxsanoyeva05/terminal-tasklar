
# talabalar = [
#     ("Ali", 85),
#     ("Husan", 45),
#     ("Zuhra", 92),
#     ("Fotima", 64)
# ]

# def talabalarni_korish(students):
#     if students:
#         for i, (ism, bal) in enumerate(students, start=1):
#             print(f"{i}. {ism} - {bal}")
#     else:
#         print("Talaba mavjud emas!")


# def filter_students():
#     if talabalar:
#         otganlar=list(filter(lambda x:x[1]>=60,talabalar))
#         if otganlar:
#             talabalarni_korish(otganlar)
#         else:
#             print("o'tgan talaba yoq")
#     else: 
#         print("talabalar mavjud emas ")
        
        
# def balarni_oshirish():
#     if talabalar:
#         new_talabalar = list(map(lambda x: (x[0], x[1] + 5), talabalar))
#         talabalarni_korish(new_talabalar)
#     else:
#         print("talaba mavjud emas")
           
 
# def alochi_talabalar():
#     alochi = any(bal >= 90 for ism, bal in talabalar)
#     print("alochi bor" if alochi else "alochi yo'q")


# def xammasi_utgan():    
#     all_passed = all(bal > 50 for ism, bal in talabalar)
#     print("barchasi o'tgan" if all_passed else "barchasi o'tolmagan")
  
# def update_student(index,yangi_nom,yangi_bal):
    
#     yangi_talabalar = []
#     for i, (ism, bal) in enumerate(talabalar):
#         talaba = []
#         if i == index-1:
#            talaba.append(yangi_nom or ism)
#            talaba.append(yangi_bal or bal)
#         else:
#             talaba.append(ism)
#             talaba.append(bal)
#         yangi_talabalar.append(tuple(talaba))
    
#     talabalarni_korish(yangi_talabalar)
    
          
            
# while True:
#     print("<----------------------------------------------------->")
#     print("1. Talaba va uning balini qo'shish")
#     print("2. Barcha talabalarni ko'rish (enumerate va unpacking)")
#     print("3. Imtihondan o'tganlarni filtrlash (filter va lambda) bal>=60")
#     print("4. Ballarni  +5 ga oshirish (map va lambda) yordamida")
#     print("5. Shartlarni tekshirish (any va all yordamida) alochi,yiqilgan talabalarni chiqarish")
#     print("6.Talabani update qilish")
#     print("7.Talaba balini update qilish")
#     print("8.Talaba va balini bir vaqtda update qilish")
#     print("9.talabani delete qilish")
#     print("10. Dasturdan chiqish")
#     print("<----------------------------------------------------->")
#     tanlov = int(input("buyruqni tanla: "))

#     match tanlov:
#         case 1:
#             ism = input("ism kiriting: ")
#             ball = int(input("ball kiriting: "))
#             talaba = (ism, ball)
#             talabalar.append(talaba)
#             print(f"{ism} - {ball} balli talaba qo'shildi")
#         case 2:
#             talabalarni_korish(talabalar)
#         case 3:
#             filter_students()
#         case 4:
#             balarni_oshirish()
#         case 5:
#             alochi_talabalar()
#             xammasi_utgan()
#         case 6:
#             print("ozgartirmoqchi bolgan talabani tanla")
#             talabalarni_korish(talabalar)
#             index = int(input("talabani tanla: "))
#             yangi_nom = input("talaba nomini kirit: ")
#             update_student(index,yangi_nom,None)
#         case 7:
#             print("ozgartirmoqchi bolgan talabani tanla")
#             talabalarni_korish(talabalar)
#             index = int(input("talabani tanla: "))
#             yangi_bal = int(input("talaba nomini kirit: "))
#             update_student(index,None,yangi_bal)
#         case 8:
#             print("ozgartirmoqchi bolgan talabani tanla")
#             talabalarni_korish(talabalar)
#             index = int(input("talabani tanla: "))
#             yangi_nom = input("talaba nomini kirit: ")
#             yangi_bal = int(input("talaba balini kirit: "))
#             update_student(index,yangi_nom,yangi_bal)
#         case 9:
#             print("O'chirmoqchi bo'lgan talabani tanla!")
#             talabalarni_korish(talabalar)
#             index = int(input("Talabani tanla: "))
#             del talabalar[index-1]
#             talabalarni_korish(talabalar)
#         case 10:
#             print("Dasturdan chiqildi!")
#             break
#         case _:
#             print("Xato buyruq kiritildi!")




from datetime import datetime
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def now_text():
    return datetime.now().strftime(DATE_FORMAT)


def parse_time(value):
    if isinstance(value, datetime):
        return value
    if not value:
        return None
    try:
        return datetime.strptime(str(value), DATE_FORMAT)
    except ValueError:
        return None


class Custumer:
    def init(self, id, name, phone, service_type, arrival_type=None, status=None, start_type=None, end_type=None ):
        




class Navbat:
    def init(self):
        self.customers=[]

    def generate_id(self):
        numbers = []
        for customer in self.customers:
            try:
                numbers.append(customer.id) 

            except(ValueError, IndentationError):
               pass
            return f"a{max(numbers, default=0)+1}"

    def add_customers(self):
        name = input("Ism kiriting: ").strip()
        phone = input("telefon raqamingizni kiriting: ").strip()
        service = input("Xizmat turini kiriting: ").strip()

while True:
    print("\n===== SMART QUEUE MANAGEMENT SYSTEM =====")
    print("1. Yangi mijoz qo'shish")
    print("2. Keyingi mijozni chaqirish")
    print("3. Navbatdagi mijozlarni ko'rish")
    print("4. Mijozni navbatdan bekor qilish")
    print("5. Mijozni qidirish")
    print("6. Xizmat ko'rsatish tarixini ko'rish")
    print("7. Statistikani ko'rish")
    print("8. Excel faylga eksport qilish")
    print("0. Chiqish")

    tanlov = int(input("Tanlovingiz: "))

    # if tanlov == 1: