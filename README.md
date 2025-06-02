
# 🌊 Simulador de Risco de Enchentes no Brasil

Projeto desenvolvido para a disciplina **Computational Thinking Using Python** com o objetivo de aplicar conceitos fundamentais de programação na resolução de um problema social relevante: as enchentes no Brasil.

## 📌 Objetivo

Simular o risco de enchentes em cidades brasileiras com base em dados de **chuva** (mm) e **nível do rio** (m). A aplicação permite:
- Entrada validada dos dados
- Processamento da análise de risco
- Armazenamento dos registros
- Visualização dos resultados

## ⚙️ Tecnologias

- Python 3.x
- Ambiente de terminal (CLI)

## 🧠 Lógica de Análise

A análise é feita com base nos seguintes critérios:

| Chuva (mm) | Nível do Rio (m) | Risco     |
|------------|------------------|-----------|
| > 100      | > 5              | ALTO      |
| > 50       | > 3              | MODERADO  |
| ≤ 50       | ≤ 3              | BAIXO     |

## 📂 Funcionalidades

- [x] Inserção de dados validados
- [x] Cálculo automático de risco
- [x] Armazenamento em lista de registros
- [x] Visualização de todos os registros salvos
- [x] Interface de menu simples e intuitiva

## 🧩 Estrutura Modular

- `ler_float`: valida entrada numérica
- `receber_dados`: coleta dados do usuário
- `calcular_risco`: analisa o risco da enchente
- `registrar_dado`: salva os dados na lista
- `exibir_registros`: exibe os dados cadastrados
- `main`: interface principal com menu

## ▶️ Execução

```bash
python enchentes_simulador.py
```

## 💡 Exemplo de Uso

```
Informe o nome da cidade: Porto Alegre
Informe o nível de chuva (em mm): 120
Informe o nível do rio (em metros): 4.8
Risco na cidade Porto Alegre: ALTO
```

## 👨‍🏫 Avaliação

Critérios atendidos:
- Estruturas de decisão e repetição
- Validação de dados de entrada
- Armazenamento com listas
- Modularização e funções com retorno
- Interface clara no terminal
- Comentários explicativos

## 🧾 Autores

- Paulo Cesar de Govea Junior - (RM:566034)
- Guilherme Vilela Perez - (RM:564422)
- Gustavo Panham Dourado - (RM:563904)

## 📎 Licença

Este projeto é acadêmico e livre para fins educacionais.
