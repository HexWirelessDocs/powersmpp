
## Regras de Normalização OA/DA no iTextPRO

![OA/DA Normalization](images/oada1.png)

**OA (Endereço de Origem)** e **DA (endereço de destino)** Normalização no iTextPRO permite conteúdo de mensagens, remetente (fonte) e endereços de destinatários de **Terminado móvel (MT)** mensagens a serem automaticamente ajustadas com base em regras predefinidas.

Este recurso é crucial quando se trabalha com diferentes fornecedores ou gateways de telecomunicações que podem seguir diferentes protocolos ou requisitos de formatação.

---

### Objetivo
Normalizar **originador (OA)** e **destino (DA)** Endereços para:
- Conheça **orientações regulamentares**
- Realização **requisitos específicos de formatação de negócios ou fornecedores**

---

### 2. iTextPRO motor OA/DA
iTextPRO inclui um embutido **Motor de normalização OA/DA** que opera ao lado do motor de roteamento. 
Permite modificações dinâmicas de **PDU (Unidade de Dados do Protocolo)** cabeçalhos para entrega de mensagens sem problemas e conformidade.

---

### 3. Exemplo do Mundo Real

#### Mensagem Original Enviada:
- **ID do remetente**: <span data-ph="0"></span> 
- **Mensagem**: 
 <span data-ph="0"></span>

#### Mensagem após a regra OA/DA aplicada:
- **ID do remetente**: <span data-ph="0"></span> 
- **Mensagem Modificada**: 
 <span data-ph="0"></span>

Esta transformação é tratada automaticamente pelas regras de normalização OA/DA definidas no iTextPRO.

---

### 4. Nota em Caracteres Unicode

- Para **Unicode** mensagens: Limite máximo de caracteres = **70 caracteres**
- Para **Inglês (GSM)** mensagens: Limite máximo de caracteres = **160 caracteres**

Se uma mensagem exceder estes limites, o sistema **aparar automaticamente** os caracteres adicionais para permanecer dentro de restrições de codificação SMS.

---

### 5. Etapas de implementação

Para aplicar a normalização OA/DA:

1. **Criar novas regras de OA/DA** no painel de configuração.
2. Defina a lógica de transformação:
   - Modificar o ID do remetente
   - Reescrever o conteúdo da mensagem
   - Ajustar a formatação do número de destino
3. Atribuir as regras aos gateways ou fontes de tráfego relevantes.

---

### 6. Principais benefícios

- □ Interoperabilidade do fornecedor sem costura
- □ Cumprimento das normas de telecomunicações ou regulamentares
- □ Saneamento ou reescrita de conteúdo automático
- • Personalização do ID do remetente e conteúdo de mensagens

---

**Normalização OA/DA** no iTextPRO oferece um poderoso mecanismo para a formatação e conformidade de mensagens, permitindo o roteamento de mensagens que é tecnicamente robusto e amigável à regulação.
