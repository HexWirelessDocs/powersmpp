---
tags:
  - Admin
  - User Management
---

## Administração

**Bem- vindo ao iTextPRO**, seu gateway para gerenciamento eficiente de documentos!

Para começar com o acesso ao site de administração do iTextPRO, você precisará fazer login usando o **URL do administrador** e **credenciais de login** fornecido pela nossa equipa de entrega de serviços.

Uma vez que você tenha logado com sucesso, você será recebido por um **Interface amigável** equipados com vários comandos de navegação. O controle primário de navegação para iniciar sua experiência é **«Administração do Utilizador — Gestão do Utilizador».** Tenha em mente que os controles associados aninhados sob este menu só serão visíveis uma vez que você **inserir um nome de usuário específico** e bater na **'Ver'** Botão.

Para informações detalhadas sobre a funcionalidade da seção Administração, você encontrará **descrições abrangentes** dos diversos controlos nas secções subsequentes deste documento.

---

## Administração do Utilizador

Navegando para o **Gestão do Utilizador** Page é uma brisa. Basta clicar no **«Gestão do Utilizador»** opção, e irá guiá-lo perfeitamente para a página de Gestão do Usuário.

Para continuar, **insira o nome de usuário** você está interessado em dentro da caixa de pesquisa dedicada e bater o **'Ver'** Botão. A caixa de pesquisa **preenche automaticamente os registos correspondentes** em ordem alfabética, tornando sua pesquisa rápida e sem esforço.

![User Management](images/Administration1.png)

---

## Adicionar novo usuário

Mergulhar no processo de expandir sua base de usuários é simples. Basta clicar no **"Adicionar novo usuário"** botão para iniciar a criação de uma nova conta de usuário.

No entanto, para garantir uma configuração abrangente, você precisará fornecer as seguintes informações essenciais.

### **Passo 1: Digite os detalhes do usuário**

Ao clicar no **"Adicionar novo usuário"** botão, iTextPRO irá guiá-lo para uma página dedicada. Preencher o seguinte:

- **Nome próprio**
- **Sobrenome**
- **Endereço**
- **Nome do Utilizador** - Deve ser único.
- **Senha** – No mínimo 8 caracteres, com pelo menos:
  - 1 letra maiúscula
  - 1 letra minúscula
  - 1 carácter numérico
  - 1 carácter especial
- **ID de e- mail** – Usado para alertas de e-mail, incluindo OTPs e e-mails de boas-vindas (com base nas configurações do Admin SMTP).
- **Número Móvel**
- **Fuso horário** – Afeta reportar datas e exibição específica do usuário.
- **Moeda do Usuário** – Exibe apenas propósito; sujeito a conversão em tempo real.
- **Validade da Conta do Usuário**:
  - **Validade Personalizada** – Defina uma data final.
  - **Validade vitalícia** – Sem validade (acesso permanente).
- **Tipo de Conta do Usuário**:
  - **Usuário** – Acesso ao Painel do Usuário.
  - **Revendedor** – Conta em branco com opções de marca e preços.

![Add User Step 1](images/adduser1.png)

---

### **Etapa 2: Detalhes da notificação (Opcional)**

Personalize suas notificações adicionando vários e-mails de stakeholders para alertas como:

- OTPs de login
- Nova Verificação do Usuário
- Atualizações do Plano de Taxa
- Notificações de aprovação

![Add User Step 2](images/adduser2.png)

Ao clicar **"Criar Novo Usuário"**, a **e- mail de boas- vindas** é enviado (requer configuração SMTP). iTextPRO confirma sucesso e apresenta:

- **Vou fazê-lo noutra altura.** – Redireciona para o perfil do novo usuário.
- **Está bem! Vamos fazê-lo** – Lança o **Assistente de Configuração da Conta**.

![Add User Step 3](images/adduser3.png)

---

### **Passo 3: Configuração das configurações do portal**

