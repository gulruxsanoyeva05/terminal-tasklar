from students import find_student
from datetime import date
from group import find_group

def add_baholar():
    group_name = input("Guruh nomi(mavjudligi): ")
    student_name = input("Talaba ismi (mavjudigi): ")

    student = find_student(group_name, student_name)

    if student is None:
        print("Guruh yoki talaba topilmadi")
        return

    today = str(date.today())
    baho= int(input("baho kirit: "))

    for grade in student["baholar"]:
      if grade["date"] == today:
        print("bu kunda avval baho qoyilgan")
    
    
    if baho<1 or baho>100:
        print("baholar 1 dan katta yoi 100 dan kichik bolishi kerak")
        return

    student["baholar"].append({"date":today, "ball":baho})

    print(f"{student["student_name"]}  9ga {baho} baho qoyildi")



def show_baholar():
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
        if not student["baholar"]:
            print("Bu talabaga hali baho qo'yilmagan")

        for baho in student["baholar"]:
            print(f"Sana: {baho['date']}")
            print(f"baho: {baho['ball']}")



def ortacha_baho():
        talaba = find_student()
        
        if talaba is None:
                print("Bunday talaba mavjud emas")
                return
        jami=0
        for baho in talaba["baholar"]:
            jami+=baho["ball"]

        ortacha = jami/len(talaba["baholar"])
        print(f"baho: {ortacha}")


def get_best_student():
    group_name = input("Guruh nomini kiriting: ")
    if not group_name:
            print("Guruh bo'sh bo'lmasligi kerak")
            return
    
    group= find_group(group_name)

    if group is None:
        print("Bu guruh mavjud emas")
        return

    best_student=None
    best_grade=0

    for student in group["students"]:
        jami = 0
        for baho in student["baholar"]:
            jami+=baho["ball"]
 
        if jami>best_grade:
            best_grade=jami
            best_student=student
    print(f"eng yaxshi talaba - {best_student["student_name"]} - {best_grade } bahosi")