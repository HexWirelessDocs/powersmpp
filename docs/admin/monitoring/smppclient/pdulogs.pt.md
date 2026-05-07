---
tags:
  - Monitoring
  - PDU
  - Troubleshooting
---

# Acompanhamento

iTextPRO fornece abrangente **ferramentas de monitorização** para garantir o desempenho ótimo de entrega de SMS e estabilidade do sistema. Isto inclui **Monitorização ao vivo em tempo real** para insights de tráfego e um robusto **Registrador PDU** para análise profunda do nível das mensagens.

---

## Monitorização ao vivo

A **Monitorização ao vivo** módulo em iTextPRO rastreia dinamicamente e analisa os principais pontos de dados relacionados ao tráfego SMS, habilitando **tomada de decisão em tempo real** para roteamento e otimização de desempenho.

### Principais Benefícios
- **Gestão Proativa do Tráfego** – Gerenciar tráfego de SMS dinamicamente com base em dados ao vivo.
- **Roteamento otimizado** – Fazer decisões de roteamento informadas para melhorar as taxas de entrega.
- **Alocação eficiente de recursos** – Alocar recursos estrategicamente durante as horas de pico.
- **Desempenho Melhorado** – Melhore a capacidade de resposta e rendimento com insights em tempo real.

**Em resumo**, Live Monitoring garante que os usuários têm **visibilidade atualizada** em fluxo de tráfego SMS, especialmente durante períodos de alta demanda.

---

## Registos PDU

iTextPRO emprega uma **Registrador PDU (Unidade de Dados do Protocolo)** capturar e registrar todas as mensagens que entram ou saem do SMSC. Esta ferramenta é vital para **resolução de problemas**, **monitorização**, e **manutenção** saúde do sistema.

### Características Principais
- **Viagem de Mensagem em Tempo Real** – Registra cada mensagem em tempo real para análise imediata.
- **Capacidades de filtragem** – Rastreie a jornada de uma mensagem com um clique.
- **Suporte ao Tipo de PDU** – Inspecione SubmitSM, DeliverSM, Bind, Unbind e muito mais.
- **Visibilidade e retenção** – Os logs seguem o **fuso horário de administração** e são mantidos para **3 dias**.
- **Inspeção de tráfego a montante** – Ver fluxo de mensagens selecionando gateways de uma lista suspensa.
- **Suporte de Resolução de Problemas** – Diagnóstico rápido da entrega ou problemas de sessão SMPP.

![PDU Logs](images/pdulogs1.png)

### Orientações de Utilização
1. Acesso **Registrador PDU** da interface iTextPRO.
2. Aplicar **filtros** isolar e inspecionar mensagens específicas.
3. Utilização **Registos de tráfego a montante** verificar as viagens de mensagens.
4. Executar **monitorização regular** manter a fiabilidade do sistema.

---

## Níveis de verbosidade no registro de PDU

O registro de PDU do iTextPRO suporta múltiplos **níveis de verbosidade**, fornecendo informações detalhadas sobre comunicação entre gateways iTextPRO e SMPP.

| Nível de Verbosidade | Objecto | Acção |
|-----------------|---------|--------|
| **Pedido de Ligação** | Iniciar ligação SMPP | iTextPRO envia uma solicitação para se conectar ao gateway SMPP |
| **Resposta à Ligação** | Confirma a ligação ao SMPP | O gateway SMPP responde ao pedido de vinculação |
| **Perguntar Pedido de Ligação / Resposta** | Exame de saúde da sessão de SMPP | iTextPRO envia solicitação a cada 30s; gateway responde |
| **Enviar SM Pedido** | Pedido de envio de mensagens | iTextPRO envia um SMS para o gateway SMPP |
| **Resposta de Enviar SM** | Aviso de apresentação | Gateway responde à submissão de mensagens |
| **Entregar  SM Pedido** | Recepção do relatório de entrega (DLR) | O gateway SMPP envia o status de entrega |
| **Entregar  SM Resposta** | Agradecimento da DLR | iTextPRO confirma recepção de DLR |
| **Pedido Desvinculado** | Terminação da sessão | iTextPRO ou gateway inicia pedido unbind |

**Importância:** Estes logs dão aos administradores uma **visualização granular dos fluxos de mensagens**, ajudando a detectar, diagnosticar e resolver problemas de forma eficiente.

---

Com **Monitorização ao vivo** e **Registo PDU**, iTextPRO habilita os administradores a manter **Sistema de entrega de SMS altamente confiável**, detectar proativamente problemas, e otimizar o tráfego em tempo real.
