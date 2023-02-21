#              by wassim bolles 
#              2/19/2023 2:59PM
#      delta.py                DELTA MATH FUNCTION
#      email : wassimbolles12@gmail.com
#      phone : +212 625218307
#      you can take this file and change anything

print(">> Programme qui calcule Δ de tous les fonctions de 2ème degré")

#sqrt function
def fsqrt(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    elif number == 0:
        return 0
    else:
        x = number
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + number // x) // 2
        return x
        
#main programme
print("Par exemple : ax2 + bx + c = 0\n")
a = float(input("entrer la valeur de a de votre fonction : "))
b = float(input("entrer la valeur de b de votre fonction : "))
c = float(input("entrer la valeur de c de votre fonction : "))

delta = (b * b) - (4 * a * c)
sdelta = delta
if delta < 0:
    sqrt_delta = fsqrt(-delta)
    sqrt_delta = 1j * sqrt_delta
    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)
    A2 = 2 * a
    print("__________________________________________________________________________________________________________")
    print(f"dans ce cas l'equation' admet deux solutions dans C x1 et x2 car Δ = {delta} est strictement inferieur à 0\n")
    print("x1 = -b - √Δ\n     --------\n       2a")
    print("x2 = -b + √Δ\n     --------\n       2a\n")
    print("__________________________________________________________________________________________________________")
    print("les résultats après le remplacement : \n")
    print(f"x1 = -{b} - √{delta}\n     -------------\n       {A2}")
    print(f"x2 = -{b} + √{delta}\n     -------------\n       {A2}\n")
    print("__________________________________________________________________________________________________________")
    print(f"les résultats final sont : \nx1 = {x1}\nx2 = {x2}\n\nS = ( {x1} , {x2} )")
    print("__________________________________________________________________________________________________________")
elif delta == 0:
    result = (-b) / (2 * a)
    a2 = 2 * a
    print("__________________________________________________________________________________________________________")
    print("dans ce cas nous n'avons qu'une seule solution dons ℝ car Δ = 0\n")
    print("        -b\n        --\n        2a")
    print("__________________________________________________________________________________________________________")
    print("\nle résultat après le remplacement : \n")
    print(f"        -{b}\n        ----\n        {a2}")
    print("__________________________________________________________________________________________________________")
    print(f"\nle résultat final : x = {result}\nS = { {result} }")
    print("__________________________________________________________________________________________________________")
else:
    sqrt_delta = fsqrt(sdelta)
    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)
    A2 = 2 * a
    print("__________________________________________________________________________________________________________")
    print(f"dans ce cas l'equation' admet deux solutions dans ℝ x1 et x2 car Δ = {delta} est strictement supérieur à 0\n")
    print("x1 = -b - √Δ\n     --------\n       2a")
    print("x2 = -b + √Δ\n     --------\n       2a\n")
    print("__________________________________________________________________________________________________________")
    print("les résultats après le remplacement : \n")
    print(f"x1 = -{b} - √{delta}\n     -------------\n       {A2}")
    print(f"x2 = -{b} + √{delta}\n     -------------\n       {A2}\n")
    print("__________________________________________________________________________________________________________")
    print(f"les résultats final sont : \nx1 = {x1}\nx2 = {x2}\n\nS = ( {x1} , {x2} )")
    print("__________________________________________________________________________________________________________")
