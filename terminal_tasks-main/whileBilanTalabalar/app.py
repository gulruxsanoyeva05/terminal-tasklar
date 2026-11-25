# talaba = []
# bahosi = []
# print("Guruh qatnashchilari ro'yxati")
# while True:
#     print("\nAsosiy menu:")
#     print("1. Talaba va uning balini qo'shish")
#     print("2. Barcha talabalar ro'yxatini ko'rish")
#     print("3. Guruhning o'rtacha balini hisoblash")
#     print("4. Dasturdan chiqish")

#     tanlov = input("1, 2, 3, 4 sonlaridan birini tanlang: ")
#     if tanlov == "1":
#         ism = input("Talaba ismini kiriting: ")
#         bal = int(input("Ballni kiriting: "))
#         talaba.append(ism)
#         bahosi.append(bal)
#         print(f"{ism} - {bal} ro'yxatga qo'shildi!")

#     elif tanlov == "2":
#         if len(talaba) == 0:
#             print("Ro'yxat mavjud emas")
#         else:
#             print("\nTalabalar ro'yxati:")
#             for son, ism in enumerate(talaba):
#                 print(f"{son+1}. {ism} - {bahosi[son]}")

#     elif tanlov == "3":
#         if len(bahosi) > 0:
#             ortacha = sum(bahosi) / len(bahosi)
#             print("Guruhning o'rtacha bali:", round(ortacha, 2))
#         else:
#             print("Hali talabalar qo'shilmagan!")
#     elif tanlov == "4":
#         print("Dasturdan chiqdingiz!")
#         break
#     else:
#         print("1, 2, 3 yoki 4 ni kiriting!")

