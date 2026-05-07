---
tags:
  - SMPP
  - Gateway
  - Configuration
---

# Configuração

## Porta SMPP (MO/MT)

A **Aplicação iTextPRO** prioriza a **experiência amigável** através de uma interface de design flexível e um fluxo de trabalho de configuração simplificado. O objetivo é afastar-se de complexidades CLI e imergir proprietários de aplicativos em um **Interface gráfica do usuário (GUI)**- ambiente baseado. Uma integração **Motor de comunicação** lida com todos os comandos da infraestrutura, simplificando suas tarefas operacionais.

---

![Manage Gateway](images/httpgateway1.png)

---

A **"Manage Gateway"** recurso capacita usuários para lidar com conectividade com externa **Centros de Serviços de Mensagens Curtas (SMSCs)** via **SMPP** e **HTTP** protocolos.

Para **SMPP**, a **ligação única** permite operações Mobile-Originated (MO), Mobile-Terminated (MT) e Relatórios de Entrega (DLR). Suportes iTextPRO **SMPP múltiplo Portais**, permitindo **redundância** e **roteamento econômico**.

---

### Configurar uma nova porta

Para configurar um conector SMPP:

1. Clique **"Adicionar Novo"**.
2. Digite as credenciais fornecidas pelo seu **fornecedor de gateway** ou **operador de telecomunicações**.

---

![SMPP Gateway Credentials](images/httpgateway2.png)

---

#### Credenciais Obrigatórios

| Campo | Designação das mercadorias |
|-------|-------------|
| **Nome do Portal** | Um nome amigável para identificar seu gateway |
| **Endereço IP** | O IP do seu SMSC/vendor |
| **ID do sistema** | Nome de utilizador fornecido pelo seu fornecedor/SMSC |
| **Senha** | Usado para autenticação no SMSC |
| **Tx Port / Rx Port / TxR Port** | Portos para Transmissor, Receptor e Transceptor se ligam |
| **Tipo de sistema** | *(Opcional)* Digite apenas se necessário pelo vendedor |

!!! warning
 Verifique todos os valores conforme a documentação SMSC/vendor para garantir uma conexão bem sucedida.

---

### Propriedades do Portal

![Gateway Properties](images/httpgateway3.png)

Configurar o SMPP Propriedades da gateway no iTextPRO para o desempenho ideal:

1. **Manter vivo (segundos):** 
 Intervalo para *Perguntar a Ligação* Para manter a sessão viva.

2. **Gateway Open Time / Close Time:** 
 Definir horas operacionais, muitas vezes utilizadas para cumprir **Não Perturbar** políticas.

3. **Codificação do Portal:** 
 Seleção de caracteres compatível com o telco/SMSC.

4. **Converter ID da mensagem:** 
 Permite a conversão entre **Decimal ↔ Hex** Formatos de ID de mensagem para DLRs precisos.

5. **Zona horária:** 
 Todos os relatórios refletirão este fuso horário selecionado.

6. **Parar o Preço de Perda:** 
 Define o **custo máximo permitido do gateway** quando utilizar roteamento cego.

7. **Produção por segundo (TPS):** 
 Definir com base na capacidade do fornecedor. 
 **Fórmula:** <span data-ph="0"></span>

---

### Configuração do TON/NPI

![TON/NPI Setup](images/httpgateway4.png)

- **TON (Tipo de número):** 
 Selecione como por documentação SMSC (por exemplo, Internacional, Alfanumérico, etc.)

- **NPI (indicador do plano de numeração):** 
 Indica a norma de numeração em uso (E.164, RDIS, etc.)

- **Configuração da Sessão:** 
 Configure sessões Tx, Rx e TxR por alocação de fornecedores.

---

### Roteamento

![Gateway Roles](images/httpgateway5.png)

- **É Activo:** 
 Marca o portal como ao vivo e pronto para encaminhar o tráfego.

- **É Padrão:** 
 Apenas um gateway pode ser marcado como padrão. Mensagens sem rotas correspondentes vão aqui.

- **É o Async:** 
 Activar **modo assíncrono** para envios de mensagens mais rápidos.

- **Roteamento Cego:** 
 Permite a submissão de mensagens aos países **sem preços de custo definidos**.

!!! tip
 Após a configuração, clicando **"Salvar"** envia uma **Pedido de ligação em voo** — não é necessário reiniciar manualmente.
