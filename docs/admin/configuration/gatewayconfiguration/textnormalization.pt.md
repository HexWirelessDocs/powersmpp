
# Normalização do Corpo da Mensagem

A **Normalização do Corpo da Mensagem** A regra é um recurso incorporado dentro **Potência SMPP**, projetado para dar aos administradores flexibilidade para modificar e refinar o conteúdo da mensagem antes da submissão ao gateway. 
Isso garante que todas as mensagens enviadas sejam formatadas corretamente, melhorando a legibilidade e a eficácia.

Este documento explica como **Normalização do Corpo da Mensagem** funciona e como os administradores podem configurá-lo para ajustar automaticamente o conteúdo da mensagem com base em regras predefinidas — garantindo consistência e conformidade com os requisitos de gateway.

---

## Características Principais

A Regra de Normalização do Corpo de Mensagens estende o existente **Regra de Normalização OA/DA**. Ele fornece várias maneiras de manipular o conteúdo da mensagem, incluindo:

- **Extração de códigos/OTPs:** Detectar e extrair automaticamente OTPs ou códigos específicos do texto da mensagem. 
- **Adicionar Prefixos ou Sufixos:** Inserir texto específico antes ou depois da mensagem para manter um formato padrão. 
- **Substituição de Texto:** Substituir certas palavras ou frases de acordo com regras predefinidas para uma melhor consistência.

Essas opções ajudam os administradores a garantir que todas as mensagens estejam de acordo com os padrões de gateway, melhorando a experiência geral de mensagens.

---

## Normalização do Corpo de Mensagens

Para configurar a Normalização do Corpo da Mensagem:

1. Navegar para o **Módulo de Configuração**. 
2. Selecionar **Configuração do Gateway**. 
3. Escolher **Normalização do Corpo da Mensagem**. 
4. Clique **Adicionar um Novo** criar uma nova regra de normalização.

![Message Body Normalization UI](images/mbn1.png)

---

## Configuração da Regra

Depois de clicar **Adicionar um Novo**, uma página de configuração aparece com vários campos.

### **Nome da Regra**
Defina um nome descritivo e significativo para a regra.

---

### **Configuração da Condição**

#### 1. Selecione Interface
Especifique a interface onde a regra se aplica. Você pode selecionar um ou mais dos seguintes:

- WEB 
- API 
- SMPP 
- Todas as Interfaces 

![Interface Selection](images/mbn3.png)

Isso permite a aplicação de regras específicas dependendo da interface operacional.

---

#### 2. Usuário
Escolha se a regra se aplica a:
- A Específica **Usuário**, ou 
- **QUALQUER** (aplica-se a todos os utilizadores).

---

#### 3. ID do remetente
Configurar as condições de ID do remetente com base em padrões de correspondência específicos:

- **Igual** – Corresponde exatamente ao ID do remetente especificado 
- **Iniciar com** – Ativa se o ID do remetente começa com uma palavra-chave específica 
- **Terminar com** – Aplica se o ID do remetente termina com uma palavra-chave específica 
- **Contém** – Aplica-se se a palavra-chave for encontrada em qualquer lugar no ID do remetente 

![Sender ID Condition](images/mbn4.png)

---

#### 4. Endereço do destino
Funções semelhantes às **ID do remetente**, permitindo as mesmas condições — *Igual*, *Iniciar com*, *Terminar com*, *Contém* — aplicar regras baseadas no formato do endereço de destino.

---

#### 5. Mensagem
As mesmas opções condicionais acima podem ser aplicadas ao conteúdo da mensagem, permitindo o controle preciso da formatação.

---

## Ações: Explicação detalhada

In **Potência SMPP**, **Acção** a seção oferece três métodos configuráveis para manipular o conteúdo da mensagem antes da submissão ao gateway:

1. **Código de extração** 
2. **Procurar e Substituir** 
3. **Adicionar e Prependir**

Cada um serve um caso de uso específico. Vamos explorar cada um em detalhes.

---

### Código de Extração

A **Código de extração** Action permite que os administradores puxem OTPs ou códigos de mensagens.

#### a) De modelo fixo
Se a mensagem tiver um padrão fixo, você pode usar <span data-ph="0"></span> para definir a contagem de caracteres para extração.

**Exemplo:**

- Mensagem: <span data-ph="0"></span> 
- Configuração: <span data-ph="0"></span> 
- Saída: <span data-ph="0"></span> 

![Extract Code - Fixed Template](images/mbn6.png)

---

#### b) Pelo seu índice de ocorrência
Use isto quando as mensagens contêm vários códigos, e você deseja extrair um pelo seu índice.

**Exemplo:**
- Mensagem: <span data-ph="0"></span> 
- Configuração: 
  - Comprimento: <span data-ph="0"></span> 
  - Índice: <span data-ph="0"></span> 
- Saída: <span data-ph="0"></span>

![Extract Code - Occurrence Index](images/mbn7.png)

---

### Encontrar e substituir

Use isto para substituir palavras ou frases específicas na mensagem.

**Exemplo:**
- Mensagem: <span data-ph="0"></span> 
- Configuração: 
  - Procurar: <span data-ph="0"></span> 
  - Substituir: <span data-ph="0"></span> 
- Saída: <span data-ph="0"></span>

![Find and Replace](images/mbn8.png)

---

### Adicionar e Prependir

Isso permite adicionar texto personalizado antes (prepend) ou depois (append) a mensagem, ou ambos.

#### a) Adicionar  
Adiciona texto ao **fim** da mensagem. 
**Exemplo:** 
- Mensagem: <span data-ph="0"></span> 
- Adicionar: <span data-ph="0"></span> 
- Saída: <span data-ph="0"></span> 

![Append Example](images/mbn10.png)

---

#### b) Preparação  
Adiciona texto ao **início** da mensagem. 
**Exemplo:** 
- Mensagem: <span data-ph="0"></span> 
- Prepend: <span data-ph="0"></span> 
- Saída: <span data-ph="0"></span> 

![Prepend Example](images/mbn11.png)

---

#### c) Ambos  
Adiciona tanto um prefixo como um sufixo. 
**Exemplo:** 
- Mensagem: <span data-ph="0"></span> 
- Prepend: <span data-ph="0"></span> 
- Adicionar: <span data-ph="0"></span> 
- Saída: <span data-ph="0"></span> 

![Append and Prepend Both](images/mbn12.png)

---

## Combinando várias ações

Os administradores podem aplicar várias ações dentro de uma única regra.

**Exemplo:**
- Mensagem: <span data-ph="0"></span> 
- Acções: 
  - Extrair código (de modelo fixo) 
  - Adicionar e Prependir (Ambos) 

Isto extrai o OTP e aplica formatação de texto adicional conforme configurado.

![Combined Actions](images/mbn13.png)

---

## Prioridade e Compatibilidade

- **Normalização do Corpo da Mensagem** executa **antes** a **Normalização OA/DA**. 
- Isso garante que o conteúdo da mensagem seja otimizado e formatado primeiro, evitando conflitos de regras. 
- Ambas as regras de normalização funcionam em camadas para submissão precisa de gateway.

---

## Resumo

**Normalização do Corpo da Mensagem** no Power SMPP capacita os administradores para:
- Extrair OTPs ou códigos, 
- Adicionar prefixos/sufixos, 
- Substituir palavras ou frases, 
- Combinar várias regras e 
- Aplicar regras por usuário, remetente ou interface. 

Este recurso garante que todas as mensagens mantenham um formato consistente e cumpram os requisitos de gateway — melhorando a confiabilidade e o profissionalismo na entrega de mensagens.
