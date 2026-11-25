# Print bilan chiqarish
# vazifa1
# print("Sanoyeva")
# print("Gulrux")
# print("3-kurs ATT talabasi")

# vazifa-2
# print("2024", "09", "30", sep="-" )

# vazifa-3
# print("*" * 24)
# print("*\t\t \t*")
# print("*\t\t\t*")
# print("*\t\t\t*")
# print("*\t MENYU\t\t*")
# print("*\t\t\t*")
# print("*\t\t\t*")
# print("*\t\t\t*")
# print("*" * 24)

# vazifa-4
# print("Yuklanmoqda", end="" )
# print("...", end="")
# print("Tayyor!")

# vazifa-5
# print("Ism \tBall \nAli\t95 \nVali\t87" )

# vazifa6
# print("*\n*\t*\n*\t*\t*\n*\t*\t*\t*")


# Arifmetik amallar
# vazifa-1
# a= int(input("Kavdratni a tomonini kiritng:"))
# p=4*a
# s=a*2
# print("perimetri:",p)
# print("yuzasi:", s)

# vazifa-2
# a= int(input("to'g'ri to'rtburchak a tomonini kiritng:"))
# b= int(input("to'g'ri to'rtburchak b tomonini kiritng:"))
# p=2*(a+b)
# s=a*b
# print("perimetri:",p)
# print("yuzasi:", s)

# vazifa-3
# olma=17
# kishi=5
# bolish =olma // kishi
# qoldiq =olma%kishi
# print(bolish ,"tadan")
# print(qoldiq, "ta qoldi")

# vazifa-4
# r= int(input("doira radiusini kiritng:"))
# p=3.14
# s=p*r**2
# print("yuzasi",s)

# vazufa-5
# c= int(input("celsiy bo'yicha haroratni kiritng:"))
# F=c-9/5+32
# print(F)

# vazifa-6
# kun=365
# soat=kun*24
# daqiqa=soat*60
# soniya=daqiqa*60
# print("soat", soat)
# print("daqiqa", daqiqa)
# print("soniya", soniya)

# vazifa-7
# a= int(input("3xonali son kiritng:"))
# yuzlar=a//100
# onlar=a//10%10
# birlar=a%10
# print("yuzlar", yuzlar)
# print("onlar", onlar)
# print("birlar", birlar)

# vazifa-8
# non= int(input("non sonini kiritng:"))
# sut= int(input("sut litrini kiritng:"))
# pul= int(input("pulni kiritng:"))
# jaminon=non*4000
# jamisut=sut*12000
# qaytim=pul-(jaminon+jamisut)
# print(qaytim)

# vazifa-9
# maosh= int(input("oylik maoshni kiritng:"))
# yigish=maosh%15
# print(yigish)

# vazifa-10
# soniya=int(input("soniyani kiriting:"))
# soat=soniya/3600
# daqiqa=soniya/60
# minut=soniya/60
# print(soat,"soat")
# print(daqiqa,"daqiqa")
# print(minut,"minut")

# -----------3-modul---------
# vazifa-1
# ism=input("ismni kiriting:")
# yosh=int(input("yoshni kiriting:"))
# shahar=input("shahar kiriting:")
# print(ism, yosh, shahar)

# vazifa-2
# balans=int(input("balansni kiriting:"))
# xarid=int(input("xarid summa kiriting:"))
# tushum=int(input("tushumni kiriting:"))
# komunal=int(input("komunal tolovni kiriting:"))
# jami=(balans-(xarid+komunal))+tushum
# print(jami)

# vazifa-3

# a = 5
# b = 7
# c = 9
# a, b, c = c, a, b
# print("a =", a)
# print("b =", b)
# print("c =", c)

# a=int(input("a ni kiriting:"))
# b=int(input("b ni kiriting:"))
# c=int(input("c ni kiriting:"))
# perimetri=a+b+c
# yarim_perimetri=perimetri//2
# print("perimetri", perimetri)
# print("yarim_perimetri",yarim_perimetri)

# ----------------Tarmoqlanuvchi algoritmlar-----------
# vazifa-1
# n=int(input("n sonni kiriting:"))
# if n > 0 :
#     print("musbat")
# else:
#     print("manfiy")

