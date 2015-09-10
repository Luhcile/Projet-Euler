# Projet-Euler prog 1
resultat = 0
for i in range(1, 1000):
  if i%3 == 0 or i%5 == 0:
    resultat += i
print(resultat)

#Projet Euler prog 2 
a, b = 1, 2
resultat = 0
while b <= 4000000:
  if b % 2 == 0:
    resultat += b
  a, b = b, a + b
print(resultat)

#Projet Euler prog 3
def is_prime(nb):
    if nb == 1:
        return False
    if nb == 2:
        return True
    elif nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

def divisors(nb, extremum = False):
    divisors = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors
    
divs = divisors(600851475143)
divs.sort(reverse=True)
for i in divs:
    if is_prime(i):
        print(i)
        break
        
# Projet Euler prog 4
def is_palindrome(nb):
    if str(nb) == str(nb)[::-1]:
        return True
    return False
resultat = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        produit = i*j
        #Test si le produit est un palindrome
        if is_palindrome(produit):
            if produit > resultat:
                resultat = produit
print(resultat)

#Projet Euler 5
print(2*2*2*2*3*3*5*7*11*13*17*19)