Escolha o seu método de roteamento:

- **Sim.** – Utilizar **gateway fixo** para todas as mensagens.
- **Não, eu vou adicionar a regra de roteamento mais tarde** - Deixe o **Motor de Roteamento Principal** dinamicamente manusear roteamento.

Você também pode clicar **"Skip"** Prossiga.

![Gateway Settings](images/adduser4.png)
![Routing Option](images/adduser5.png)

---

### **Passo 4: Adicionando créditos SMS**

- **Digite Créditos** – Número de créditos SMS.
- **Salvar alterações**
- **Continuar para o Passo Seguinte**

!!! note
 Todas as transações de crédito estão em **apenas a moeda de base**.

![Credits](images/adduser6.png)

---

### **Passo 5: Escolher a Política de ID do remetente**

Seleccionar de:

- **ID Dinâmico do Sender** – Os usuários podem usar qualquer ID remetente (numérico/alphanumérico).
- **ID do remetente fixo** – Use um ID de remetente predefinido para consistência.

Clique **"Salvar"** para confirmar.

![Sender ID](images/adduser7.png)
![Sender ID Settings](images/adduser8.png)

---

### **Passo 6: Configurar o SMPP Conta para clientes por grosso**

Para criar uma conta SMPP:

- Selecionar **Sim.**
- Configurar:
  - **ID do sistema**
  - **Senha**
  - **IPs da Lista Branca** (para a garantia)

!!! tip "Boas práticas"
 Whitelist IPs para evitar spam SMS.

Utilização **0.0.0.0** para acesso aberto (autenticação via ID & senha do sistema).

![SMPP Setup 1](images/adduser9.png)
![SMPP Setup 2](images/adduser10.png)

---

### **Passo 7: Gerenciar a Conta de Usuário**

Após completar a configuração, você verá a mensagem final com 3 opções:

#### **Opção 1: Personagem**
Faça logon como usuário instantaneamente — não há necessidade de credenciais separadas.

#### **Opção 2: Configurar cobrança antecipada**
Gerenciar planos de taxa:

- **Adicionar novo preço de venda**:
  - País
  - MCC/MNC
  - Preço de Venda
  - Estado de ativação
- **Modelo do Plano de Taxa de Importação**

!!! warning "Proteção contra perdas"
 Assegurar **preço de venda ≥ custo de entrada** para evitar quedas de mensagens (Política de Proteção de Perdas).

#### **Opção 3: Gerenciar este Usuário**
Acesso **Perfil** ou **Gestão do Utilizador** página para novos ajustes.

A **e- mail de boas- vindas** será enviado automaticamente.

![Impersonate](images/adduser11.png)
![Rate Plan Setup](images/adduser12.png)
![Manage User](images/adduser13.png)

---

□ **Está tudo pronto!** Agora você configurou completamente um usuário em **iTextPRO**, e estão prontos para gerenciar usuários, faturamento, notificações e muito mais – tudo de um só lugar.

# Gestão do Utilizador

A **Gestão do Utilizador** a seção é organizada em múltiplas abas para melhor layout de controle. Esta divisão de controles associada à conta de usuário fornece **conveniência na gestão eficaz da conta do utilizador**.

Para encontrar um usuário específico, simplesmente **insira o nome de usuário** na caixa de pesquisa e clique no **Ver** Botão. A caixa de pesquisa está equipada com um **recurso inteligente** que preenche automaticamente a caixa com **registros correspondentes em ordem alfabética**.

Para uma representação visual, consulte a figura abaixo:

![User Management](images/usermanagement1.png)

---

## Detalhes das Páginas de Gestão do Utilizador

### Opções da Primeira Linha

#### **Personagem**
- **Descrição:** A selecção desta opção permite- lhe **fazer login ou imitar um usuário** na conta deles.
- **Autenticação** Digite o **senha de administração** para verificação.
- **Nota:** A conta de usuário abre em um **nova página** dentro da mesma janela do navegador, facilitando **gestão simultânea** de contas de usuário e administrador.

