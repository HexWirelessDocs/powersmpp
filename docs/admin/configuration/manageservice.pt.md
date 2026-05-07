
## Gerenciar serviços

A **Gerenciar serviços** seção no iTextPRO fornece visibilidade para os vários **serviços de base e de primeiro plano** que impulsionam as funcionalidades centrais da plataforma. Esta interface destina-se principalmente a utilizadores ou administradores especializados.

!!! danger "Atenção"
 Embora seja possível parar ou iniciar um serviço a partir da interface web, isso deve ser feito **com extrema precaução**, particularmente durante o tempo de carga de pico, pois pode resultar em **perda de dados** ou **perturbação do serviço**.

---

### Visão Geral do Serviço

Abaixo está uma breve descrição de cada serviço visível no **Gerenciar serviços** secção:

| **Nome do serviço**         | **Designação das mercadorias**                                                                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Serviço do Cliente**       | Liga o iTextPRO ao seu SMSC via SMPP para gerir **SMS MT (Terminado em Mobile)** e **SMS MO (Mobile Originado)** tráfego.                      |
| **Serviço DLR**          | Manuseia em tempo real **Relatórios de entrega (DLRs)** e atualiza o status da mensagem dentro do sistema para relatórios precisos.                                      |
| **Serviço de Servidor SMPP**  | Escuta para o tráfego SMPP de entrada de **Utilizadores do ESME** numa porta pré-definida, permitindo aos utilizadores externos enviar SMS.                                      |
| **Serviço de recolha de ficheiros**  | Lê os ficheiros de mensagem de campanha enviados pelos utilizadores e encaminha- os para o **fila de gateway** para processamento.                                               |
| **Serviço de Validação**    | Validações **parâmetros de ligação** para usuários que se conectam através de interfaces API e SMPP, garantindo que o tráfego é aceito apenas de clientes autorizados.       |
| **Serviço de Construtor de Dados** | Gerencia o armazenamento de **Registos de PDU** e **logs de mensagens** no banco de dados para fins de registro e depuração.                                          |
| **Serviço de Construtor de Relatórios** | Perfis e compilações **contas enviadas e relatórios sumários** para usuários, auxiliando no rastreamento de uso e faturamento.                                            |
| **Download Report Service** | Processos e gera **relatórios transferíveis** para administradores e usuários com base em dados solicitados.                                                  |
| **Serviço de Notificação** | Envia **Notificações de alerta de e- mail** para usuários e administradores e monitores ativamente **estado de saúde da porta de entrada**.                                               |

---

### Características Principais

- Ver o **estado atual** de cada serviço.
- □ Opção para **Iniciar** ou **Parar** serviços da interface web.
- Projetado para uso por **usuários ou administradores avançados** com uma forte compreensão das dependências de serviço.
- Cada serviço inclui metadados como o **versão da aplicação**.

---

### Melhores Práticas

- Sempre confirmar horas de pico de tráfego antes de parar qualquer serviço crítico (por exemplo, Cliente, DLR, Validador).
- Evite reiniciar serviços sem consultar registros de sistema ou suporte técnico.
- Certifique-se de que os serviços de banco de dados e gateway estejam sincronizados para evitar inconsistências de dados.

---

A **Gerenciar serviços** O recurso oferece uma forma centralizada de monitorar e controlar processos de nível de sistema, garantindo operações suaves dentro do ambiente iTextPRO.
