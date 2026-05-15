---
tags:
  - Reporting
  - Business Insight
  - Gateway
---

# Contagem sábia do portal

**Navegação:** <span data-ph="0"></span> □ <span data-ph="1"></span> □ <span data-ph="2"></span>.

## Visão geral

A **Contagem sábia do portal** O relatório fornece aos administradores uma visão consolidada dos volumes de submissão de mensagens em todos os gateways configurados. O relatório abrange o **últimos sete dias** em uma base diária, tornando fácil identificar padrões de tráfego e distribuição de carga em um relance.

![Gateway Wise Count — All Gateways (7-day view)](images/gwcount-01-all-gateways.png)

---

## Usando o Filtro de Gateway

Para restringir o relatório a um gateway específico, selecione o gateway desejado do **filtro suspenso** disponível no ecrã do relatório. A tabela irá atualizar para mostrar apenas os dados de submissão do gateway.

![Gateway Wise Count — Filtered by a single gateway](images/gwcount-02-filtered.png)

---

## O Que o Relatório Mostra

| Coluna | Designação das mercadorias |
|--------|-------------|
| **Nome do Portal** | Nome amigável do gateway configurado. |
| **Colunas de data (uma por dia)** | Contagem total de mensagens através desse gateway no dia correspondente. |

!!! note
 As contagens de mensagens visíveis são computadas em cada **fuso horário próprio do gateway**, não o fuso horário da aplicação. Isto é mostrado na nota na página acima da tabela.

---

## Quando usar este relatório

- Dips de tráfego dia-o-dia que podem indicar problemas de fornecedores ou de rede.
- Identificar os gateways subutilizados que podem ser candidatos à reforma ou reencaminhamento.
- Verifique se novos gateways adicionados estão recebendo a parte esperada do tráfego.
- Forneça instantâneos rápidos de volume para as partes interessadas.