#### **Gerenciar plano de taxa**
- **Funcionalidade:** Este hiperlink redireciona você para o **Plano de Taxa de Usuário** Page.
- **Objectivo:** Configurar **preços de venda para países e redes**.

#### **Estado**
- **Uso:** **Activar ou desactivar** uma conta de utilizador/reseller.
- **Resultado:** Utilizadores desativados **não é possível entrar**.

#### **Apagar este Utilizador**
- **Acção:** Permanentemente **apagar uma conta de utilizador**.
- **Atenção:** Usuários excluídos **não pode ser restaurado**.

---

### Opções da Segunda Linha

#### **Perfil (Detalhes Incluídos)**

- Nome do Utilizador 
- ID do usuário 
- Número Móvel 
- ID de e- mail *(utilizado para comunicação e indicações)* 
- Fuso horário 
- Prioridade do Usuário *(para mensagens de encaminhamento)* 
- Papel da Conta *(Revendedor ou Utilizador)* 
- Moeda do Usuário *(divulgar moeda, sujeito a conversão)* 
- Validade Até *(Alfândega ou Tempo de Vida)* 
- Último IP de Login 
- Hora da última sessão 

**Funcionalidade:** Acesso e gestão **informação básica do perfil do utilizador**.

#### **Reiniciar senha**
- **Acção:** Reiniciar a senha para **Utilizadores ou contas de revenda**.

!!! note
 Todas as acções na secção Gestão do Utilizador contribuem para **Gestão abrangente e simplificada da conta de utilizador** experiência. Para mais detalhes, consulte o manual do usuário do iTextPRO.

---

## Privilégios adicionais e configurações avançadas

![Advanced Privileges](images/usermanagement2.png)

### **Estado do Bloqueio do Usuário**
- **Descrição:** Habilitando esta opção **trava a conta do usuário**, restringindo as atividades de login.

### **Validação do Spam do Usuário**
- **Descrição:** Quando activado, o iTextPro **valida as palavras- chave do utilizador SPAM** para cada campanha. Usuários confiáveis podem **sobrescrever** isto, desactivando o botão.

### **Validação Global do Spam**
- **Descrição:** Habilita o aplicativo para **valida palavras- chave de SPAM globais** para campanhas de usuários. Usuários confiáveis podem substituir esta validação.

### **Validação IP da API**
- **Descrição:** Habilitar esta opção garante iTextPRO **valida o endereço IP listado em branco** antes de processar pedidos de API.

### **SMS HTTP Web Push**
- **Descrição:** Quando habilitado, o aplicativo **cópias DLR** para o URL de endpoint HTTP configurado na opção gerenciar webhooks da conta do usuário.

### **WhatsApp HTTP Web Push**
- **Descrição:** Habilitar este botão de comutar permite que o administrador ative o **Opção Webhook do WhatsApp** para que o usuário receba as DLRs/Conversas WhatsApp para os endpoints configurados.

![WhatsApp HTTP Web Push](images/usermanagement14.png)

### **Mostrar o Número Móvel Mascarado**
- **Descrição:** O número mascarado do show permite que o administrador habilite o recurso de **mascaramento de números**. Uma vez que este botão de comutação tenha sido definido como activo, todos os números móveis em que as campanhas foram iniciadas a partir da aplicação, **últimos quatro dígitos** para o número de telemóvel será mascarado.

![Show Masked Mobile Number](images/usermanagement15.png)

!!! example
 No Relatório de Campanha do usuário, números mascarados aparecem como <span data-ph="0"></span>.

![Masked Number in Report](images/usermanagement16.png)

### **Limiar de Sobrevenda do Usuário**
- **Descrição:** Activa a configuração de um **Limite do limiar de sobrevenda** nos utilizadores, permitindo-lhes consumir uma quantidade especificada para além do saldo atribuído.

