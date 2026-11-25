from datetime import date
from group import find_group, GROUPS
from students import search_students

def add_davomat():
    group_name= input("guruh nomini kiriting : ")
    if not group_name:
        print("guruh nomi bo'sh bo'lmasligi kerak")
        return

    group = find_group(group_name)
    if group is None:
        print("bunday gruruh mavjud emas")
        return

    student_name=input("talaba ismini kiriting: ")
    topilgan_talaba = None

    for student in group["students"]:
        if student_name in student["student_name"].lower():
            topilgan_talaba =student
            today = str(date.today())
            print("\n1.keldi")
            print("2. kelmadi")

            tanlov= int(input("davomatni talang: "))

            status=None

            if tanlov == 1:
                status="keldi"
            elif tanlov == 2:
                status="kelmadi"
            else:
                print("Noto'g'ri tanlov")

            topilgan_talaba["davomat"].append({"date":today, "status":status})

            for davomat in topilgan_talaba["davomat"]:
                if not davomat:
                    print("talaba yoq")

                else:
                    print(f"{davomat['date']}, holati-{davomat['status']}")



def show_davomat():
    guruh_nomi = input("Guruh nomini kiritng: ")
    if not guruh_nomi:
        print("Guruh bo'sh bo'lmasligi kerak")
        return
    group = find_group(guruh_nomi)

    if group is None:
        print("Bunday guruh mavjud emas")
        return

    if not group["students"]:
        print("Bu guruhda talabalar mavjud emas")
        return
    for student in group["students"]:
        print(f"\nTalaba: {student['student_name']}")
        if not student["davomat"]:
            print("Bu talabaga hali davomat kiritilmagan")

        for davomat in student["davomat"]:
            print(f"Sana: {davomat['date']}")
            print(f"Holati: {davomat['status']}")
            



def calculate_attendance(student):
    student= search_students()

    if student is None:
        print("Bunday talaba yo'q")

    # if not student["davomat"]:
    #     print ("Talabada davomat yo'q")

    count=0

    for davomat in student["davomat"]:
        if davomat["status"] == "keldi":
                    count += 1
        davomat_foizi = round(count/len(student["davomat"]) *100, 2)
        print(f"davomat_foizi - {davomat_foizi}")
        