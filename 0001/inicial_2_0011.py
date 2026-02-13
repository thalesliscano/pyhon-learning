weight = float(input("Digite seu peso: "))
height = float(input("Digite sua altura: "))

imc = weight / height ** 2

print(f"Seu peso é {weight}")
print(f"Sua altura é {weight}")
print(f"." * 10)
print(f"Seu imc é {imc:.2f}")


categoria = (
    "Abaixo do peso" if imc < 18.5 else
    "Normal" if 18.5 <= imc < 25.00 else
    "Sobrepeso" if 25.0 <= imc < 30.00 else
    "besidade grau I" if 30.0 <= imc < 35.00 else
    "besidade grau II" if 35.0 <= imc < 40.00 else
    "besidade grau III"
)

print(categoria)