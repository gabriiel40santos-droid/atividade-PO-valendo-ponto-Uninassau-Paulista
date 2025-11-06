while True:
    nome = input("Digite seu nome: ").strip()
    
    if not nome or any(char.isdigit() for char in nome):
        print("Nome inválido! Digite apenas letras e não deixe vazio.\n")
        continue  
    else:
        break

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Idade inválida! Digite apenas números.\n")

print(f"\nDados recebidos com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
