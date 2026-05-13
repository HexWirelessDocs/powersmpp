---
tags:
  - HTTP
  - DLR
  - Handler
  - Configuration
---

# Configuração do Manipulador DLR HTTP

Uma vez que o Gateway HTTP tenha sido configurado sobre o aplicativo, o usuário poderá enviar mensagens e a resposta será atualizada sobre o aplicativo.

!!! note
 A **Resposta do Portal** é apenas o **1a resposta** que indica se as mensagens foram enviadas ao vendedor com ou sem sucesso.

Para receber o **DLR (Receita de Entrega)** do fornecedor, o administrador precisa configurar um **HTTP DLR Handler** de modo que sempre que o fornecedor enviar o DLR, o DLR será atualizado sobre o aplicativo usando o manipulador DLR.

Neste documento, vamos compartilhar todas as etapas e configurações que precisam ser feitas pelo administrador para receber o DLR corretamente sobre o aplicativo.

---

## Navegação

<span data-ph="0"></span> □ <span data-ph="1"></span> □ <span data-ph="2"></span> □ <span data-ph="3"></span>.

---

## Amostra DLR Payload

Para configurar o gerenciador DLR HTTP, nós exigiríamos o **Formato de resposta DLR** ou uma amostra DLR do fornecedor para que o administrador possa completar a configuração sobre o aplicativo.

Por exemplo, usaremos a amostra DLR abaixo para a Configuração do Manipulador DLR HTTP:

```json
{
    "messageId": "161a9168-623c-4411-9e30-cf69353f9bef",
    "status": "EXPIRED",
    "errorCode": "1039",
    "mobile": "91123537072",
    "shortMessage": "Test Message",
    "doneDate": "2024-05-22 11:07:46"
}
```

---

## Passos de Configuração

Siga os passos abaixo para configurar o manipulador DLR para a amostra DLR fornecida acima:

1. **Adicionar um nome amigável do usuário** Para o encarregado.
2. **Lista em branco o IP do fornecedor** *(Não obrigatório)*.
3. **Selecione o método suportado** pelo vendedor — <span data-ph="0"></span> ou <span data-ph="1"></span>.
4. **Configurar os Carregamentos** — Sob as cargas, o cliente precisa configurar o nome do parâmetro que armazena os valores específicos.

### Referência de mapeamento de campo

| Campo de Aplicação | Mapas para a chave JSON | Valor do Exemplo |
|-------------------|------------------|---------------|
| **MensagemId** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Estado da Mensagem** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Data de conclusão** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Código de Erro** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Número Móvel** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **ID do remetente** | *(opcional, mapa se o vendedor o enviar)* | — |
| **Mensagem** | <span data-ph="0"></span> | <span data-ph="0"></span> |

!!! tip
 No exemplo acima, o parâmetro <span data-ph="0"></span> armazena o valor do estado DLR e <span data-ph="1"></span> armazena o valor do código de erro. Estes parâmetros precisam ser configurados como está em **Estado da Mensagem** e **Código de Erro** respectivamente. Aplicar a mesma lógica para todos os outros parâmetros compartilhados pelo fornecedor.

---

## Endpoint Local

Quando o manipulador é salvo, o Power SMPP gera uma **Endpoint Local** URL (por exemplo, <span data-ph="0"></span>). Este é o URL que o fornecedor irá chamar de volta com cargas DLR.

!!! warning "Importante"
 Uma vez que todos os detalhes foram configurados sobre a aplicação, **salvá-lo e, por favor, entre em contato com o seu fornecedor de gateway e peça-lhes para listarem em branco o Endpoint do manipulador DLR no final**.

---

## Valores por Omissão

Pela **Estado da Mensagem** e **Código de Erro** campos, um opcional <span data-ph="0"></span> pode ser configurado. O valor padrão é aplicado quando o vendedor não retorna esse campo em um DLR específico. Isso garante que o registro DLR ainda está completo e a mensagem é fechada em relatórios.

---

## Verificação

Após configurar o manipulador DLR:

1. Envie uma mensagem de teste através do Gateway HTTP correspondente.
2. Pergunte ao fornecedor (ou use uma ferramenta de teste como <span data-ph="0"></span> / <span data-ph="1"></span>) para enviar uma amostra DLR carga útil para o URL Local Endpoint.
3. Abrir o respectivo **Relatório DLR** em <span data-ph="0"></span> Confirmar que a DLR foi recebida e analisada correctamente.

Se o DLR não aparecer, verifique novamente os mapeamentos do nome do parâmetro — a causa mais comum é um descompasso entre a chave JSON que o fornecedor envia e a chave configurada no manipulador.
