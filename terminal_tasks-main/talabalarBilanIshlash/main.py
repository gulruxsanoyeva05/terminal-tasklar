from group import add_group, show_groups
from students import add_students, show_students, search_students
from davomat import add_davomat, show_davomat
from baholar import add_baholar,get_best_student
from reports import group_report



def report_menu():
       print(" \n======= HISOBOTLAR =======")
       print("1. Umumiy guruh hisoboti ")
       print("1. Umumiy guruh hisoboti")
       print("2. Davomat hisoboti")
       print("3. O'zlashtirish hisoboti")
       print("0. Orqaga")
    
       tanlov = int(input("Tanlovingizni kiriting: "))
       if  tanlov == 1 :
           group_report()

        # if tanlov == 2 :
           
           



def main():
    while True:
        print("\n" + "=" * 40)
        print("       UNIVERSITET BOSHQARUV TIZIMI")
        print("=" * 40)

        print("1. Guruh qo'shish")
        print("2. Guruhlarni ko'rish")
        print("3. Talaba qo'shish")
        print("4. Talabalarni ko'rish")
        print("5. Talabani qidirish")
        print("6. Davomat belgilash")
        print("7. Davomatni ko'rish")
        print("8. Talabaga baho qo'yish")
        print("9. Eng yaxshi talabani aniqlash")
        print("10. Hisobotlar")
        print("0. Dasturni yakunlash")

        choice = input("\nTanlovingizni kiriting: ")

        if choice == "1":
            add_group()

        elif choice == "2":
            show_groups()

        elif choice == "3":
            add_students()

        elif choice == "4":
            show_students()

        elif choice == "5":
            search_students()

        elif choice == "6":
            add_davomat()

        elif choice == "7":
            show_davomat()

        elif choice == "8":
          add_baholar()

        elif choice == "9":
            get_best_student()

        elif choice == "10":
            report_menu()

        elif choice == "0":
            print("Dastur yakunlandi. Xayr!")
            break

        else:
            print("Noto'g'ri tanlov! Qayta urinib ko'ring.")


if __name__ == "__main__":
    main()
