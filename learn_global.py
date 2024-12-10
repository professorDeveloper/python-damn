summa = 200_000


def kammunal_tulov():
    global summa
    summa = summa - 10_000


def wifi_tulov():
    global summa
    summa = summa - 100_000


def uydan_yordam():
    global summa
    summa = summa + 500_000


wifi_tulov()
kammunal_tulov()

print(summa)


def talabalar(*,talaba):
    print(talaba)


talabalar(talaba = ("Saikou", "Azamov", "Aikou"))
