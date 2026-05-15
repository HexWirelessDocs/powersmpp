---
tags:
  - Reporting
  - Business Insight
  - User
  - Profit
---

# Relatório de Lucro Sábio do Usuário

**Navegação:** <span data-ph="0"></span> □ <span data-ph="1"></span> □ <span data-ph="2"></span>.

## Visão geral

A **Relatório de Lucro Sábio do Usuário** permite que os administradores analisem o tráfego de SMS a nível do utilizador e a rentabilidade para qualquer intervalo de datas seleccionado. O relatório baseia-se **inteiramente em mensagens enviadas pelos usuários através do aplicativo** e fornece dados detalhados de receita, custo e margem por conta do cliente.

---

## 1. Seleção do Usuário

Selecione uma conta de usuário específica da lista suspensa para gerar um relatório de lucro direcionado para esse cliente.

## 2. Seleção de País

Filtrar dados de tráfego por país de destino para obter análise granular da rentabilidade do usuário por região.

## 3. Filtro de Intervalo de Datas

Defina um intervalo de datas personalizado para gerar relatórios de lucro do usuário para qualquer faturamento ou período operacional.

---

## 4. Tabela Ver Relatório

A **Vista da Tabela** mostra informações detalhadas sobre rentabilidade do usuário em formato tabular.

![User Wise Profit — Table View (all users)](images/userprofit-01-table-all.png)

![User Wise Profit — Table View (highlighted)](images/userprofit-02-table-highlighted.png)

### Referência da coluna

| Coluna | Designação das mercadorias |
|--------|-------------|
| **Nome do Utilizador** | Nome / identificador da conta de usuário. |
| **Nome do país** | País de destino do tráfego SMS do usuário. |
| **MCCMNC** | Código do país móvel + Código da rede móvel. |
| **Nome da rede** | Destino nome da rede móvel. |
| **Contagem de Mensagens** | Total de mensagens SMS enviadas pelo usuário. |
| **Preço de Compra** | Custo real de roteamento incorrido para o processamento do tráfego do usuário. |
| **Preço de venda** | Valor total de venda cobrado ao utilizador. |
| **Margem % (Vendas − Compra)** | Percentagem de lucro calculada para o tráfego do usuário. |
| **Margem (Vendas - Compra)** | Lucro total obtido do tráfego de usuários em USD. |

---

## 5. Graph View Report

A **Vista de Gráficos** torna um gráfico de barras de rentabilidade do usuário, permitindo uma comparação rápida entre os clientes.

![User Wise Profit — Graph View (Margin by user)](images/userprofit-03-graph-view.png)

---

## 6. Análise da submissão da mensagem

Todos os cálculos no Relatório de Lucro Sábio do Usuário são conduzidos **exclusivamente** por mensagens enviadas do lado do utilizador através da aplicação. O tráfego que ultrapassa o caminho de submissão do usuário da aplicação não está incluído neste relatório.

---

## 7. Fórmula de cálculo do lucro

```
Margin (USD)          =  Sales Price − Purchase Price

Margin Percentage (%) = ((Sales Price − Purchase Price) / Purchase Price) × 100
```

!!! tip
 Combinar este relatório com **Gateway lucro sábio** Ver rentabilidade de dois ângulos complementares — o cliente (lado das receitas) e o vendedor (lado dos custos).
