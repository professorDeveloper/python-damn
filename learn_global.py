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


def talabalar(*, talaba):
    print(talaba)


talabalar(talaba=("Saikou", "Azamov", "Aikou"))


# ARgs qachonki parametr berish nomalum bo`lsa foydalanimz
def lol_arg(*args):
    print(args)


lol_arg(2, 31, "44")


# kwargs esa args kabi lekin dictionary type da malumot oladi asosan mening tushunishim bo`yicha
# bu 2 funksiyadagi ish bajarish sharti paramterlar ga tasi qilmasligi kerak ekan

def lol_kwarg(**kwargs):
    print(kwargs)


lol_kwarg(foo="bar", cat="mosh", alien="Bob")
