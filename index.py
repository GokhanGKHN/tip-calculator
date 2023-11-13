#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Tip hesaplama uygulamasını kullandığınız için teşekkürler. ")
Toplam =float(input("Lütfen fatura tutarını giriniz: ")) 
PahsisOranı=float(input("Lütfen pahşişi oranını giriniz: "))
KısıSayısı=int(input("Lütfen kişi sayısının giriniz: "))

KısıBasıDusen =(Toplam / KısıSayısı) 
Oran =(Toplam / KısıSayısı) * PahsisOranı
Toplam =KısıBasıDusen + Oran

print(f"The number rounded to two decimal places is {Toplam:.2f}")