**Exemplo:** 
Se o limiar for fixado em **500 EUROS**, o usuário pode consumir até **500 EUR mais** do que o saldo atribuído.

---

## Configuração Avançada

![Advanced Settings](images/usermanagement3.png)

### **Abrir o Sender**
- **Descrição:** Permite aos utilizadores finais enviar mensagens com um **ID do remetente dinâmico** (numérico ou alfanumérico).

### **Abrir Modelo**
- **Descrição:** Habilita usuários a usar **conteúdo dinâmico** nas mensagens, permitindo abrir modelos.

### **Ignorar o perfil OTP**
- **Descrição:** Envia um **OTP para o ID de e- mail registado do utilizador** para atividades de atualização de perfil.

### **Ignorar o OTP de Login**
- **Descrição:** Envia um **OTP para o ID de e- mail registado do utilizador** para atividades de login.

### **Permitir a compensação DLR**
- **Descrição:** Permite activar ou desactivar **Compensação DLR** Contas de revenda para crianças.

### **Compensação DLR**
- **Descrição:** Este recurso permite que o administrador gere algum lucro adicional aplicando compensação nas mensagens e gerando o DLR a partir da aplicação **sem enviar as mensagens para o gateway**.

![DLR Compensation](images/dlrcompensation1.png)

**Configuração:**

- **Estado do DLR:** Selecione o status da mensagem que precisa ser aplicado para as mensagens em que a compensação foi aplicada.
- **Percentagem:** Adicione o valor percentual ao qual a compensação precisa ser aplicada.
- **Código de Erro:** Configure o código de erro contra o status, então o mesmo será atualizado nos relatórios.
- **Limite do Limiar SMS:** Define o limiar de número de destino para a aplicação da compensação DLR. Uma vez atingido o limiar, a compensação será aplicada de acordo com a configuração.

!!! note
 Para a interface web, o limite de limiar funcionará com base na campanha e, no caso da SMPP/API, o limiar funcionará diariamente.

![DLR Compensation Controller](images/dlrcompensation2.png)

??? example "Exemplo de compensação DLR"
 Um usuário iniciou uma campanha em 2000 números com a seguinte configuração:

    - **Compensação DLR:** 20 Percentagem
    - **Limite de Limiar:** 1000

 De acordo com a configuração:

    - De 2000 mensagens, apenas **1600 mensagens** será submetido ao fornecedor de gateway.
    - Para **400 mensagens**, iTextPRO gera **DLRs falsas automáticas**, resultando em maximizar sua rentabilidade para 400 mensagens.

 Se o usuário enviar uma campanha sobre **1000> números móveis** (inferior ao limiar), **A compensação DLR não é aplicada**.

---

## Serviços Activos

Esta secção é composta por: **Plugins oferecidos pelo iTextPRO**. Estes plugins precisam ser **optado separadamente** uma vez que não fazem parte do pedido embalado.

![Active Services](images/activeservices1.png)

**Exibição de Serviços Activos:** Mostra os plug- ins atualmente habilitados. Além disso, o administrador pode ativar ou desativar os plug-ins do botão alternar.

### 1. **MO (Mobile Originator)**
- **Função:** Activa a **Serviço MO** para utilizadores.
- Uma vez que iTextPRO+ recebe o **mensagem de entrada (MO)**, aparece no **relatório da caixa de entrada do usuário**.
- As mensagens podem ser enviadas para **SMPP, HTTP push, email**, ou gatilho **respostas automáticas**.

### 2. **SMS inteligente**
- **Função:** Activa a **SMS inteligente** recurso.
- Converte URLs longos para **links inteligentes encurtados**.
- Faixas:
  - Utilizador **número de telemóvel**,
  - **Endereço IP**,
  - **Detalhes do dispositivo**,
  - **Geolocalização**.