# vazifa-2
# a=int(input("a sonni kiriting:"))
# b=int(input("b sonni kiriting:"))
# if a>b:
#     print("a son katta")
# else:
#     print("b son katta")    

# vazifa-3
# n=int(input("n sonni kiriting:"))
# if n%5:
#     print("bolinadi")
# else:
#     print("bo'linmaydi")

# vazifa-4
# x=int(input("x sonni kiriting:"))
# if x<0 :
#     x=-x
#     print(x)
# else:
#     print(x)    

# vazifa-5
# ball=int(input(" balni kiriting:"))
# if ball>60:
#     print("o'tdi")
# else:
#     print("yiqildi")

# vazifa-6
# summa = int(input("Summani kiriting: "))
# if summa > 100000:
#     summa = summa * 10 / 100
#     print(summa)
# else:
#     print(summa)

# vazifa-6
# a = int(input("a sonni kiriting: "))
# b = int(input("b sonni kiriting: "))
# c = int(input("c sonni kiriting: "))
# if a < b and a < c:
#     print("Eng kichigi:", a)
# elif b < a and b < c:
#     print("Eng kichigi:", b)
# else:
#     print("Eng kichigi:", c)

# vazifa-7
# km=int(input("km ni kiriting: "))

# if km<= 3:
#     summa=10000
#     print(summa)
# else:
#     summa=10000+(km - 3)*2500
#     print( summa, "so'm")

# s1 vazifa
# sum=0
# for i in range (1, 11) :
#     print(i, end=",")
   
#s2 vazifa  
# n=int(input("n ni kiriting: "))
# faktorial = 1
# for i in range(1, n+1):
#     faktorial = faktorial * i
#     print(faktorial)

# s3 vazifa
# n=int(input("n ni kiriting: "))
# for i in range(1, 11):
#     print(n, "*", i, "=", n * i)

# s4 vazifa
# dan=int(input("dan ni kiriting: "))
# gacha=int(input("gacha ni kiriting: "))
# yigindi = 0
# for i in range(dan, gacha):
#     if i % 2 == 0:
#         yigindi += i
# print( yigindi)


#  t8
# telefon=None
# print("telefon mavjud emas", telefon)
# telefon="123456789"
# print(telefon)

# t9
# a=True
# b=False
# c=False
# d=True
# f=True

# true_soni=a + b + c + d + f
# false_soni=5 - true_soni

# print("True:", true_soni)
# print("False:", false_soni)

# 10
# shahar="samarqand"
# nom= shahar+"  shahar"
# print(len(nom) , *nom ,sep="=",)

# 9
# kitob=350
# kunlik=24
# print(kitob+kunlik-1//kunlik)

# 10
# hozir=22
# n=int(input("soatni kiriting:"))
# keyingi=(hozir+n)%24
# print(keyingi)

# 11
# dushanba=1
# seshanba=2
# chorshanba=3
# payshanba=4
# juma=5
# shanba=6
# yakshanba=7
# bugun=1
# n=int(input("kunni kiriting:"))
# print((bugun-1+n)%7+1)

# ism=input("ismingizni kiriting:")
# yosh=int(input("yoshingizni kiriting:"))
# manzil=input("soatni kiriting:")
# yoshi=2026-yosh
# print(ism, yoshi,"yilda tug'ilgan", manzil, "da yashaydi")

# yosh=int(input("yoshingizni kiriting:"))
# if yosh>18 and  yosh<60:
#     print("layoqatli")
# else:
#   print("layoqatsiz")
import math
# a=math.sqrt(25)
# print(a)

# b=math.floor(33)
# print(b)

# c=math.ceil(44)
# print(c)

# d=math.factorial(5)
# print(d)

# f=math.gcd(8, 14)
# print(f)

# a= int(input("4 xonalik sonni kiriting: "))
# birlar=a%10
# onlar=a%100//10
# yuzlar=(a//100)%10
# minglar=a//1000
# teskari=birlar*1000+onlar*100+yuzlar*10+minglar
# print(teskari)

