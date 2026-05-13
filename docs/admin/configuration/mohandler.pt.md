---
tags:
  - HTTP
  - MO
  - Handler
  - Configuration
---

# HTTP MO Handler

## Visão geral

A **HTTP MO Handler** no iTextPro é usado para receber e processar entrada **MO (Mobile Originado)** mensagens de operadores de telecomunicações ou fornecedores de gateway. O manipulador atua como um endpoint API que aceita solicitações de MO e encaminha os dados recebidos para a plataforma para posterior roteamento e processamento.

A configuração HTTP MO Handler define:

- Método de comunicação
- Detalhes do canal
- Mapeamento de carga útil
- Restrições de segurança
- Geração de pontos finais

!!! warning "Pré-requisito"
 Esta configuração é **obrigatório** antes de criar regras de roteamento MO.

---

## Caminho de navegação

<span data-ph="0"></span> □ <span data-ph="1"></span> □ <span data-ph="2"></span>.

![Manage MO Handler list](images/mohandler-01-list.png)

---

## Parâmetros de Configuração do Manipulador

Os seguintes parâmetros devem ser configurados ao criar um HTTP MO Handler.

### 1] Nome do manipulador

A **Nome do manipulador** é usado para identificar exclusivamente a configuração MO Handler dentro da plataforma.

Este nome é usado internamente para:

- Configuração da rota
- Seleção do manipulador
- Mapa de tráfego MO
- Administração e resolução de problemas

!!! example
    ```
    MO_HANDLER_INDIA_01
    ```

---

### 2] Tipo de canal

A **Tipo de Canal** define o tipo de número de telecomunicações associado ao tráfego de entrada MO.

**Tipos de canais suportados:**

| Tipo | Designação das mercadorias |
|------|-------------|
| **Código Longo** | Um número móvel padrão usado para comunicação de mensagens bidirecionais. |
| **Código Curto** | Um código numérico curto geralmente usado para campanhas empresariais, sistemas de votação, assinaturas, ou serviços promocionais. |

O tipo de canal seleccionado deve corresponder à configuração do operador ou do fornecedor.

![Manage MO Handler — full configuration form](images/mohandler-02-add-new.png)

---

### 3] Número do canal

A **Número de Canal** representa o número de destino real em que o tráfego MO será recebido.

!!! example
    ```
    567890
    ```

Este número deve ser configurado **exactamente como previsto** pelo operador de telecomunicações ou fornecedor de gateway.

---

### 4] Endpoint local

A **Endpoint Local** é gerado automaticamente pelo iTextPro uma vez que a configuração do manipulador é criada.

Este endpoint atua como o URL de recepção para solicitações HTTP MO recebidas.

O URL de endpoint gerado é geralmente compartilhado com:

- Vendedores de Gateway SMS
- Operadores de Telecom
- Agregadores
- Plataformas de terceiros

O fornecedor usa este endpoint para empurrar mensagens MO recebidas para a plataforma iTextPro.

**Fluxo de Exemplo:**

```
Operator/Vendor → Local Endpoint → iTextPro Processing
```

---

### 5] Whitelist IP

A **Whitelist IP** a secção é usada para assegurar o ponto final do MO, restringindo o acesso apenas aos endereços IP autorizados.

Apenas os pedidos recebidos de endereços IP configurados serão aceitos pela plataforma.

**Objectivo:**

- Impedir o acesso não autorizado
- Melhorar a segurança da API
- Restrinja o tráfego desconhecido
- Proteger o objectivo MO contra a utilização abusiva

!!! example
    ```
    192.168.10.20
    ```

!!! tip
 Vários IPs podem ser configurados conforme os requisitos operacionais.

---

### 6] Método

A **Método** define o método de comunicação HTTP usado pelo fornecedor durante o envio de solicitações de MO.

**Métodos suportados:** <span data-ph="0"></span>, <span data-ph="1"></span>.

#### Método GET

No método GET:

- Os parâmetros são transmitidos dentro do URL.
- Os dados são enviados como parâmetros de consulta.
- Adequado para integrações leves.

!!! example
    ```
    https://domain.com/mo?originator=9876543210&destination=567890&message=TEST
    ```

#### Método POST

No método POST:

- Parâmetros são transmitidos dentro do corpo de solicitação HTTP.
- Suporta cargas estruturadas e maiores.
- Comumente usado para integrações de API modernas.

**Benefícios:**

- Melhor segurança
- Estrutura de solicitação mais limpa
- Suporta cargas JSON / XML
- Adequado para integrações complexas

---

## Configuração da carga útil

A **Carga útil** a seção define como os parâmetros de pedidos recebidos serão mapeados no iTextPro.

O mapeamento correto da carga útil é **obrigatório** para processamento de MO bem sucedido. Configurar os parâmetros de carga útil exatamente como mencionado abaixo:

| Parâmetro da Plataforma | Parâmetro do Fornecedor |
|--------------------|------------------|
| **Originador** | <span data-ph="0"></span> |
| **Destino** | <span data-ph="0"></span> |
| **Mensagem** | <span data-ph="0"></span> |

### Descrição do Parâmetro de Carga

#### Originador

A **Originador** parâmetro representa o número do remetente do qual a mensagem MO é recebida.

!!! example
    ```
    9876543210
    ```

#### Destino

A **Destino** parâmetro representa o **Código Curto** ou **Código Longo** número em que a mensagem MO foi enviada.

!!! example
    ```
    567890
    ```

#### Mensagem

A **Mensagem** parâmetro representa o conteúdo de texto real enviado pelo usuário final.

!!! example
    ```
    ASKRK BALANCE
    ```

---

## Salvar configuração do manipulador

Após completar todas as configurações:

1. Verificar todos os detalhes configurados.
2. Clique em **Gravar**.

O HTTP MO Handler agora está configurado com sucesso e pronto para receber o tráfego MO.

!!! tip "Próxima Etapa"
 Uma vez que o manipulador é salvo, prossiga para criar um **Regra de roteamento MO** para definir como o tráfego MO de entrada será filtrado e entregue aos usuários finais.
