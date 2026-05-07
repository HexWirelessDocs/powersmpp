---
tags:
  - Billing
  - Rate Plan
  - Pricing
---

# Faturação

## Gerenciamento de faturamento simplificado com iTextPRO

Agregadores na indústria de SMS muitas vezes enfrentam desafios na gestão **vários gateways**, **diversas estruturas de preços**, e **Operações internacionais**. 
A **Módulo de cobrança iTextPRO** aborda esses desafios com recursos avançados que garantem operações simplificadas, precisas e lucrativas.

---

## 1. Configuração da Moeda de Base

- **Importância**: Garante coerência e precisão nas transações financeiras.
- **Recomendação**: Euro (EUR) é amplamente utilizado na indústria global de agregação SMS.
- **Considerações**: Uma vez que a moeda base é definida, mudando-a pode ser complexa. Decida no início da jornada de negócios.

---

## 2. Compreendendo os códigos MCC e MNC

- **MCC (Código do país móvel)** e **MNC (Código da rede móvel)** são cruciais para a personalização de preços baseados em redes móveis dentro de um país.
- **Preços do operador**: Muitos operadores de telecomunicações baseiam seus preços em combinações MCC + MNC.
- **Flexibilidade**: iTextPRO habilita **Preço específico da rede** para uma maior otimização de receita.

---

## 3. Entendendo Prefixo para números móveis de engenharia reversa

- **Objecto**: Identifica a origem e a rede de um número móvel.
- **Prefixo**: Os primeiros 3-4 dígitos ajudam a detectar **Código do país** e **Rede móvel**.
- **Exemplo**: 
  - Número: <span data-ph="0"></span> 
  - Código do país: <span data-ph="0"></span> (EAU) 
  - Com preço fixo: Cálculo de custos é simples. 
  - Com preços MCC/MNC: É necessária uma pesquisa adicional (nenhuma ferramenta atual fornece MCC/MNC diretamente a partir deste número).

![Manage Countries](images/managecountries1.png)

---

## 4. Conversão de moeda

- **Moeda de base**: Usado para transações internas.
- **Exibir moeda**: Os usuários podem visualizar transações em sua moeda preferida.
- **Benefício**: Simplifica as operações internacionais mantendo a precisão contábil.

---

## 5. Política de proteção contra perdas

- **Ferramenta de Fuga de Receitas**: Identifica potenciais perdas de receita em tempo real.
- **Medidas preventivas**: Para transações causadas por erros de digitação, manipulação de números ou erros de administração.
- **Salvaguarda financeira**: Protege contra a perda de receita e garante a precisão de faturamento.

---

## Principais Benefícios

- **Simplificação operacional** – Facilitando faturamento global de SMS. 
- **Preços precisos** – Controle de nível de rede para preços competitivos. 
- **Limpar o Tratamento da Moeda** – Base sem costura e gerenciamento de moeda. 
- **Segurança financeira** – Políticas automatizadas de prevenção de perdas. 

---

# Gestor de Dados Mestre

A **Gestor de Dados Mestre** a seção contém quatro opções de configuração chave:

1. **Gerir os Países** 
2. **Gerenciar MCC/MNC** 
3. **Gerenciar o Prefixo** 
4. **Gerenciar o Preço do Gateway**

---

## 1. Gerir os Países

A **Gerir os Países** o recurso permite a configuração e gerenciamento da terminação de tráfego SMS em vários países.

![Manage Countries](images/managecountries2.png)

### Adicionar um País Único

- **Nome do país** – Nome completo do país para identificação clara. 
- **Código do país** – Identificador único para roteamento. 
- **País Código ISO** – Código padronizado para compatibilidade global. 
- **Adicionar um Processo** – Clique **Adicionar** Incluir o país na lista principal.

![Single Country Add](images/managecountries3.png)

---

### Funcionalidade de envio em massa

![Bulk Upload](images/managecountries4.png)

- **Baixar Exemplo de Excel** – Pré-formatado com todos os países para fácil edição. 
- **Escolher Arquivo e Envio** – Suporta várias entradas ao mesmo tempo. 
- **Mapeamento de Colunas** – Mapear campos Excel para **Nome do país**, **ISO**, e **Código**. 
- **Enviar & visualização** – Bulk adicionar países e personalizar exibição de registro.

![Bulk Upload Results](images/managecountries5.png)

---

### Característica de Ação

![Action Options](images/managecountries6.png)

- **Editar** – Atualizar os detalhes existentes. 
- **Actualizar** – Atualizar dados do país. 
- **Apagar** – Remover entradas não utilizadas. 

---

**Melhores práticas:** 
Revise regularmente e atualize seu **Gestor de Dados Mestre** para garantir que as configurações de país e rede permaneçam precisas para preços e roteamento.
