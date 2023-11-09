class_name = input("Digite o nome da classe: ")
variaveis = []

while True:
    var_nome = input("Digite o nome da variável (0 para parar): ")
    if var_nome == "0":
        break
    var_tipo = input("Digite o tipo da variável: ")
    variaveis.append((var_tipo, var_nome))

# Class e Atributos
print(f"public class {class_name} {{")
for var in variaveis:
    print(f"    private {var[0]} {var[1]};")
print()

# Construtor
print(f"    public {class_name}(", end="")
for i, var in enumerate(variaveis):
    print(f"{var[0]} {var[1]}", end="")
    if i < len(variaveis) - 1:
        print(", ", end="")
print(") {")
for var in variaveis:
    print(f"        this.{var[1]} = {var[1]};")
print("    }")
print()

# Setters e Getters
for var in variaveis:
    print(f"    public {var[0]} get{var[1].capitalize()}() {{")
    print(f"        return {var[1]};")
    print("    }")
    print()
    print(f"    public void set{var[1].capitalize()}({var[0]} {var[1]}) {{")
    print(f"        this.{var[1]} = {var[1]};")
    print("    }")
    print()

# toString()
print("    @Override")
print("    public String toString() {")
print(f'        return "{class_name}: " +')
for i, var in enumerate(variaveis):
    print(f'               "{var[1]}= " + {var[1]}', end="")
    if i < len(variaveis) - 1:
        print(' + ", " + ', end="\n")
print(";\n    }")
print("}")
