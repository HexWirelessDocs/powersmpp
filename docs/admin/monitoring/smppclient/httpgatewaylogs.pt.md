---
tags:
  - Monitoring
  - HTTP
  - Gateway
  - Logs
---

# Registros de Gateway HTTP

**Navegação:** <span data-ph="0"></span> □ <span data-ph="1"></span> □ <span data-ph="2"></span>.

## Visão geral

A **Registros de Gateway HTTP** a seção permite aos administradores visualizar o HTTP completo **pedido** e **resposta** comunicação trocada entre o aplicativo PowerSMPP e fornecedores de gateway configurados. Esses logs são essenciais para diagnosticar falhas de entrega, verificar cargas úteis da API e verificar interações de gateway.

---

## Passos para Ver os Registos

1. Selecione o **Gateway HTTP** da **Nome do Portal** Largar.
2. Selecione o necessário **Intervalo de Datas** usando o selecionador de datas.
3. Escolha o **Tipo de Registo** (<span data-ph="0"></span> / <span data-ph="1"></span> / <span data-ph="2"></span>) conforme necessário.
4. Selecione o **Verbosidade** nível se for necessária uma filtragem granular.
5. Clique **Enviar** para obter e exibir os logs correspondentes.

![HTTP Gateway Logs — Log list view](images/httplogs-01-list.png)

---

## Seções de log disponíveis

### Organismo de Pedido

A **Organismo de Pedido** contém a carga completa transmitida da aplicação PowerSMPP para o fornecedor de gateway.

![HTTP Gateway Logs — Request Body expanded](images/httplogs-02-request-body.png)

!!! info "Organismo de solicitação — dados incluídos"
    - **Número Móvel** — número de destino do SMS
    - **ID do remetente** — o endereço de origem / ID do remetente utilizado
    - **Parâmetros de Pedido** — parâmetros API completos enviados para o gateway
    - **Detalhes da máquina / IP** — Endereço IP e porta do ponto de ligação
    - **Tempo de submissão** — calendário do envio do pedido

### Corpo de Resposta

A **Corpo de Resposta** contém os dados de reconhecimento e status recebidos de volta do fornecedor de gateway.

![HTTP Gateway Logs — Response Body expanded](images/httplogs-03-response-body.png)

!!! info "Organismo de resposta — Dados incluídos"
    - **Resposta do Portal** — resposta em bruto devolvida pelo gateway
    - **Informação do Estado** — códigos do estatuto de entrega ou de aceitação
    - **Detalhes do Erro** — códigos de erro e descrições para as observações falhadas
    - **Agradecimento de resposta** — confirmação de que o gateway tratou o pedido

---

## Opções do Filtro

Os administradores podem refinar a visão de log usando os seguintes filtros adicionais:

| Filtro | Utilização |
|--------|-----|
| **Endereço IP** | Filtrar registros pelo IP do servidor de gateway. |
| **ID do remetente** | Filtrar logs originando o ID do remetente. |
| **Número Móvel** | Filtrar registros por número de celular de destino. |

---

## Fluxo Típico de Resolução de Problemas

1. Uma campanha relata falhas inesperadas ou mensagens não entregues.
2. Abrir **Registros de Gateway HTTP**, selecione o gateway afetado e um intervalo de data que cobre o problema.
3. Definir **Tipo de Registo** para <span data-ph="0"></span> para emergir apenas trocas falhadas.
4. Expandir o **Organismo de Pedido** para confirmar que a carga de saída estava correcta.
5. Expandir o **Corpo de Resposta** para ler o código/descrição de erro real retornado pelo vendedor.
6. Utilização **Endereço IP**, **ID do remetente**, ou **Número Móvel** filtros para isolar uma amostra de teste específica para a equipe de suporte do fornecedor.