### 3. **E- mail para SMS**
- **Função:** Conversos **e- mails em mensagens SMS**, habilitando a comunicação via gateways de email.

### 4. **WhatsApp**
- **Função:** Permite a **Serviços WhatsApp** ao utilizador.
- Uma vez que o plugin tenha sido ativado, o módulo WhatsApp aparecerá na aplicação.
- Os usuários podem conectar sua conta comercial ao aplicativo.
- Adicione modelos, configure os webhooks para DLR e Conversações.
- Obter APIs para enviar mensagens através de APIs.

---

## ID do remetente

A **ID do remetente** A aba habilita os usuários a configurar seus IDs de remetente diretamente. Mostra:

- **Pendente**
- **Aprovado**
- **Rejeitado** IDs do remetente

Acessível através da **"Ver ID do remetente"** link.

![Sender ID](images/usermanagement6.png)

Para **adicionar um ID do remetente**:

- Clique **Adicionar um Novo**
- Definir o **ID do remetente** e **finalidade**
- Clique **Gravar**

ID do remetente (Estatuto: **aprovado**) será adicionado à conta do usuário.

![Add Sender ID](images/usermanagement7.png)

---

## Modelo

A **Modelo** a seção permite aos usuários visualizar modelos existentes. Cada modelo **status** (aprovado, pendente, rejeitado) está claramente marcado.

![Templates](images/usermanagement8.png)

---

## Detalhes da mensagem

Os utilizadores obtêm informações sobre a **últimas três mensagens de campanha** e seus **estatísticas sobre o estado**, ajudando a avaliar **desempenho da campanha**.

![Message Details](images/usermanagement9.png)

---

## Créditos

A **Créditos** tab mostra:

- **Saldo disponível do usuário**
- **Histórico de transações**

Os utilizadores podem gerir o seu saldo de conta através **"Adicionar mais crédito"**:

![Credits](images/usermanagement10.png)

Para adicionar créditos:

- Selecionar **tipo de serviço**
- Digite **detalhes do pagamento**
- Especificar o **montante de crédito**

!!! note
 Os créditos devem ser adicionados ao **moeda de base**.

![Add Credit](images/usermanagement11.png)

---

## Filtro

A **Filtro** a opção permite aos utilizadores **Números móveis da lista branca**, assegurar **A compensação DLR não é aplicada** para aqueles.

Adicionar números móveis com **Códigos de países** facilmente.

![Filter](images/usermanagement12.png)

---

## MT Roteamento

A **MT Regra de Rotação** é uma característica fundamental. Você pode:

- Criar **regras de encaminhamento** para dirigir o tráfego de SMS
- Aplicar a:
  - **Interface Web**
  - **APIs**
  - **Observações da SMPP**

Os usuários também podem configurar **regras de roteamento de gateway fixas**, auto-povoando entradas no **Motor de Roteamento Principal**.

!!! tip
 Configurar um gateway fixo é opcional, mas melhora **eficiência de roteamento**.

![MT Routing](images/usermanagement13.png)

---

## Gerenciar plano de taxa

A **Gerenciar plano de taxa** a opção permite ao administrador configurar o **Preço de venda** para o utilizador.

**Preço de venda:** O montante admin será cobrado ao seu usuário por mensagem será o preço de venda.

Para adicionar um preço de venda ao usuário, siga os passos abaixo:

**Passo 1:** Vá para Administração >> Administração do Usuário >> Gestão do Usuário >> Usuário de pesquisa >> **Gerenciar plano de taxa**.

![Manage Rate Plan](images/rateplan1.png)

**Passo 2:** Escolha o método apropriado para adicionar preço de venda.

### 1] Adicionar novo preço de venda

Isso permite que o administrador digite o preço de venda um-por-um para o País e Redes para o usuário.

Selecione o Tipo de Interface: **TODOS** ou **SMPP**

![Add New Selling Price](images/rateplan2.png)

#### a) TODA a interface