# a= float(input("a sonni kiriting: "))
# b= float(input("b sonni kiriting: "))
# c= float(input("c sonni kiriting: "))
# if a==0:
#     print("a nolga teng bo'lmasligi kerak")
# else:
#    d=b**2-4*a*c
#    print(f"d= {d}")
# if d==0:
#     x=-b/2*a
#     print(f"x= {x}")
# if  d>0:
#     x1=(-b+math.sqrt(d))/2*a
#     x2=(-b-math.sqrt(d))/2*a
#     print(f"x1= {x1} x2= {x2}")
# if d<0:
#     print("yechimga ega emas")


# --------input() va turlarni o'zgartirish----------
# k1 vazifa
# a= int(input("a butun sonni kiriting: "))
# b= int(input("b butun sonni kiriting: "))
# print("yigindisi: ", a+b)
# print("ayirmasi: ", a-b)
# print("kopaytmasi: ", a*b)

# k2 vazifa
# ism= input("ismingizni  kiriting: ")
# yosh= int(input("yoshingizni kiriting: "))
# print(ism, "2026-yilda", 2026-yosh, "yoshda")

# k3 vazifa
# vazn= float(input("vaznni kiriting: "))
# boy= float(input("bo'yini kiriting: "))
# bmi=vazn/boy*2
# print(math.floor(bmi))

# k4-vazifa
# a= int(input("int ni kiriting: "))
# b= int(input("int ni kiriting: "))
# c= float(input("floatni kiriting: "))
# d= input("inputni  kiriting: ")
# e= int(float("int floatni kiriting: "))

# k5 
# print(bool(0))
# print(bool(-3))
# print(bool(""))
# print(bool("0"))
# print(bool(0.0))
# print(bool(None))







# 1
# summa= int(input("summa ni kiriting: "))
# a=divmod(summa, 100_000)
# b=divmod(summa, 50_000)
# c=divmod(summa, 10_000)
# d=divmod(summa, 5000)
# e=divmod(summa, 1000)
# print(a, b, c, d, e)

# 2
# a= int(input("a ni kiriting: "))
# b= int(input("b ni kiriting: "))
# c= int(input("c ni kiriting: "))
# p=(a+b+c)/2
# s=math.sqrt(p(p-a)*(p-b)*(p-c))
# print("p=", p, "s=", s)

# 3
# x1= int(input("x1 ni kiriting: "))
# x2= int(input("x2 ni kiriting: "))
# y1= int(input("y1 ni kiriting: "))
# y2= int(input("y2 ni kiriting: "))
# d=math.sqrt((x2-x1)**2+(y2-y1)**2)
# print(d)

# 4
# p= int(input("sum ni kiriting: "))
# r= int(input("foiz ni kiriting: "))
# n= int(input("yil ni kiriting: "))
# s=p*(1+r/100)*n
# print(s)

# 5
# r= int(input("radius sonni kiriting: "))
# s=math.pi*r**2
# l=2*math.pi*r
# print("s= ", s, "l=", l)

# 6
# a= float(input("a sonni kiriting: "))
# b= float(input("b sonni kiriting: "))
# c= float(input("c sonni kiriting: "))
# if a==0:
#     print("a nolga teng bo'lmasligi kerak")
# else:
#    d=b**2-4*a*c
#    print(f"d= {d}")
# if d==0:
#     x=-b/2*a
#     print(f"x= {x}")
# if  d>0:
#     x1=(-b+math.sqrt(d))/2*a
#     x2=(-b-math.sqrt(d))/2*a
#     print(f"x1= {x1} x2= {x2}")
# if d<0:
#     print("yechimga ega emas")

# print(f"[{'diyor':-^10}]")
# print("buxoro\nshahar")

# karta= input("karta raqamni kiriting: ")
# ism= input("ism familiyani kiriting: ")
# if len(karta)==16 and karta.isdigit() :
#     print("*"*12+karta[12:])
# else:
#     print("karta raqam 16 ta dan kam bolmasin")
# familiya=ism.find(" ")

# print(ism[familiya+1:]+" "+ism.strip[0].uppper())
# 1
# shahar= input("shahar nomini kiriting: ")
# print("uzunligi",len(shahar), "birinchi  harfi", shahar[0], "oxirgi harfi ", shahar[-1] )

