---
tags:
  - HTTP
  - OAuth
  - Handler
  - Configuration
---

# Configuração do OAuth Handler

In **Gateway HTTP**, apoiamos **3 tipos de autorização**:

| # # | Tipo | Designação das mercadorias |
|---|------|-------------|
| 1 | **Sem Auth** | Não é necessária autorização. |
| 2 | **Auth Básico** | Um nome de usuário e senha são necessários para autenticação segura da API. |
| 3 | **OAuth 2.0** | A versão mais recente da autorização, usada para regenerar novas credenciais após um certo período para manter a alta segurança da API usando o **OAuth Handler** API. |

Neste documento, explicaremos todas as etapas e informações necessárias para o **OAuth Handler** configuração para o Gateway HTTP.

![Manage OAuth Handler list](images/oauthhandler-01-list.png)

---

## Navegação

<span data-ph="0"></span> □ <span data-ph="1"></span> □ <span data-ph="2"></span> □ <span data-ph="3"></span>.

![Manage OAuth Handler form](images/oauthhandler-02-add-new.png)

---

## Campos de Tratamento de OAuth

| Campo | Requerido | Designação das mercadorias |
|-------|----------|-------------|
| **Nome** | Sim. | Um nome amigável para o manipulador OAuth. Ajuda a identificar e gerenciar facilmente diferentes manipuladores OAuth dentro da aplicação. |
| **URL do Token** | Sim. | O endpoint URL onde o aplicativo irá solicitar o token OAuth. É o URL fornecido pelo fornecedor para obter o token de acesso. |
| **Tempo de expiração** | Sim. | A duração em minutos para os quais o token de acesso permanecerá válido. Após este período, o token expirará, e um novo precisará ser gerado. |
| **Código de expiração do item** | Sim. | O código de erro que indica que o token expirou. Quando este código de erro for recebido, o sistema saberá que precisa atualizar o token. |
| **Método de pedido** | Sim. | O método HTTP usado para solicitar o token da URL do Token — <span data-ph="0"></span> ou <span data-ph="1"></span>. |
| **Tipo de resposta** | Sim. | O formato em que a resposta da URL do Token será recebida — <span data-ph="0"></span>, <span data-ph="1"></span>, ou <span data-ph="2"></span>. |
| **Acesso ao campo de itens** | Opcional | O nome do campo na resposta que contém o token de acesso. O sistema irá extrair o token de acesso deste campo para autenticar futuras solicitações. |
| **Atualizar o campo do item** | Opcional | O nome do campo na resposta que contém o token de atualização. O token de atualização é usado para obter um novo token de acesso quando o atual expira. Este campo é opcional dependendo da implementação do fornecedor. |

---

## Carga útil

Esta secção permite ao administrador definir **pares de valor-chave adicionais** que tem de ser enviado juntamente com o pedido de token.

| Campo | Designação das mercadorias |
|-------|-------------|
| **CHAVE** | O nome do parâmetro a incluir no pedido. |
| **VALOR** | O valor do parâmetro a ser incluído no pedido. |
| **TIPO DE PARÂMICO** | Especifica o tipo de parâmetro. Tipos de parâmetros comuns incluem <span data-ph="0"></span>, <span data-ph="1"></span>, etc. |

!!! example
    - **CHAVE**: <span data-ph="0"></span>
    - **VALOR**: <span data-ph="0"></span>
    - **TIPO DE PARÂMICO**: <span data-ph="0"></span> *(indicando que este parâmetro será incluído no corpo do pedido do token)*

Esta configuração ajuda na configuração **Autenticação OAuth** para acessar APIs automatizando o processo de obtenção e refrescante tokens.

---

## Como Funciona

1. Quando uma mensagem precisa ser enviada através de um Gateway HTTP que usa **OAuth 2.0**, Power SMPP primeiro verifica se um token de acesso válido (não expirado) já está em cache.
2. Se existir um token válido, ele é anexado à chamada API de saída (tipicamente através de um <span data-ph="0"></span> cabeçalho).
3. Se não existir nenhum token válido — ou o token tiver expirado e o configurado **Código de expiração do item** é devolvido pelo gateway — Power SMPP chama **URL do Token** com o configurado <span data-ph="0"></span>, <span data-ph="1"></span>, e <span data-ph="2"></span> pares.
4. A resposta é analisada utilizando o **Tipo de resposta**, **Acesso ao campo de itens** é extraído, e o item está em cache durante a duração de **Tempo de expiração**.
5. Os pedidos de mensagens de saída agora usam o token recém-obtido até que expire novamente.

---

## Ligando o OAuth Handler a um Gateway HTTP

Após salvar o OAuth Handler:

1. Abra o Gateway HTTP que deseja proteger com OAuth.
2. Embaixo **Secção 1: Credenciais necessários**, conjunto **autenticação** para **OAuth 2.0**.
3. Da **OAuth Handler** dropdown, escolha o manipulador que você acabou de criar.
4. Salvem o portal.

O Gateway HTTP agora usará o Manipulador OAuth configurado para obter e atualizar tokens automaticamente — não é necessária rotação manual do token.

!!! tip
 Manter a **Tempo de expiração** ligeiramente menor do que o valor anunciado pelo vendedor (por exemplo, definir <span data-ph="0"></span> minutos se as fichas do vendedor durarem <span data-ph="1"></span> minutos). Isto evita condições de corrida em que o primeiro pedido após a expiração falha antes da atualização ser acionada.
