
# Registos PDU do Servidor

A **Registos PDU do Servidor SMPP** em iTextPRO são essenciais para **monitorização e resolução de problemas** transacções de mensagens entre a **ESME (Entidade de Mensagem Curta Externa)** e a plataforma iTextPRO. 
Estes logs capturam **tráfego a jusante** e fornecer detalhes granulares que ajudam na resolução eficiente da questão.

---

## Características Principais
- **Registo Integral de Transações** – Grava todas as transações de mensagens entre o usuário ESME e o iTextPRO.
- **Suporte de Resolução de Problemas** – Crítica para diagnosticar e resolver problemas de comunicação.
- **Zona horária da administração** – Os logs são exibidos no fuso horário do administrador para referência precisa.

---

## Tráfego a jusante
Acompanha o **viagem de mensagens** desde o usuário ESME até o iTextPRO, proporcionando visibilidade no fluxo de entrega e status.

![Server PDU Logs](images/pdulogs1.png)

---

## Níveis de Verbosidade

Compreender **níveis de verbosidade** ajuda na monitorização e resolução de problemas:

| **Nível de Verbosidade** | **Designação das mercadorias** | **Objecto** |
|---------------------|-----------------|-------------|
| **Pedido de Ligação** | O usuário do ESME inicia a conexão. | Estabelece conexão com o iTextPRO. |
| **Resposta à Ligação** | iTextPRO responde à solicitação de conexão. | Confirma a conexão do usuário do ESME. |
| **Perguntar o Pedido de Ligação** / **Resposta** | Chamada de verificação de saúde do usuário ESME e correspondente resposta. | Verifica o estado da sessão do iTextPRO (intervalo recomendado: 30 segundos). |
| **Enviar SM Pedido** | O usuário do ESME inicia o pedido de mensagem. | Envia mensagens SMS para o iTextPRO. |
| **Resposta de Enviar SM** | iTextPRO responde ao pedido de mensagem. | Confirma envio de SMS. |
| **Entregar  SM Pedido** | DLR (Relatório de Entrega) recebido pelo iTextPRO para uma mensagem enviada. | Atualiza o status de entrega para SMS enviado. |
| **Entregar  SM Resposta** | Usuário ESME reconhece solicitação DLR. | Confirma o recebimento do status de entrega. |
| **Pedido Desvinculado** | O usuário do ESME inicia a solicitação unbind. | Termina sessões conectadas. |

---

## Melhores Práticas
- **Revise regularmente os registros** – Garante monitoramento robusto e detecção rápida de problemas relacionados à transação.
- **Insights sobre a verbosidade** – Use os detalhes capturados PDU para manter uma comunicação eficaz entre ESME e iTextPRO.
- **Ação Perguntar** – Anomalias de endereço assim que forem detectadas para manter o desempenho ideal do sistema.