# 2
# soz= input("sozni  kiriting: ")
# orta=len(soz)//2
# soz2=soz[orta]
# if soz2:
#     print(soz2)
# else:    
#   print(soz2+1)

# 3
# soz= input("sozni  kiriting: ")
# print(soz[0:3], soz[-3:])

# 4
# soz= input("sozni  kiriting: ")
# print("juft ", soz[0:len(soz):2], "toq", soz[0:len(soz):3])

# 5
# soz= input("sozni  kiriting: ")
# print(soz[::-1])

# 6
# soz= input("sozni  kiriting: ")
# yozuv=soz[-1]+soz[1:]+soz[1]
# print(yozuv)

# 7
# soz= input("sozni  kiriting: ")
# yozuv=len(soz)//2
# print(soz[yozuv:]+soz[:yozuv])

# 8
# soz= int(input("2026-09-30 kiriting: "))
# raqam=soz.find("-")
# print(raqam)

# kabissa yili
# kabissa=int(input("yilni kiriting: "))
# if kabissa % 100!=0 :
#     if kabissa % 400==0 or kabissa % 4 !=0:     
#         print("kabissa yili", kabissa)

# else:
#     print("kabissa yili emas")

# uchburchak
# a=int(input("a tomon kiriting: "))
# b=int(input("b tomon kiriting: "))
# c=int(input("c tomon kiriting: "))
# if a>0 and b>0 and c>0 :
#   if  a+b>c and a+c>b and b+c>a :
#     if a==b==c: 
#       print("teng tomonli")
#     elif a==b or b==c or c==a: 
#        print("teng yonli")
#     else: 
#        print("turli tomonli")
#   else:
#         print("mumkin emas")
# else:
#     print("manfiy son bor")


# katta kichigi
# a=int(input("a tomon kiriting: "))
# b=int(input("b tomon kiriting: "))
# c=int(input("c tomon kiriting: "))
# if a>b>c:
#     print(a)
# if a<b<c:
#     print(c)
# if a<b>c:
#     print(b)
# else:
#     print("teng")


# ---------if/ else-----------

# 1
# n=int(input("n sonni kiriting: "))
# if n>0:
#     print(n+1)
# else :
#     print(n)

# 2
# n=int(input("n sonni kiriting: "))
# if n>0:
#     print(n+1)
# else :
#     print(n-2)

#3
# n=int(input("n sonni kiriting: "))
# if n>0:
#     print(n+1)
# elif n==0 :
#     print(n+10)
# else:
#     print(n-2)    

# 4
# a=int(input("a sonni kiriting: "))
# b=int(input("b sonni kiriting: "))
# c=int(input("c sonni kiriting: "))
# if a>0 and b>0 and c<0:
#     print("1ta musbat")
# elif a>0 and b<0 and c<0:
#     print("2ta musbat")
# elif a<0 and b<0 and c<0:
#     print("3 ta musbat")
# else:
#     print("musbat son yoq")

# 5
# a=int(input("a sonni kiriting: "))
# b=int(input("b sonni kiriting: "))
# c=int(input("c sonni kiriting: "))
# if a>0 and b>0 and c>0 :
#     print("3ta musbat")
# elif a>0 and b>0 and c<0 :
#     print("2ta musbat va 1ta manfiy")
# elif a>0 and b<0 and c<0 :
#     print("1ta musbat va 2ta manfiy")
# else:
#     print("3ta manfiy")

# 6
# a=int(input("a sonni kiriting: "))
# b=int(input("b sonni kiriting: "))
# if a>b:
#     print(a ,"katta")
# else:
#     print(b , "katta")

# 7
# a=int(input("a sonni kiriting: "))
# b=int(input("b sonni kiriting: "))
# if a>b:
#     print(a ,"1")
# else:
#     print(b , "2")

# 8
# a=int(input("a sonni kiriting: "))
# b=int(input("b sonni kiriting: "))
# if a>b:
#     print(a ,":katta", b, ": kichik")
# else:
#     print(b , ":katta ", a, ":kichik")

# 9
# a=int(input("a sonni kiriting: "))
# b=int(input("b sonni kiriting: "))
# if a<b:
#     c=a
#     a=b
#     b=c
#     print(a,b)
# else:
#     print(a, b)

