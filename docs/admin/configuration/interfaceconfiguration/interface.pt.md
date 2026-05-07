---
tags:
  - SMPP
  - ESME
  - HTTP API
  - Configuration
---

## Gerenciar Interface

A **Gerenciar Interface** seção no iTextPRO permite que os administradores configurem e gerenciem a conectividade do parceiro através **Ligações SMPP (Contas ESME)** e **Conectores HTTP**. Estes conectores aumentam as capacidades de comunicação, permitindo uma integração perfeita com sistemas externos.

---

### 1. Conector SMPP (Conta ESME)

![SMPP Connector](images/manage1.png)

A **Conector SMPP**, também referido como **Conta do ESME (entidade externa de mensagens curtas)**, facilita conexões de parceiros para o **Servidor SMPP** no iTextPRO.

#### Como adicionar um novo conector SMPP:
1. Procure a conta de usuário específica.
2. Clique **"Adicionar Novo"** para iniciar a configuração.
3. Preencha os detalhes necessários:

**Campos de Configuração da Conta ESME:**

| Campo | Designação das mercadorias |
|-------|-------------|
| **ID do sistema** | Nome de utilizador usado para ligar à conta ESME |
| **Senha** | Senha de autenticação para a conta ESME |
| **Whitelist IP** | Só são permitidas ligações deste IP |
| **Contagem Tx** | Número de sessões do transmissor (Tx) |
| **Rx Count** | Número de sessões de Receptor (Rx) |
| **Contagem TRx** | Número de sessões de Transceiver (TRx) |

#### Configuração Avançada:
- **Validar IP**: Activa a validação dos endereços IP de origem. Apenas IPs em branco podem se conectar.
- **Está Activa a Conta**: Quando habilitado, o usuário do ESME pode se conectar ao servidor SMPP.
- **Lista negra**: Isto é ativado automaticamente se o usuário ESME violar o **Regra da lista negra do ESME**.

---

### 2. Conector HTTP

![HTTP Connector Setup](images/manage2.png)

A **Conector HTTP** permite que os parceiros se integrem com o iTextPRO usando **APIs baseadas em HTTP**.

#### Passos para habilitar o acesso à API HTTP:
1. Activar **Estado da API** na conta de utilizador desejada.
2. Uma vez activada, a **API do desenvolvedor** a seção fica visível na interface do usuário.
3. A partir daí, os usuários podem:
   - Ver **Credenciais da API**
   - **Transferir a documentação da API** (Formato PDF)
   - Comece usando endpoints de API HTTP para submissões de mensagens, relatórios e muito mais.

![HTTP API Dashboard](images/manage3.png)

---

### Resumo

A **Gerenciar Interface** no iTextPRO oferece uma configuração unificada e intuitiva para ambos **Conectores SMPP e HTTP**, permitindo:
- Acesso seguro e controlado para parceiros e revendedores.
- Documentação e ferramentas de API para fácil integração.
- Controle de nível de sessão e gerenciamento de acesso baseado em IP.

Ao aproveitar esses conectores, os usuários do iTextPRO podem expandir seu alcance de mensagens, mantendo um controle e flexibilidade rigorosos.
