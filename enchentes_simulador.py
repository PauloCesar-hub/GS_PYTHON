
# Simulador de Risco de Enchentes
# Autores: João da Silva (RM: 123456), Maria Souza (RM: 654321)
4
def ler_float(mensagem):
    """Solicita um número decimal do usuário com validação."""
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def receber_dados():
    """Recebe os dados da cidade e níveis de chuva e rio."""
    cidade = input("Informe o nome da cidade: ")
    chuva = ler_float("Informe o nível de chuva (em mm): ")
    rio = ler_float("Informe o nível do rio (em metros): ")
    return cidade, chuva, rio

def calcular_risco(chuva, rio):
    """Calcula o risco de enchente baseado nos níveis de chuva e rio."""
    if chuva > 100 or rio > 5:
        return "ALTO"
    elif chuva > 50 or rio > 3:
        return "MODERADO"
    else:
        return "BAIXO"

def registrar_dado(registros, cidade, chuva, rio, risco):
    """Armazena os dados na lista de registros."""
    registros.append({
        "cidade": cidade,
        "chuva": chuva,
        "rio": rio,
        "risco": risco
    })

def exibir_registros(registros):
    """Exibe todos os registros armazenados."""
    if not registros:
        print("Nenhum registro encontrado.")
        return
    print("\n--- Registros de Enchentes ---")
    for r in registros:
        print(f"{r['cidade']} | Chuva: {r['chuva']} mm | Rio: {r['rio']} m | Risco: {r['risco']}")

def filtrar_por_risco(registros, nivel_risco):
    """Filtra e exibe registros com base no risco informado."""
    filtrados = [r for r in registros if r["risco"].upper() == nivel_risco.upper()]
    if not filtrados:
        print(f"Nenhum registro com risco {nivel_risco.upper()} encontrado.")
    else:
        print(f"\n--- Registros com Risco {nivel_risco.upper()} ---")
        for r in filtrados:
            print(f"{r['cidade']} | Chuva: {r['chuva']} mm | Rio: {r['rio']} m")

def calcular_media_chuva(registros):
    """Calcula e exibe a média de chuva dos registros."""
    if not registros:
        print("Nenhum registro para calcular média.")
        return
    media = sum(r['chuva'] for r in registros) / len(registros)
    print(f"Média de chuva registrada: {media:.2f} mm")

def main():
    registros = []
    while True:
        print("\nMenu:")
        print("1. Registrar nova cidade")
        print("2. Ver todos os registros")
        print("3. Filtrar por risco")
        print("4. Ver média de chuva")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cidade, chuva, rio = receber_dados()
            risco = calcular_risco(chuva, rio)
            registrar_dado(registros, cidade, chuva, rio, risco)
            print(f"Risco na cidade {cidade}: {risco}")
        elif opcao == "2":
            exibir_registros(registros)
        elif opcao == "3":
            nivel = input("Digite o nível de risco para filtrar (BAIXO, MODERADO, ALTO): ")
            filtrar_por_risco(registros, nivel)
        elif opcao == "4":
            calcular_media_chuva(registros)
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