# 10
# a=int(input("a sonni kiriting: "))
# if a%2==0 and a<0:
#     print("manfiy juft son", a)
# elif a%2==0 and a>0:
#     print("musbat juft son")
# elif a%2!=0 and a>0:
#     print("musbat toq son")
# elif a==0:
#     print("nol")
# else :
#     print("manfiy toq")

# 11
# a=int(input("a sonni kiriting: "))
# if a%2==0 and a<10 :
#     print("1 xonalik juft")
# elif a%2==0 and a<99:
#     print("2 xonalik juft")
# elif a%2!=0 and a<99:
#     print("2 xonalik toq son")
# elif a%2==0 and a<999:
#     print("3 xonalik juft")
# elif a%2!=0 and a<999:
#     print("3 xonalik toq son")
# else:
#     print("1 xonalik toq")

# kabissa yili 12
# kabissa=int(input("yilni kiriting: "))
# if kabissa % 100!=0 :
#     if kabissa % 400==0 or kabissa % 4 !=0:     
#         print("kabissa yili", kabissa)

# else:
#     print("kabissa yili emas")

# 13

# katta kichigi
# a=int(input("a tomon kiriting: "))
# b=int(input("b tomon kiriting: "))
# c=int(input("c tomon kiriting: "))
# if a>b>c:
#     print(a)
# if a<b<c:
#     print(c)
# if a<b>c:
#     print(b)
# else:
#     print("teng")

# 14
# a=int(input("a tomon kiriting: "))
# b=int(input("b tomon kiriting: "))
# c=int(input("c tomon kiriting: "))
# if a >= b and a <= c or a <= b and a >= c:
#     print(a)
# elif b >= a and b <= c or b <= a and b >= c:
#     print(b)
# else:
#     print(c)

# 15
# a=int(input("a tomon kiriting: "))
# b=int(input("b tomon kiriting: "))
# c=int(input("c tomon kiriting: "))
# if a >= b and a <= c or a <= b and a >= c:
#     print(c+b-a)
# elif b >= a and b <= c or b <= a and b >= c:
#     print(a+c-b)
# else:
#     print(a+b-c)

# 16
# a=int(input("a sonini kiriting: "))
# b=int(input("b sonini kiriting: "))
# c=int(input("c sonini kiriting: "))
# if a < b < c:
#     a = a * 2
#     b = b * 2
#     c = c * 2
# else:
#     a = -a
#     b = -b
#     c = -c
# print("a =", a)
# print("b =", b)
# print("c =", c)


# ----------matnli algoritmlar-----------
# 1
# a=input("so'zni kiriting: ")
# if a[::-1]==a:
#   print(a)
# else:
#     print("xato")

# 2
# matn = input("Matn kiriting: ")
# matn = matn.lower()
# matn = matn.replace(" ", "")
# if matn == matn[::-1]:
#     print("Palindrom" , matn)
# else:
#     print("Palindrom emas")

# 3
# soz = input("So'z kiriting: ").lower()
# unli=soz.count("a")+soz.count("o")+soz.count("e")+soz.count("u")+soz.count("i")
# undosh=len(soz)-unli
# print(f"undoshlar soni: {undosh}\ unlilar soni {unli}")


# 4
# karta=input("karta raqam kiriting: ")
# if len(karta)==16:
#     karta= karta[:4]+"**** ****"+karta[12:]
#     print(karta)
# else:
#     print("karta raqam 16 ta bolish kerak")

# 5
# ism= input("Familiya ism otasini ismi kiriting: ")
# familiya=ism.find(" ")
# familya2=ism[:familiya]+ism[familiya+1].upper()
# ism2 = ism.find(" ",familiya+1)
# familya3 = familya2 + " " + ism[ism2+1].upper()

# print(familya3)



# if 17
# x= int(input("x sonni kiriting: "))
# y= int(input("y sonni kiriting: "))
# if x>0 and y>0 :
#     print("birinchi chorrak")
# elif x<0 and y>0 :
#     print("ikkinchi chorak")
# elif x<0 and x<0 :
#     print("uchinchi chorak")
# elif x>0 and y<0 :
#     print("to'rtinchi chorak")
# else :
#     x==0 and y==0
#     print(x, y )

