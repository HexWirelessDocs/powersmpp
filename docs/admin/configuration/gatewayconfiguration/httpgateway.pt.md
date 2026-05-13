---
tags:
  - HTTP
  - Gateway
  - Configuration
---

# Gateway HTTP

In **Potência SMPP**, apoiamos ambos **SMPP** e **HTTP** protocolos para conectividade de fornecedores. Consequentemente, o administrador tem a opção de configurar um gateway baseado em SMPP ou um gateway HTTP. Este documento fornece uma visão concisa da configuração do gateway HTTP. Ele foi projetado para ajudar os administradores a entender e configurar um gateway HTTP dentro do aplicativo Power SMPP com facilidade.

Como o nome sugere, o gateway HTTP é baseado no **Protocolo de Transferência de Hipertexto (HTTP)**Este protocolo permite aos clientes enviar mensagens através de uma API que atua como um gateway dentro da aplicação Power SMPP.

![Manage Gateway list view](images/httpgw-01-manage-gateway.png)

**Navegação:** <span data-ph="0"></span> □ <span data-ph="1"></span> □ <span data-ph="2"></span> □ <span data-ph="3"></span> □ <span data-ph="4"></span>.

![HTTP Gateway Detail sections](images/httpgw-02-detail-sections.png)

!!! tip "Ver Documentação"
 Ao clicar em **Adicionar um Novo**, a primeira opção será **Ver Documentação**. Recomendamos que o administrador reveja este documento para se familiarizar com os termos mencionados na configuração do gateway.

A tela HTTP Gateway Detail é organizada nas seguintes seções:

- Credenciais Obrigatórios
- Tipos de Mensagens
- Parâmetros
- Parâmetros Condicionais
- Propriedades do Portal
- Propriedades da Resposta
- Sessão
- Entrega automática de mensagens

---

## Secção 1: Credenciais necessários

Nesta secção, são necessárias várias informações, tais como: **Nome do Portal**, **Tipo de Pedido**, **autenticação**, **URL base**, e **UDH**.

**Nome do Portal** — Um nome fácil de recordar para o portal HTTP.

**A UDH é necessária?** — precisar se o **UDH (Cabeçalho de Dados do Usuário)** é necessário para as mensagens enviadas deste portal. UDH é usado para mensagens concatenadas.

**Tipo de Pedido** — Especifica o tipo de pedido HTTP. Pode ser. **HTTP simples**, **REST/JSON**, ou **SOAP**. Diferentes tipos de solicitação requerem configurações diferentes. Geralmente, HTTP simples é usado para <span data-ph="0"></span> métodos, enquanto REST/JSON pode ser usado para ambos <span data-ph="1"></span> e <span data-ph="2"></span> métodos.

![Required Credentials form](images/httpgw-03-required-credentials.png)

**Detalhe do URL base** — Especifica a URL base da API HTTP, **excluindo** todos os outros parâmetros.

!!! example
 Se o URL da API for <span data-ph="0"></span>, então o URL base deve ser configurado como <span data-ph="1"></span>.

**autenticação** — Power SMPP apoia actualmente três tipos de autorização:

| # # | Tipo | Designação das mercadorias |
|---|------|-------------|
| 1 | **Sem Auth** | Não é necessária autorização. |
| 2 | **Auth Básico** | Um nome de usuário e senha são necessários para autenticação segura da API. |
| 3 | **OAuth 2.0** | A versão mais recente da autorização, usada para regenerar novas credenciais após um certo período para manter a alta segurança da API usando o **OAuth Handler** API. |

![Authentication options](images/httpgw-04-authentication.png)

---

## Secção 2: Tipos de Mensagens

**Tipo de mensagem** é uma seção opcional onde o administrador pode configurar o valor da codificação de dados aceito pelo vendedor. Os valores padrão para cada tipo de codificação de dados são mencionados entre parênteses.

| Tipo | Padrão | Objecto |
|------|---------|---------|
| **TEXTO** | <span data-ph="0"></span> | Mapeando o tipo de mensagem específica do gateway para mensagens de texto simples. |
| **UNICODE** | <span data-ph="0"></span> | Mapeando o tipo de mensagem específica do gateway para mensagens Unicode. |
| **BINÁRIO** | <span data-ph="0"></span> | Mapeando o tipo de mensagem específica do gateway para mensagens binárias. |
| **FLASH** | <span data-ph="0"></span> ou <span data-ph="1"></span> | Mapeando o tipo de mensagem específica do gateway para mensagens flash. |

!!! note
 Mapeie seus tipos de mensagens específicas do gateway com tipos de mensagens do sistema. Deixar os campos em branco se não for aplicável.

![Message Types form](images/httpgw-05-message-types.png)

---

## Secção 3: Parâmetros

