
# MO

## Definição
Mensagens MO (**Origem Móvel** mensagens) são iniciadas por usuários de telefone celular e enviadas para códigos de acesso dedicados ou números de código longos usando palavras-chave específicas. 
Eles permitem que clientes ou assinantes interajam diretamente com fornecedores ou aplicativos.

---

## Processo

### Início do Utilizador
Um cliente envia uma mensagem de texto com uma palavra-chave específica para um shortcode dedicado ou código longo.

**Exemplo:** 
<span data-ph="0"></span> → <span data-ph="1"></span>

### Roteamento da Mensagem
A mensagem é encaminhada para o aplicativo ou fornecedor ligado a esse shortcode ou número.

---

## Pontos-chave
- Permite uma comunicação bidirecional entre usuários e fornecedores.
- Usa palavras-chave específicas para desencadear respostas.
- Funciona através de códigos de acesso dedicados ou códigos longos.

---

## Configuração dos manipuladores HTTP MO

### Visão geral
HTTP MO Handlers em **iTextPro** receber mensagens MO recebidas de fornecedores. 
As estruturas de carga útil podem diferir entre fornecedores.

### Passo 1: Adicionar um novo manipulador
1. Clique **Adicionar novo manipulador**.
2. Parâmetros de carga útil do mapa na UI.

![MO Handler Config](images/mo1.png)

**Pré-requisitos:** 
Conhecimento básico das APIs RESTful.

**Exemplo (Vendor: Airtel):**
```json
{
  "originatorAddress": "999563256",
  "destinationAddress": "8754321565",
  "messageContent": "BINGO 101",
  "CustomerId": "669912"
}
```

**Configuração iTextPro:**
- Método: <span data-ph="0"></span>
- Tipo de Conteúdo: <span data-ph="0"></span>
- Chave do Originador: <span data-ph="0"></span>
- Chave de destino: <span data-ph="0"></span>
- Chave da mensagem: <span data-ph="0"></span>

![MO Config 2](images/mo2.png)

---

### Passo 2: Configurar os Serviços MO para a Conta do Usuário
1. Faça login no iTextPro → localize a conta do usuário.
2. Activar **Serviços MO** em **Gerenciar serviços**.
3. Definir & palavra chave do número MO:
   - Data de Fim
   - Selecionar Canal (número MO)
   - Palavra- chave (ou <span data-ph="0"></span> para todos)
   - Estado: Activo
4. Clique **Adicionar**.

![MO Config 3](images/mo3.png) 
![MO Config 4](images/mo4.png)

---

### Passo 3: Configuração da regra de roteamento MO
1. Ir para **Regra de roteamento MO**.
2. Criar ou editar uma regra:
   - Nome da regra, Data de início/ fim
   - Interface de gateway: HTTP/SMPP
   - Condições: Originador, Destino, Mensagem
   - & Ponto final do usuário: HTTP Webhook ou ESME

![MO Routing](images/mo5.png) 
![MO Routing UI](images/mo6.png) 
![MO Routing Rule](images/mo7.png)

---

## Acesso ao Módulo MO
1. Impersonate/Login para conta de usuário.
2. Abrir **Módulo MO** para ver mensagens MO.

![MO Inbox](images/mo8.png) 
![MO Keyword](images/mo9.png) 
![MO Keyword Details](images/mo10.png)

---

## Resposta automática
- Definir respostas automatizadas para mensagens MO.

![MO Auto Reply](images/mo11.png)

---

## Notificação
- **E- mail de encaminhamento** – Receba alertas MO por e-mail. 
- **Encaminhamento Móvel** – Receba alertas via SMS (incluir código do país).

![MO Mobile Notify](images/mo12.png)

---

## Gerir a Sub- Palavra
Sub-palavras são gatilhos secundários após a palavra-chave principal.

**Exemplo:**
- **Palavra chave principal:** CAR 
- **Resposta automática:** 
 <span data-ph="0"></span>
- **Subpalavra 1:** SIM → <span data-ph="0"></span> 
- **Sub- palavra 2:** NÃO → <span data-ph="0"></span>

![MO Sub-keyword](images/mo13.png)

---

## Relatórios
- Exportar relatórios MO para Excel.
- Filtrar por palavras-chave ou sub- palavras-chave.

**Passos:**
1. Ir para **Relatórios**.
2. Clique **Relatório de Exportação**.
3. Baixe e personalize.

![MO Reports](images/mo14.png) 
![MO Reports 2](images/mo15.png)

---

## Mo Webhooks
Entrega de mensagens MO em tempo real para um determinado endpoint HTTP.

**Configuração:**
1. Activar **HTTP Web Push** na conta-mãe.
2. Ir para **Mo Webhooks** → **Adicionar um novo Webhook**.
3. Set:
   - Nome
   - URL do ponto final
   - Método: GET/POST
   - Manipulador: MO

**Nota:** 
Se o ponto final for inacessível, o MO é eliminado. O intervalo é de 10 segundos.

![MO Webhook](images/mo16.png) 
![MO Webhook Config](images/mo17.png)