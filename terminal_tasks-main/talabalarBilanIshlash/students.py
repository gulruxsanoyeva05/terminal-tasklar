from group import  find_group,  GROUPS

def add_students():
    group_name=input("guruh nomini kiriting(mavjudligi): ")
    group=find_group(group_name)

    if  group is None:
        print("bunday guruh mavjud emas")
        return
    
    name=input("Talaba nomini kiriting (add): ").strip()

    if not name:
        print("ism b'sh bo'lishi mumkin emas")
        return
  
  
    for student in group["students"]:
         if student["student_name"].lower()==name.lower():
              print ("talaba yoq")
              return

    group["students"].append({
             "student_name":name,
             "davomat":[],
             "baholar":[]
         })
    print(f"{name} - nomli talaba {group['name']} guruhga qo'shildi ")
    


def show_students():

    group_name=input("guruh nomini kiriting(mavjudligi): ")
    group=find_group(group_name)
    
    if  group is None:
        print("bunday guruh mavjud emas")
        return
      
    for student in group["students"]:
              print(f"Talaba - {student['student_name']}")
              print(f"Talaba davomadi - {student['davomat']}")
              print(f"Talaba baholar - {student['baholar']}")



def search_students():
    name = input("Talaba nomini qidirish: ").lower().strip()

    if not name:
        print("Talaba nomi bo'sh bo'lmasligi kerak")
        return
    for group in GROUPS:
        for student in group["students"]:
            if name in student["student_name"].lower():
                print(f"Talaba: {student['student_name']}")
                print(f"Guruh: {group['name']}")
                print(f"Davomad: {len(student['davomat'])}")
                print(f"Baholar: {len(student['baholar'])}")

    # print("Talaba topilmadi")


def find_student(group_name, student_name):
    name = input("Talaba nomini qidirish: ").lower().strip()
   
    if not name:
           print("Talaba nomi bo'sh bo'lmasligi kerak")
           return
    for group in GROUPS:
           for student in group["students"]:
               if name in student["student_name"].lower():
                   return student