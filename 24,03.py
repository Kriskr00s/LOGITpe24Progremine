from random import randint

tõenäosus = 75
i = 0
while i < 10:
    if randint(1,100) <= tõenäosus:
        print ("kiri")
    else:
        print("kull")
    i += 1