# if 18
# A= int(input("A sonni kiriting: "))
# B= int(input("B sonni kiriting: "))
# C= int(input("C sonni kiriting: "))
# if A+C>B+C :
#     print("A nuqta yaqin")
# else :
#     print("B nuqta yaqin")

# 19
# a=int(input("a tomon kiriting: "))
# b=int(input("b tomon kiriting: "))
# c=int(input("c tomon kiriting: "))
# if a>0 and b>0 and c>0 :
#   if  a+b>c and a+c>b and b+c>a :
#     if a==b==c: 
#       print("teng tomonli")
#     elif a==b or b==c or c==a: 
#        print("teng yonli")
#     else: 
#        print("turli tomonli")
#   else:
#         print("mumkin emas")
# else:
#     print("manfiy son bor")

# 20
# a= int(input("a sonni kiriting: "))
# b= int(input("b sonni kiriting: "))
# c= int(input("c sonni kiriting: "))
# if a==0:
#     print("a nolga teng bo'lmasligi kerak")
# else:
#    d=b**2-4*a*c
#    print(f"d= {d}")
# if d==0:
#     x=-b/2*a
#     print(f"x= {x}")
# if  d>0:
#     x1=(-b+math.sqrt(d))/2*a
#     x2=(-b-math.sqrt(d))/2*a
#     print(f"x1= {x1} x2= {x2}")
# if d<0:
#     print("yechimga ega emas")

# 21
# boy= float(input("bo'yningizni kiriting: "))
# vazn= float(input("vazningizni kiriting: "))
# BMI=vazn/boy**2
# if BMI<18.5:
#     print("vazn yetishmaydi")
# elif BMI<25 :
#     print("normal")
# elif BMI<30 :
#     print("ortiqcha vazn")
# else :
#     print("semizlik")

# 22
# x= int(input("x sonni kiriting: "))
# if x>0:
#     f=2*math.sin(x)
#     print("f(x) ", f)
# else:
#     f=6-x
#     print("f(X) ", f)

# 23
# baho= int(input("bahoni kiriting: "))
# if baho>86 and baho<100 :
#     print("5")
# elif baho>71 and baho<85 :
#     print("4")
# elif baho>56 and baho<70 :
#     print("3")
# elif baho>0 and baho<55 :
#     print("2")
# else:
#     print("0")

# 24
# summa= int(input("summani kiriting: "))
# if summa>=1000_000:
#     chegirma=summa * 10/100
#     print("chegirma: ", chegirma) 
# elif summa>=500_000 :
#     chegirma=summa * 5 /100
#     print("chegirma: " , chegirma)

# case1
#    

# case2
# raqam= int(input("1-12  kiriting: "))
# match raqam:
#     case 12,1,2:
#         print("qish")
#     case 3,5:
#         print("bahor")
#     case 6,8:
#         print("yoza")
#     case 9,11:
#         print("kuz")
#     case _:
#         print("xato")

# case3
# oy= input("oyni kiriting: ")
# match oy:
#     case "yanvar":
#         print("31")
#     case "fevral":
#         print("28")
#     case "mart":
#         print("31")
#     case "aprel":
#         print("30")
#     case "may":
#         print("31")
#     case "iyun":
#         print("30")
#     case "iyul":
#         print("31")
#     case "avgust":
#         print("31")
#     case "sentabr":
#         print("30")
#     case "oktabr":
#         print("31")
#     case "noyabr":
#         print("30")
#     case "dekabr":
#         print("31")
#     case _:
#         print("xato")

# case4
# a= float(input("a  kiriting: "))
# b= float(input("b  kiriting: "))
# N= float(input("amal  kiriting: "))

# match a, b:
#     case "N==":
#         print("qish")
#     case 3,5:
#         print("bahor")
#     case 6,8:
#         print("yoza")
#     case 9,11:
#         print("kuz")
#     case _:
#         print("xato")

# case6
# rang= float(input("rangni  kiriting: "))

# match rang:
#     case "yashil":
#         print("yuring")
#     case "sariq":
#         print("tayyorlaning")
#     case "qizil":
#         print("to'xtang")
#     case _:
#         print("xato")



