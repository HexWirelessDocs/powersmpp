
# Modelos de E- mail

## Características Principais

### Monitorização automatizada
- **iTextPro** Monitora continuamente os parâmetros críticos da aplicação em intervalos regulares.
- Identificação proactiva de potenciais problemas antes de se intensificarem.

### Alertas via E- mail
- Os interessados recebem alertas através de notificações por e-mail.
- As notificações são enviadas com antecedência, permitindo que as partes interessadas tomem medidas preventivas.

### Gestão Personalizada de Modelos
- Suporta modelos de alerta personalizáveis.
- Os usuários podem gerenciar e adaptar modelos de notificação de acordo com seus requisitos.

### Integração com as Variáveis do Sistema
- Modelos personalizados podem incluir variáveis relevantes do sistema.
- Comunicação personalizada através de informações do sistema atualizadas dinamicamente.

---

## Orientações de Utilização

### Gestão de Modelos
- Personalize modelos de alerta para atender às necessidades de comunicação específicas.
- Incorpore variáveis relevantes do sistema para notificações dinâmicas e conscientes do contexto.

### Engajamento das partes interessadas
- Assegurar que as partes interessadas estejam configuradas para receber notificações.
- Verifique se as configurações de e-mail estão configuradas corretamente para uma comunicação perfeita.

---

## Benefícios
- Aumenta a confiabilidade e a estabilidade da **iTextPro** aplicação.
- Fornece um mecanismo proativo para detecção e alerta de problemas.
- Modelos personalizáveis e variáveis do sistema permitem comunicação personalizada e informativa.
- Ajuda as organizações a ficarem à frente de potenciais desafios.

!!! note
 Os detalhes de SMTP são obrigatórios para o administrador, bem como para contas de revendedores para ativar e-mails.

---

## Gestão de Modelos de E- mail

![Email Templates](images/template1.png)

---

## Eventos de Notificação e Modelos Correspondentes

### Falha de comunicação agregada
Acionado quando o serviço de relatórios agregados encontra uma falha desconhecida. 
![Aggregate Reporting Failure](images/template2.png)

### Notificação da homologação
Enviado após aprovação do administrador de ID do remetente e pedidos de modelo. 
![Approval Notification 1](images/template3.png) 
![Approval Notification 2](images/template4.png)

### Notificação do pedido de homologação
Ativado quando um revendedor/usuário inicia uma solicitação de aprovação do Sender ID ou modelo. 
![Approval Request Notification 1](images/template5.png) 
![Approval Request Notification 2](images/template6.png)

### Mudar a Senha
Enviado quando um usuário muda sua senha com sucesso. 
![Change Password](images/template7.png)

### Notificação de Crédito
Alertado quando o saldo disponível de um usuário cai abaixo do limiar de crédito. 
![Credit Notification](images/template8.png)

### Transferência de Crédito
Triggered após a adição de saldo para uma conta de usuário pelo usuário ou revendedores. 
![Credit Transfer](images/template9.png)

### Correio de E- mail
Enviado ao receber uma mensagem recebida (MO) quando o encaminhamento de e-mail MO está ativo. 
![Email Post](images/template10.png)

### Esme Lista Negra
Alertado quando uma conta ESME está na lista negra devido ao spam. 
![Esme Blacklist](images/template11.png)

### Porta de falha
Acionado quando a comutação automática de mensagens ocorre devido a uma falha primária do gateway. 
![Failover Gateway](images/template12.png)

### Esqueceu a senha
Enviado quando existe uma solicitação para alterar a senha da conta de login. 
![Forgot Password](images/template13.png)

### Gateway Lista negra
Alertado quando um gateway/rote de fornecedor SMPP está na lista negra após tentativas de vinculação falhadas. 
![Gateway Blacklisted](images/template14.png)

### Gateway Preço Expiração
Triggered quando uma rota com uma taxa expirada é detectada. 
![Gateway Price Expiry](images/template15.png)

### Notificação não aprovada
Enviado quando um ID do remetente ou pedido de modelo é desaprovado pelo administrador / revendedor. 
![Job Disapproved Notification 1](images/template16.png) 
![Job Disapproved Notification 2](images/template17.png)

### Fila de Mensagem
Ativado quando a fila de gateway do fornecedor viola o limite de limiar. 
![Message Queue](images/template18.png)

### Nova Conta por Administração
Enviado quando um novo usuário é adicionado da administração ou se inscreve. 
![New Account by Admin](images/template19.png)

### Nova Conta por Revendedor
Enviado para revendedores quando um revendedor adiciona um novo usuário ou um novo usuário se inscreve. 
![New Account by Reseller](images/template20.png)

### Nova Verificação de Email do Usuário
Ativado para novos usuários se inscrever para verificação de e-mail. 
![New User Email Verification](images/template21.png)

### OTP
Enviado para verificação OTP durante logins do usuário. 
![OTP](images/template22.png)

### Estado do serviço
Alertado quando um demónio/serviço é automaticamente recuperado.

### Serviço Parado
Disparado quando um demónio/serviço é intencionalmente parado. 
![Service Stopped](images/template23.png)

### Detecção de Spam
Alertado quando o conteúdo de SPAM é detectado. 
![Spam Detection](images/template24.png)

### Actualização da Venda do Utilizador
Enviado quando o preço de venda do cliente é atualizado pela conta-mãe. 
![User Selling Update](images/template25.png)

---

Estas notificações abrangem uma vasta gama de eventos, fornecendo insights abrangentes e alertas oportunos para garantir o acompanhamento e a gestão eficientes do **iTextPro** plataforma.
