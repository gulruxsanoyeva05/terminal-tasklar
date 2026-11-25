from group import GROUPS ,find_group
from davomat import calculate_attendance
from baholar import ortacha_baho


def group_report():
    group_name = input("Guruh nomini kirit: ")

    group = find_group(group_name)

    if group is None:
        print("Bunday guruh yo'q!")
        return

    print(f"Guruh - {group['name']}")

    for index, student in enumerate(group["students"], start=1):
        print(f"{index}. {student['student_name']}")
        davomatni_foizi = calculate_attendance(student)
        print(f"Talaba davomati: {davomatni_foizi}")
        ortacha = ortacha_baho(student)
        print(f"Talaba o'rtacha bahosi: {ortacha}")
