---
tags:
  - Routing
  - Configuration
  - MT
---

## Gerenciador de regras de roteamento

O roteamento desempenha um papel crucial na manutenção de uma vantagem competitiva e na maximização da receita. A **Gerenciador de regras de roteamento** no iTextPRO permite o encaminhamento eficiente do tráfego SMS do usuário para o seu destino final através de lógica de roteamento dinâmica e inteligente.

Aplicações SMPP suportam múltiplos caminhos de roteamento. iTextPRO simplifica essa complexidade, permitindo que você crie regras dinâmicas de roteamento de MT (Mobile Terminated) que melhorem o desempenho da entrega, reduzam os custos e distribuam o tráfego de forma inteligente.

Os principais benefícios incluem:
- Seleção de gateway com base no tempo de entrega
- Otimização de custos através de roteamento de menor custo
- Comutador dinâmico entre protocolos HTTP e SMPP
- Distribuição de tráfego em tempo real e balanceamento de carga

Uma vez dentro da **MT Regra de Rotação** seção, uma lista de regras de roteamento já configuradas será exibida. Podes. **editar** qualquer regra clicando no ícone de edição.

!!! tip
 Não é necessário reiniciar ou recarregar manualmente. Todas as atualizações da regra de roteamento são aplicadas em tempo real.

---

### Gerenciar a regra de roteamento MT

![Manage Routing Rule](images/routingrule1.png)

Para criar uma nova regra, clique no **"Adicionar nova regra MT"** Botão. Você será solicitado a configurar o seguinte:

#### 1. **Nome da Regra**
- Digite um nome amigável e descritivo para fácil identificação.

#### 2. **Tipo de Filtro**
- Dois tipos de filtro estão disponíveis:

##### **Passar pelo Filtro**
- Projetado para políticas globais de roteamento.
- Recomendado para criar uma regra de passagem de alta prioridade para servir como uma rota de retrocesso.

![Pass Through Filter](images/routingrule2.png)

##### **Filtro Personalizado**
- Mensagens de rota baseadas em parâmetros mais específicos:

![Custom Filter](images/routingrule3.png)

- **Código do país**: Selecione o país para rotear o tráfego de SMS.
- **MCC/MNC**: Escolha uma rede móvel específica do país selecionado.
- **Usuário**: Aplicar a regra a um usuário individual.
- **Grupo de Usuários**: Aplicar a regra a um grupo específico de usuários.
- **Data de início e data de fim**: Definir o período de validade da regra.
- **Endereço de origem**: Definir código-endereço–rote específico.
- **Endereço do destino**: Defina destino-endereço-rote específico.

---

### Políticas de Roteamento

Você pode definir políticas de roteamento com base em requisitos de negócios ou SLAs. As políticas de roteamento disponíveis incluem:

#### **LCR (Diminuição dos custos)**
- Rota o tráfego através do gateway do fornecedor oferecendo o menor custo configurado para um determinado destino.
- Ajuda a otimizar os preços e aumentar as margens de lucro.

#### **Porta fixa**
- Todo o tráfego é encaminhado através de um único gateway predefinido.

#### **Robin Redondo**
- Distribui tráfego uniformemente pelos gateways selecionados.
- Garante o uso ideal de todos os gateways configurados.

#### **Distribuído**
- Método avançado de balanceamento de carga.
- Conduz o tráfego para múltiplos gateways com base em rácios percentuais (por exemplo, 60%, 30%, 10%).

#### **ACD/DLR (entrega reconhecida)**
- Também conhecido como roteamento baseado em entrega.
- Conduz o tráfego para o gateway do fornecedor com a maior razão de entrega (DLR), garantindo o desempenho de qualidade em tempo real.

---

### Tratamento Prioritário

!!! info "Tratamento Prioritário"
 Se várias regras de roteamento correspondem a uma mensagem, **iTextPRO selecionará a regra com o maior valor de prioridade** (numericamente mais alto).

Esta poderosa lógica de roteamento garante que seu tráfego de SMS seja fornecido de forma eficiente, econômica e em conformidade com a lógica empresarial – sem necessidade de interrupções de serviço ou reinício do sistema.
