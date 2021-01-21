# Fizzbuzz challenge

#for i in range(0,99):
#   if i % 5 == 0 and i % 3 == 0:
#      print("fizzbuzz")
# elif i % 3 == 0:
#    print("fizz")
#elif  i % 5 == 0:
#    print("buzz")

# Altercheck

#age = input("Alter angeben: ")

#age= int(age)

#if age >= 18:
#    print("kannst zocken")
#else:
#    print("du kommst hier nicht rein")

# Urlaubsrechner

age = input("Alter angeben:")
age = int(age)

mongo = input("Behinderungsgrad in % angeben:")
mongo = int(mongo)

verschwendete_zeit = input("Wie lange bist du im Unternehmen tätig:")
verschwendete_zeit= int(verschwendete_zeit)

urlaubstage = 26

if age < 18:
    urlaubstage = 30
elif age > 55:
    urlaubstage = urlaubstage+2

if mongo > 50:
    urlaubstage = urlaubstage + 5

if verschwendete_zeit > 10:
    urlaubstage = urlaubstage + 2

print(urlaubstage)