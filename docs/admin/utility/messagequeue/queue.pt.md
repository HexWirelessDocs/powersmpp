
# Utilitário – Transferência de Fila para Fila

A **Transferência da Fila- para- Fila** O recurso no iTextPro permite uma transferência perfeita do tráfego SMS entre gateways, garantindo um gerenciamento eficiente das operações de mensagens. 
Esta funcionalidade é particularmente útil quando o seu **gateway primário** experimenta o tempo de inatividade ou torna-se não-funcional. Usando esta opção, você pode **redirecionar tráfego para um gateway alternativo**, assegurando uma comunicação ininterrupta.

![Queue-to-Queue Overview](../images/queue1.png)

---

## Configuração da Transferência

### 1. Finalidade da Transferência
Especifique o propósito ou motivo para transferir o tráfego SMS. 
Isto ajuda a manter **registos claros** e fornece contexto para a transferência.

### 2. Gateway de origem
Selecione o **gateway de origem** das quais as mensagens serão transferidas. 
iTextPro permite que você escolha o **fila de mensagens específica** associado a este portal.

### 3. Portão de Destino
Escolha o **gateway de destino** onde devem ser enviadas mensagens. 
Isto garante que o tráfego seja redireccionado para o objectivo operacional correcto.

### 4. Iniciando a transferência
Uma vez definidos os parâmetros de transferência:
- Clique na **"Adicionar trabalho"** Botão.
- O iTextPro adicionará o trabalho à fila de transferência.
- O sistema irá transferir automaticamente as mensagens dos seleccionados **gateway de origem** à **gateway de destino**.

Este processo contínuo garante **continuidade dos serviços SMS** mesmo em caso de interrupções de porta de entrada.

![Queue Transfer Execution](../images/queue2.png)
