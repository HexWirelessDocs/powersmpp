
# Faturação

O módulo de faturamento permite que os administradores gerenciem faturamento para seus usuários diretos (tipo Conta: **Usuário**), fornecendo um plugin para gerar faturas, baixá-los ou enviá-los por e-mail. O fluxo de geração de faturas é automatizado e acionado em intervalos específicos configurados pelo administrador.

Este módulo ajuda os administradores a gerenciar a operação de faturamento de seus usuários filhos de forma eficiente.

---

## Fatura [pré-pago / pós-pago] como Plug- in

O administrador deve optar por **Licença de facturação** separadamente. Uma vez habilitado, o módulo de faturamento torna-se acessível na aplicação com o modo de faturamento selecionado-**Pré-pago** ou **Pós-pago**.

- A **Método de cobrança** (Pré-pago/Pós-pago) para cada usuário é definido durante a criação do usuário.
- O administrador pode configurar o método de faturamento para cada usuário.
- Usuários que se inscrevem por conta própria terão **Pré-pago** faturamento por padrão.

---

## Painel de facturação

Quando o administrador acessa o módulo de faturamento, a primeira view apresentada é a **Painel de facturação**. O painel fornece insights chave de faturamento:

### 1. Fatura Total
Mostra a **número total de facturas**, incluindo:
- Facturas aprovadas 
- Facturas não aprovadas 

### 2. Faturas pagas
Mostra a contagem de **facturas integralmente pagas**.

### 3. Faturas Inquietas
Mostra o número de faturas que ainda estão pendentes, com:
- Facturas não pagas 
- Facturas parcialmente pagas 

### 4. Gerenciar a fatura
Um breve resumo do *Gerenciar fatura* secção. 
Os administradores podem clicar **Ir para a Página** Para navegar para gestão detalhada da fatura.

### 5. Gerencie Faturas Recorrentes
Aplicável **Apenas para os utilizadores pós-pagos**. 
A partir daqui, os administradores podem:
- Criar faturas recorrentes 
- Iniciar ou parar o ciclo de faturamento 
- Modificar as configurações do ciclo de faturamento 

### 6. Gerenciar o pagamento recebido
Um breve resumo do *Gerenciar o pagamento recebido* secção. 
Os administradores podem redirecionar para a página detalhada usando o **Ir para a Página** Botão.

---

## Gerenciar faturas

A **Gerenciar faturas** página exibe todas as faturas (incluindo faturas recorrentes) juntamente com o seu estado de pagamento. Os administradores podem reivindicar faturas, baixá-las e enviar e-mails de lembrete de pagamento.

![Manage Invoices](images/manage1.png)

### Características chave:

#### **Baixar relatório de fatura**
Permite que os administradores exportem e baixem o relatório de fatura como uma planilha Excel.

#### **Enviar lembrete em massa**
Permite enviar lembretes de pagamento para usuários cujas faturas são **Não pago** ou **Pagado Parcialmente**.

#### **Rascunhos**
As faturas recorrentes geradas automaticamente para usuários pós-pagos são armazenadas como **rascunhos**. 
Os administradores devem rever e aprovar os rascunhos manualmente do menu Ação.

#### **Pesquisa Avançada**
A opção de pesquisa avançada permite filtrar faturas por:
- Usuário 
- ID da factura 
- Estado devido 
- Situação do pagamento 

Isso ajuda os administradores a localizar faturas rapidamente com base em requisitos específicos.

---

## Criar Fatura

Esta seção permite que os administradores criem manualmente faturas para os usuários.

---

### **Para usuários pré-pagos:**

1. Selecione o tipo de usuário: **Pré-pago**
2. Escolha o utilizador.
3. Digite o **Data da factura** e **Data de vencimento**.
4. Digite o **Quantidade de recarga** (antes dos impostos).
5. Fornecer uma **descrição** da factura.
6. Modificar **Termos e Condições** ou **Notas de Clientes** se necessário (ou usar valores configurados por omissão).
7. Escolha um de:
   - **Criar Fatura** (se o pagamento ainda não for recebido)
   - **Criar & Reivindicar Fatura** (se o pagamento já tiver sido recebido — o sistema irá alertar para os detalhes do pagamento)

---

### **Para Usuários Postpained:**

As faturas pós-pagos são geralmente geradas automaticamente no final do ciclo de faturamento definido em **Faturas recorrentes**. 
No entanto, se um ciclo foi ignorado ou precisa de intervenção manual, os administradores podem criar a fatura manualmente:

1. Selecione o tipo de usuário: **Pós-pago**
2. Escolha o utilizador.
3. Selecione o **intervalo de datas** para o qual a fatura deve ser criada e buscar os registros.
4. O sistema exibirá os registros de mensagens para o período selecionado.
5. Após verificação, escolha:
   - **Criar Fatura**
   - **Criar e Reivindicar factura**