Se a interface foi escolhida como ALL, o administrador precisa especificar o País & Rede, em seguida, o preço de venda. Uma vez que todos os detalhes foram adicionados, clique em **ADD** para salvar a configuração.

![ALL Interface](images/rateplan3.png)

#### b) Interface SMPP

Se a Interface foi escolhida como SMPP, o administrador precisa especificar **SMPP Nome do conector ou nome ESME**, por conseguinte, o plano de taxas será aplicável a essa conta SMPP específica. Em seguida, especifique o País & Rede e o preço de venda. Uma vez que todos os detalhes foram adicionados, clique em **ADD** para salvar a configuração.

![SMPP Interface](images/rateplan4.png)

!!! info "ALL vs. Interface SMPP"
 **TODOS** indica mensagens iniciadas de todas as interfaces (Web, API e SMPP). **SMPP** indica um plano de taxa aplicável apenas quando o usuário está enviando tráfego usando a interface SMPP. Se nenhum preço de venda específico para SMPP estiver configurado, as mensagens serão processadas com o preço configurado para TODOS.

![Rate Plan List](images/rateplan8.png)

### 2] Modelo do plano da taxa de importação

Esta opção permite ao administrador importar todas as taxas existentes ou folha de taxas preparadas para a conta do usuário de uma só vez. Ele reduzirá as iterações para adicionar vários preços de venda à conta do usuário.

**Passo 1:** Selecione o plano de taxa
**Passo 2:** O administrador também pode escolher a interface (ALL ou SMPP)
**Passo 3:** Opção para substituir qualquer preço de venda existente.
**Passo 4:** Clique no botão Importar para adicionar o preço de venda à conta do usuário.

![Import Rate Plan Template](images/rateplan6.png)

### Notificar usuário

Sempre que o preço de venda é atualizado pelo administrador, um e-mail será enviado para o e-mail registrado na conta de usuário com a linha de assunto **"Notificação de Atualização de Preços - Suas Taxas de Mensagens Foram Revisadas"**.

Este e-mail contém os arquivos excel para todos os preços de venda configurados na aplicação.

Além disso, o administrador / revendedor pode clicar no **Notificar usuário** botão para ativar o e-mail para o usuário, caso eles não tenham recebido nenhum e-mail.

![Notify User](images/rateplan5.png)

---

## Criação do usuário - Modo de cobrança

Durante **criação do usuário**, se **Módulo de facturação** está habilitado no aplicativo, o administrador deve configurar o **Modo de cobrança** para o utilizador. O modo de faturamento selecionado determina como o uso da mensagem é cobrado e como as faturas são geradas.

![Billing Mode](images/billingmode1.png)

Estão disponíveis os seguintes modos de faturamento:

=== Pré-pago ===

 Quando um usuário está configurado como **Pré-pago**:

    - O administrador deve: **gerar uma fatura manualmente**.
    - O montante da factura deve ser **creditado na conta do utilizador**.
    - Somente após a fatura ser reivindicada e o saldo estiver disponível o usuário poderá enviar mensagens do aplicativo.
    - O envio de mensagens é restrito com base no saldo pré-pago disponível.

=== Pós-pago ===

 Quando um usuário está configurado como **Pós-pago**:

    - O administrador deve: **atribuir um limite de descoberto** ao utilizador.
    - O pedido **gerar automaticamente faturas** baseado no configurado **Ciclo de cobrança**.
    - O usuário pode continuar enviando mensagens até que o limite atribuído seja alcançado.
    - A cobrança é calculada com base no uso real durante o período de faturamento.

!!! warning "Notas-chave"
    - A **Modo de cobrança** é aplicável apenas quando o módulo de facturação estiver activo.
    - A configuração de faturamento impacta diretamente a entrega de mensagens do usuário e a geração de faturas.
    - Limites adequados de descoberto e ciclos de faturamento devem ser configurados para usuários pós-pagos para evitar a interrupção do serviço.
