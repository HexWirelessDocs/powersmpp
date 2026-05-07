
# Gerenciar o Prefixo

A **Gerenciar o Prefixo** o recurso no iTextPRO é projetado para lidar eficientemente com prefixos de números móveis associados a países específicos e operadores de rede. Desempenha um papel importante na garantia de um mapeamento e faturamento precisos da rede.

---

## Caso de uso para gerenciar prefixos

### Considerações sobre a estrutura de faturamento

#### Faturação baseada na rede (MCC-MNC)
- **Prefixo como parâmetro de mapeamento** – Quando o faturamento é baseado em rede (MCC-MNC), adicionar prefixos é crucial. Prefixos atuam como parâmetros de mapeamento para identificar padrões de faturamento em rede com precisão.
- **Precisão de faturamento aprimorada** – O gerenciamento de prefixo garante que o sistema de faturamento se alinha com as configurações de rede específicas ligadas aos códigos MCC-MNC.

#### Cobrança por País
- **Sem necessidade de gerenciamento de prefixos** – Para faturamento plano, por país, prefixos não são necessários. A cobrança é feita diretamente com base em códigos de país.
- **Processo de faturamento simplificado** – O sistema cobra transações usando apenas o código do país, simplificando o processo.

![Manage Prefix Overview](images/manageprefix1.png)

---

## Adicionando Novos Prefixos

![Add Prefix](images/manageprefix2.png)

1. **Seleção de País e Operador** – Selecione o país desejado e o operador de rede associado.
2. **Prefixo** – Colar ou inserir manualmente o prefixo (sem o código do país) na caixa de entrada.
3. **Adicionar ou Substituir Opções** - Não. 
   - Selecionar **Sim.** para adicionar o novo prefixo à lista existente. 
   - Selecionar **Não** para substituir inteiramente a lista de prefixos existente.
4. **Apresentação** – Clique **Enviar** para finalizar a importação de prefixo.

---

## Verificar a Funcionalidade Prefixa

![Verify Prefix](images/manageprefix3.png)

A **Verificar o Prefixo** ferramenta fornece detalhes de rede rápida para um determinado número de celular.

1. **Digite o Número Móvel** – Introduza o número que deseja verificar.
2. **Visualização do Resultado** – O sistema mostra:
   - Nome do país
   - Nome da rede
   - MCC-MNC

Isso ajuda a confirmar a precisão dos detalhes de número de celular e informações de rede associadas.
