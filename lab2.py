#диффи-хеллман
import random
g=random.randrange(10_000,100_000)#число, загаданное Бобом
p=random.randrange(10_000,100_000)#число, загаданное Алисой
def Isprime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True
at = Isprime(g)
bt = Isprime(p)
while (not at):
	g=random.randrange(10_000,100_000)#число, загаданное Бобом
	at = Isprime(g)
while (not bt):
	p=random.randrange(10_000,100_000)#число, загаданное Алисой
	bt = Isprime(p)
print("g: ", g)
print("p: ", p)
#3 сторона имеет доступ к этим числам
a = random.randrange(1_000_000,2_000_000)#Второе число Боба
b = random.randrange(1_000_000,2_000_000)#Второе число Алисы
print("	a: ", a)
print("	b: ", b)
#3 сторона имеет доступ к этим числам
A = (g**a) % p#число боба
B = (g**b) % p#число алисы
#3 сторона имеет доступ к этим числам
print("Вычисленные переменные: ",A, " и ", B)
KA = B**a % p;
KB = A**b % p;
#Единый ключ, известный только Алисе и Бобу
print ("Cекретный ключ Алисы: ",KA)
print ("Cекретный ключ Боба: ",KB)
