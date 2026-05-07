
## Códigos de Erro do Gateway

![Gateway Error Codes](images/error1.png)

**Códigos de Erro do Gateway** no iTextPRO permite-lhe interpretar e gerir mensagens de resposta a partir do **Centro de Serviços de Mensagens Curtas (SMSC)** quando a mensagem falhar. Este recurso aumenta a visibilidade sobre falhas de entrega e permite rollbacks de crédito com base em códigos de erro específicos.

---

![Configure Error Codes](images/error2.png)

### Resumo
Quando o SMSC não consegue entregar uma mensagem, ele retorna uma **código de erro não- zero** juntamente com um status de mensagem de referência. Estes são referidos como **Códigos de Erro do Gateway**.

### 2. Objetivo
O iTextPRO permite aos administradores configurar e mapear esses códigos de erro. Quando a **Relatório de entrega (DLR)** é recebido, iTextPRO verifica a configuração e:
- Mostra a **etiqueta de erro personalizada**
- Mapa para um **estado padrão de SMPP** 
Esta informação é mostrada em ambos **Administrador** e **Relatórios do Utilizador**, melhorar a transparência.

### 3. Pré-requisitos
Antes da configuração, obter um **Lista de Código de Erros no Portal** do seu SMSC.

---

### 4. Passos de Configuração

#### a. Seleção do portal
Escolha o gateway para o qual você está configurando o código de erro.

#### b. Código de erro
Digite o **Código de erro específico** recebido do seu SMSC.

#### c. Mostrar etiqueta de erro
Inserir o **estado de referência** ou nome da etiqueta do SMSC (por exemplo, <span data-ph="0"></span>, <span data-ph="1"></span>).

#### d. Código de Erro Padrão (Mapped)
Mapear o erro para um dos status padrão de SMPP:
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>

#### e. Descrição do Erro
Fornecer uma **breve descrição** da etiqueta de erro. Isto será mostrado no **Relatórios do Utilizador** ajudar a compreender o estado da entrega.

#### f. Está Ativo
Alternar o código de erro **ligado ou desligado** Se necessário.

#### g. Retorno do Crédito
Habilitar esta opção para **voltar créditos do usuário** automaticamente se uma mensagem falhar com o código de erro mapeado.

---

### 5. Envio em massa

- Utilizar o **Envio em massa** recurso para configurar múltiplos códigos de erro simultaneamente.
- Clique **"Carregamento de Bloco"**, então:
  - **Transferir o Ficheiro de Exemplo**
  - **Mapear cabeçalhos de colunas** no assistente de importação

---

### 6. Submeter
Uma vez configurado, clique em **"Submeter"** para salvar os códigos de erro para o gateway selecionado.

□ **Nota:** 
A configuração adequada do código de erro melhora o monitoramento e permite o rastreamento preciso de **Falhas na entrega de mensagens**, **Acções de retrocesso**, e **Precisão da comunicação**.

---