A **Parâmetro** a seção permite que o administrador configure os detalhes do gateway e os parâmetros de solicitação fornecidos pelo fornecedor do gateway. Esses parâmetros são usados pelo Power SMPP para construir e transmitir os dados/corpo de solicitação da API para o respectivo fornecedor de gateway para processamento e entrega de mensagens.

Os parâmetros configurados definem como a solicitação HTTP será gerada e executada durante a comunicação API.

### Método

O Power SMPP suporta os seguintes métodos HTTP para execução da API:

#### 1] Método de obtenção

O método GET permite que o administrador configure os parâmetros de solicitação em **par valor-chave** formato. Durante a execução da API, todos os parâmetros configurados são adicionados diretamente ao URL como **parâmetros da pesquisa**.

Este método é geralmente utilizado para:

- Pedidos de API simples
- Transmissão de parâmetros baseada em URL
- Integração de API leve
- Integrações HTTP Legacy

!!! example
 <span data-ph="0"></span>

No método GET, o Power SMPP suporta os seguintes tipos de parâmetros:

##### Nome do pai

A **Nome do pai** campo é usado principalmente para **Baseada em SOAP** Integrações API onde os parâmetros precisam ser agrupados sob um nó XML pai ou objeto de solicitação.

Esta configuração ajuda na geração de cargas de pedido SOAP estruturadas conforme a especificação API do fornecedor.

!!! example
    ```xml
    <SendSMS>
        <username>admin</username>
        <password>test123</password>
    </SendSMS>
    ```
 No exemplo acima, <span data-ph="0"></span> age como o Nome do Pai.

##### Parâmetro do Cabeçalho

A **Parâmetro do Cabeçalho** a seção é usada para configurar os valores de cabeçalho HTTP necessários durante a execução da API.

Estes parâmetros são geralmente utilizados para:

- Tokens de autenticação
- Chaves de API
- Credenciais de Autorização
- Definições do tipo de conteúdo
- Cabeçalhos Personalizados do Fornecedor

!!! example
    ```
    Authorization: Bearer xxxxx
    Content-Type: application/json
    ```

Parâmetros de cabeçalho são transmitidos dentro do cabeçalho de solicitação HTTP durante a comunicação API.

##### Parâmetro do Corpo

A **Parâmetro do Corpo** a seção contém todos os parâmetros gerais de solicitação necessários para a solicitação de API HTTP.

Estes parâmetros incluem tipicamente:

- Número Móvel
- Conteúdo da mensagem
- ID do remetente
- ID do modelo
- ID da entidade
- Parâmetros de Roteamento
- Parâmetros Personalizados do Fornecedor

Para **GET** requisições, estes parâmetros são adicionados dentro da URL da requisição como parâmetros de consulta durante a execução da API.

![Parameters configuration with example rows](images/httpgw-06-parameters.png)

#### 2] Método POST

A **POSTO** método permite que o administrador configure o gateway enviando todos os parâmetros de requisição necessários dentro do **organismo de solicitação** em vez de anexá-los no URL. Este método é recomendado para integrações de APIs onde grandes quantidades de dados, parâmetros de autenticação, cabeçalhos, tokens ou estruturas de carga são necessários.

O uso do método POST oferece as seguintes vantagens:

- Reduz o comprimento e complexidade da URL.
- Melhora a segurança evitando a exposição de informações sensíveis na URL.
- Suporta dados estruturados e de grande carga útil.
- Permite compatibilidade com integrações avançadas da API.
- Permite formatação flexível do corpo de solicitação com base nos requisitos da API.

A carga útil configurada é transmitida no corpo de solicitação HTTP durante a execução da API.

##### Tipo de carga útil

Ao selecionar o método POST, o administrador pode configurar a carga útil da solicitação usando um dos seguintes tipos de carga útil:

###### I] Parâmetro de valor-chave [DADOS DO FORM

Esta opção permite ao administrador configurar a carga útil da solicitação em um padrão **parâmetro de valor-chave** formato, onde cada parâmetro é definido separadamente usando um nome de campo e valor correspondente.

Este tipo de carga útil é adequado para APIs que aceitam:

- Dados do Formulário
- Parâmetros codificados por URL
- Órgãos de pedido estruturados simples

!!! example
    ```
    Key        Value
    username   admin
    password   test123
    senderid   ABCDEF
    ```

**Benefícios:**

- Fácil de configurar e gerenciar.
- Adequado para simples integrações de API.
- Permite o mapeamento dinâmico de parâmetros.
- Simplifica validação de pedidos e solução de problemas.

![POST Form Data Key-Value parameters](images/httpgw-07-post-form-data.png)

###### II] Carga útil RAW

Esta opção permite ao administrador passar o **organismo de pedido completo** diretamente como conteúdo bruto sem definir parâmetros individuais de valor-chave separadamente.

O método RAW Payload é usado principalmente quando a API alvo requer:

- Carga útil do JSON
- Carregamento em XML
- Carregamento de Texto Simples
- Dados Estruturados Personalizados

O administrador pode colar diretamente ou configurar o conteúdo completo da carga útil exatamente como exigido pela API de destino.

**Formatos de carga RAW suportados:** <span data-ph="0"></span>, <span data-ph="1"></span>, <span data-ph="2"></span>.

!!! example "Carga útil do JSON"
    ```json
    {
      "username": "admin",
      "password": "test123",
      "senderid": "ABCDEF"
    }
    ```

**Benefícios:**

- Suporta estruturas de carga útil complexas e aninhadas.
- Permite uma integração perfeita com APIs REST modernas.
- Fornece flexibilidade para formatos personalizados de pedido de API.
- Permite o controle direto sobre a estrutura de carga e formatação.

![RAW JSON payload editor](images/httpgw-08-raw-payload.png)

No Power SMPP, o administrador pode definir **placeholders** para vários valores, tais como <span data-ph="0"></span> para o ID do remetente, <span data-ph="1"></span> para o conteúdo do texto, <span data-ph="2"></span> para o destino, e muitos mais. Isto permite ao administrador configurar vários valores dinâmicos para os parâmetros. Além disso, o administrador pode alterar o tipo de parâmetro, se é um **Cabeçalho** ou a **Corpo** parâmetro, enquanto configura os valores.

---

## Secção 4: Parâmetros Condicionais

Na secção de **Parâmetros Condicionais**, a aplicação tem um recurso para alterar qualquer um dos valores do parâmetro configurado configurando uma condição.

![Conditional Parameters](images/httpgw-09-conditional-parameters.png)

A construção de parâmetros condicionais é feita conforme a seguinte lógica:

> Se <span data-ph="0"></span> com o selecionado <span data-ph="1"></span> corresponde à <span data-ph="2"></span>, então <span data-ph="3"></span> será alterado para <span data-ph="4"></span>.

| Campo | Designação das mercadorias |
|-------|-------------|
| **Parâmetro** | O parâmetro chave da lista de carga útil em que a condição deve ser aplicada. |
| **Condição** | O tipo de condição a ser verificada. |
| **Valor do parâmetro atual** | O valor do parâmetro selecionado a ser comparado na condição. |
| **Parâmetro a ser modificado** | O parâmetro chave da lista de carga útil cujo valor será alterado se a condição acima for satisfeita. |
| **Valor do Parâmetro Modificado** | O novo valor a ser atribuído ao parâmetro chave se a condição for cumprida. |

---

## Secção 5: Propriedades do portal

**Configuração das Propriedades do Gateway** permite que o administrador configure o método e tipo de resposta suportados pelo fornecedor para a operação perfeita do gateway HTTP.

| Propriedade | Designação das mercadorias |
|----------|-------------|
| **Método** | Especifica o método de envio de requisições para o gateway HTTP. O administrador pode configurar o método suportado pelo fornecedor: <span data-ph="0"></span>, <span data-ph="1"></span>, ou <span data-ph="2"></span>. |
| **Tipo de resposta** | O formato em que a resposta deve ser recebida do gateway: <span data-ph="0"></span>, <span data-ph="1"></span>, ou <span data-ph="2"></span>. |
| **Parar o Preço de Perda** | Usado como o preço padrão para o gateway ao rotear mensagens usando **Roteamento Cego**. |
| **É o Roteamento Cego?** | Permite que as mensagens sejam roteadas mesmo que o Gateway Cost Price não esteja configurado para o país e a rede. Nestes casos, o **Parar o Preço de Perda** será aplicado. |
| **Zona horária do portal** | Configure o fuso horário de operação do fornecedor na aplicação para garantir que **Recibo de entrega (DLR)** os tempos de atualização são gravados com precisão. |
| **Está ativo?** | Activa ou desactiva a 'gateway'. |
| **Gateway Abrir / Fechar Tempo** | Janela de tempo operacional para o gateway em <span data-ph="0"></span> formato. |

![Gateway Properties — Method](images/httpgw-10-gateway-properties-method.png)

![Gateway Properties — Response Type](images/httpgw-11-gateway-properties-response.png)

---

## Secção 6: Propriedades da resposta

A **Propriedades da Resposta** no pedido são utilizados para **mapear a resposta** recebido do fornecedor de gateway para os relatórios, que são então usados para atualização **Receitas de entrega (DLRs)**.

Abaixo estão os tipos de configuração de resposta disponíveis na aplicação:

### 1] JSON ou XML

Se o fornecedor suporta o tipo de resposta como **JSON** ou **XML**, a configuração de resposta pode ser configurada com os seguintes campos:

| Campo | Designação das mercadorias |
|-------|-------------|
| **Campo de Código de Erros** | O campo onde o código de erro está localizado na resposta. |
| **Campo ID da Mensagem** | O campo onde o ID da mensagem está localizado na resposta. |
| **Campo de Estado da Mensagem** | O campo onde o estado da mensagem está localizado na resposta. |
| **Campo de Números Móveis** | O campo que contém o número de telemóvel na resposta. |

![Response Properties — JSON / XML](images/httpgw-12-response-properties-json.png)

### 2] TEXTO

Se o fornecedor suporta o tipo de resposta como **TEXTO**, o administrador precisa configurar parâmetros adicionais sob Propriedades de Resposta:

| Campo | Designação das mercadorias |
|-------|-------------|
| **Separador de valor de chave** | O delimitador utilizado para separar e identificar pares de valor-chave da resposta. Este campo é usado apenas para o tipo de resposta TEXT. Por exemplo, se a resposta recebida for <span data-ph="0"></span>, então o divisor seria <span data-ph="1"></span>. |
| **Divisor de propriedades** | O delimitador usado para separar várias propriedades na resposta. Este campo também é específico para o tipo de resposta TEXT. |
| **Campo de Código de Erros** | Indica o campo onde o código de erro está localizado na resposta. |
| **Campo ID da Mensagem** | Indica o campo onde o ID da mensagem está localizado na resposta. |
| **Campo de Estado da Mensagem** | Indica o campo onde o estado da mensagem está localizado na resposta. |
| **Campo de Números Móveis** | Usado para obter o número de telemóvel da resposta. O administrador precisa especificar o campo que contém o número móvel na resposta. |

![Response Properties — TEXT](images/httpgw-13-response-properties-text.png)

!!! note
 Na configuração de resposta, o administrador deve configurar os nomes dos parâmetros que armazenam os valores dos campos mencionados acima.

!!! example
 Considere a seguinte resposta:
    ```json
    { "data": [{
        "message_error_code": 0,
        "message_error_description": "Success",
        "mobile_number": "9174XXXXXXX",
        "message_id": "b349f1c2-5ae9-4076-867e-5fa15044b207"
    }]}
    ```
 Nesta resposta JSON:

    - A **Campo de Código de Erros** irá conter o nome do parâmetro <span data-ph="0"></span>.
    - A **Campo ID da Mensagem** irá conter o nome do parâmetro <span data-ph="0"></span>.

Ao configurar propriedades de resposta para uma **TEXTO** resposta, os valores serão semelhantes. Além disso, você precisa especificar o seguinte:

- **Separador de valor de chave** — na resposta, o valor de <span data-ph="0"></span> é <span data-ph="1"></span>. O separador Key-Value é o delimitador usado para separar a chave do valor, que neste caso é um cólon (<span data-ph="2"></span>). Então, o chave-valor seria <span data-ph="3"></span>.
- **Divisor de propriedades** — Na resposta, parâmetros como <span data-ph="0"></span> e <span data-ph="1"></span> são separados por uma vírgula (<span data-ph="2"></span>). Por conseguinte, o separador de propriedades para separar estes parâmetros seria <span data-ph="3"></span>.

Esta configuração ajuda a mapear e extrair os campos necessários da resposta, independentemente de o tipo de resposta ser JSON, XML ou TEXT.

---

## Secção 7: Sessão

A **sessão** indica o número de conexões, e a sessão recomendada para um gateway HTTP é **1**.

| Campo | Valor recomendado |
|-------|-------------------|
| **No de Sessões** | <span data-ph="0"></span> |

![Session configuration](images/httpgw-14-session.png)

---

## Secção 8: Entrega automática de mensagens

Se o fornecedor de gateway não enviar **Receitas de entrega (DLRs)**, a configuração do gateway HTTP inclui um recurso chamado **Entrega automática**Este recurso permite ao administrador configurar um estado para que as DLRs sejam atualizadas automaticamente.

| Campo | Designação das mercadorias |
|-------|-------------|
| **Está automaticamente marcado como entregue?** | Atualiza o status de entrega de mensagens mesmo que um DLR não seja recebido do fornecedor de gateway. Neste caso, **Estado padrão do DLR** será usado. |
| **Estado padrão do DLR** | O estado de entrega por omissão atribuído às mensagens se o recurso de entrega automática for activado. É usado quando o sistema precisa marcar mensagens como entregues na ausência de uma DLR do gateway. Opções: <span data-ph="0"></span>, <span data-ph="1"></span>, <span data-ph="2"></span>, <span data-ph="3"></span>. |

![Automatic Message Delivery](images/httpgw-15-automatic-delivery.png)

!!! info "Útil para gateways que não emitem DLRs"
 Ativar entrega automática apenas quando o fornecedor upstream realmente nunca retorna um DLR. Caso contrário, deixe-o desativado para que DLRs reais do fornecedor conduzir o relatório.
