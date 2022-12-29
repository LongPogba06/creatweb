import random

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]
a = [0, 1, 2]
b = [0, 1, 2]

Argentina = random.choice(x)
France = random.choice(y)
Argentina1 = random.choice(a)
France1 = random.choice(b)
ArgentinaP = random.choice(x)
FranceP = random.choice(y)

if Argentina > France:
    print("Tỉ số là: "+"Argentina " + str(Argentina)+"-"+str(France) + " France")
    print("Argentina đã thắng")
elif Argentina < France:
    print("Tỉ số là: "+"Argentina " + str(Argentina)+"-"+str(France) + " France")
    print("France đã thắng")
elif Argentina == France:
    print("Tỉ số là: "+"Argentina " + str(Argentina)+"-"+str(France) + " France")
    print("2 đội đã cầm hòa trong 90 phút và đưa nhau vào hiệp phụ")

    if Argentina1 > France1:
        print("Tỉ số là: "+"Argentina " + str(Argentina+Argentina1)+"-"+str(France+France1) + " France")
        print("Argentina đã thắng")
    elif Argentina1 < France1:
        print("Tỉ số là: "+"Argentina " + str(Argentina+Argentina1)+"-"+str(France+France1) + " France")
        print("France đã thắng")
    elif Argentina1 == France1:
        print("Tỉ số là: "+"Argentina " + str(Argentina+Argentina1)+"-"+str(France+France1) + " France")
        print("2 đội đã cầm hòa trong 120 phút và đưa nhau vào loạt sút luân lưu")

        if ArgentinaP > FranceP:
            print("Tỉ số luân lưu là: " + "Argentina " + str(ArgentinaP)+"-"+str(FranceP) + " France")
            print("Argentina đã thắng")      
        elif ArgentinaP < FranceP:
            print("Tỉ số luân lưu là: " + "Argentina " + str(ArgentinaP)+"-"+str(FranceP) + " France")   
            print("France đã thắng")
                   