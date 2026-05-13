---
tags:
  - MO
  - Routing
  - Rules
  - Configuration
---

# Regra de roteamento MO

## Visão geral

**MO Regras de Roteamento** no iTextPro são usados para definir como mensagens MO recebidas devem ser identificadas, filtradas e roteadas dentro da plataforma.

A regra de roteamento determina:

- Que tráfego de entrada MO deve ser processado
- Qual palavra-chave deve desencadear o roteamento
- Que usuário deve receber o tráfego MO
- Que tipo de interface deve ser usado para entrega

Regras de Roteamento MO funcionam em conjunto com o configurado **HTTP MO Handler**.

---

## Caminho de navegação

<span data-ph="0"></span> □ <span data-ph="1"></span> □ <span data-ph="2"></span> □ <span data-ph="3"></span>.

![Manage MO Routing Rules list](images/morouting-01-list.png)

---

## Parâmetros da regra de roteamento MO

Os seguintes parâmetros devem ser configurados ao criar a regra de roteamento.

## Parâmetros Gerais

### 1] Nome da regra

A **Nome da Regra** identifica exclusivamente a regra de roteamento MO dentro da plataforma.

Este nome é usado para:

- Gestão de regras
- Controlo do tráfego
- Administração
- Resolução de Problemas

!!! example
    ```
    MO_ROUTE_KEYWORD_01
    ```

---

### 2] Tempo de vida

A **Tempo de vida** parâmetro define a duração de validade da regra de roteamento.

**Uso:**

- Pode ser usado para campanhas temporárias
- Suporta roteamento MO baseado no tempo
- Útil para serviços de tempo limitado

!!! tip
 Se não for necessário expirar, este campo pode ser deixado em branco.

---

## Configuração da Interface do Gateway

### Manipulador

A **Manipulador** campo é usado para selecionar o HTTP MO Handler previamente configurado na plataforma.

Este manipulador irá processar todas as solicitações MO correspondentes às condições de roteamento. O manipulador será usado no caso de o fornecedor enviar MO com **Ligação HTTP**.

### Gateway

Caso o vendedor suporte o **SMPP** protocolo para enviar o MO hits, então durante a criação da regra de roteamento do MO o administrador precisa selecionar o **Gateway** e escolha o gateway correto para obter os hits do gateway correto.

**Objectivo:**

- Links tráfego MO com o objetivo correto
- Associa roteamento com o canal de entrada
- Activa o fluxo de trabalho de processamento de mensagens

![Add New MO Rule — General Parameters & Gateway Interface](images/morouting-02-general.png)

---

## Condições de Roteamento

Condições de roteamento definem o **lógica de filtragem** para o tráfego de entrada MO. A plataforma avalia essas condições antes de processar ou encaminhar a solicitação de MO.

### 1] Condição do Originador

A **Originador** condição define filtragem com base no número do remetente móvel.

**Configuração do Exemplo:** <span data-ph="0"></span>

Selecionar **Qualquer** permite mensagens MO de todos os números remetentes. A filtragem específica do remetente também pode ser configurada se necessário.

---

### 2] Condição de Destino

A **Destino** condição define o código curto de recepção ou número de código longo.

| Campo | Valor |
|-------|-------|
| **Tipo de Condição** | <span data-ph="0"></span> |
| **Exemplo** | <span data-ph="0"></span> |

A regra de roteamento só será ativada se a mensagem MO recebida for recebida no número de destino configurado.

---

### 3] Condição da Mensagem

A **Mensagem** condição define os critérios de correspondência de palavras-chave.

| Campo | Valor |
|-------|-------|
| **Tipo de Condição** | <span data-ph="0"></span> |
| **Palavra- chave do exemplo** | <span data-ph="0"></span> |

A regra de roteamento só será ativada se a mensagem recebida começar com a palavra-chave configurada.

!!! example
 Para uma mensagem recebida <span data-ph="0"></span>, uma vez que a mensagem começa com <span data-ph="1"></span>, a regra de roteamento processará o pedido MO.

![Routing Conditions and User / Endpoint selection](images/morouting-03-condition-user.png)

---

## Mapeamento do usuário e do ponto final

### 1] Usuário

Selecione o **conta de usuário** para o qual o tráfego de MO deve ser mapeado e entregue.

Este mapeamento garante que o usuário correto receba as mensagens MO recebidas.

### 2] Tipo de interface de usuário

A **Tipo de interface de usuário** define como a mensagem MO deve ser enviada após o roteamento.

**Tipos de interface suportados:**

| Tipo | Designação das mercadorias |
|------|-------------|
| **Não Seleccionado** | Nenhum roteamento específico da interface será aplicado. |
| **ESME** | Roteia o tráfego de MO através da conectividade SMPP. Geralmente usado quando o usuário está conectado via protocolo SMPP. |
| **Webhook** | Roteia o tráfego MO para um endpoint externo da API HTTP. Comumente usado para integrações de CRM, aplicativos de terceiros, sistemas de processamento baseados na web e fluxos de trabalho baseados em API. |

---

## Salvar regra de roteamento

Após configurar todos os parâmetros de roteamento:

1. Verifique as condições de encaminhamento.
2. Validar a configuração da palavra-chave.
3. Clique em **Gravar**.

A regra de roteamento MO está agora configurada e ativa com sucesso para processamento de tráfego MO.

!!! tip "Verificação"
 Depois de salvar a regra, envie uma mensagem de teste MO que corresponda às condições configuradas (enviar o número de destino permitido, corrigir a mensagem de destino, começando com a palavra-chave configurada) e confirme que a regra dispara, verificando os logs de endpoint do MO do usuário ou webhook.
