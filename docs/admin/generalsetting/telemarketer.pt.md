
# Configuração do Telemarketing

Com a introdução de **REGRAS TRAI DLT**, o tráfego de SMS na Índia deve seguir uma obrigatoriedade **Corrente PE-TM** (Entidade principal-cadeia Telemarketing). Esta cadeia garante rastreabilidade e conformidade regulamentar entre todas as partes interessadas envolvidas na transmissão de mensagens, incluindo **Usuário, revendedor, aplicativo e fornecedor**.

Para cumprir estes regulamentos, a aplicação deve ser configurada para **Anexar as informações necessárias do Telemarketing** Antes de enviar mensagens para o fornecedor a montante ou SMSC.

---

## Lógica de formação de corrente PE-TM

A cadeia PE-TM é construída dinamicamente durante a submissão de mensagens com base no **tipo de fornecedor**.

### Fluxo de Mensagens

1. A **usuário** envia a mensagem juntamente com o seu **Identificação da Entidade Principal (PEID)**.
2. A **aplicação** adiciona a sua configuração **ID do Telemarketing (TMID)**.
3. A estrutura final da cadeia depende do tipo de fornecedor.

---

## Tipos de fornecedores e formação em cadeia

=== "Aggregator"

 An **Agregador** é um fornecedor intermediário que envia a mensagem para outro fornecedor ou SMSC.

    - O pedido anexa o seu **TMID**
    - O agregador adiciona o seu próprio **TMID2**
    - A mensagem é então enviada para o próximo salto

 **Formação em Cadeia:** <span data-ph="0"></span>

    !!! info
 Hashing é **não exigido** no nível de aplicação para fornecedores agregadores.

=== "Parceiro de Entrega"

 A **Parceiro de entrega** é o SMSC final responsável pela entrega da mensagem ao aparelho.

    - O pedido anexa o seu **TMID**
    - A cadeia final deve ser **hashed** antes da apresentação

 **Formação em Cadeia:** <span data-ph="0"></span>

    !!! info
 O hash garante o cumprimento dos requisitos de segurança e integridade da TRAI.

---

## Configuração do Telemarketing na Aplicação

**Caminho de navegação:** <span data-ph="0"></span>

![Telemarketer Configuration List](images/telemarketer1.png)

---

## Passos de Configuração

1. Clique em **Adicionar um Novo**
2. Selecione o **Nome do Portal**
3. Digite o **ID do Telemarketing (TMID)**
4. Configurar o hashing com base no tipo de fornecedor:
    - **Agregador:** Definir **É Hashing Ativo = OFF**
    - **Parceiro de entrega:** Definir **É Ativo Hashing = ON**
5. **Tipo de Hash:**
    - Predefinições **SHA-256** (recomendado e conforme com o TRAI)
6. Clique **Gravar** para aplicar a configuração

![Telemarketer Configuration Dialog](images/telemarketer2.png)

---

!!! danger "Notas Importantes"
    - A configuração incorreta do hashing pode resultar em **Rejeição do DLT** pelo vendedor ou SMSC.
    - Certifique-se de que o tipo de fornecedor (Aggregator vs Delivery Partner) seja confirmado antes da configuração.
    - O SHA-256 é aplicado como algoritmo de hashing padrão para atender às normas regulatórias.
