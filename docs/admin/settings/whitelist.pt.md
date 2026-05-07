
# Números da Lista Branca

A **Números da Lista Branca** o recurso permite que os administradores definam uma lista global de números de celulares listados em branco. Quando **Compensação DLR** está habilitado no aplicativo, qualquer mensagem enviada para um número incluído na lista branca será sempre enviada ao vendedor e **não será considerado para compensação DLR**, independentemente do estado de entrega.

## Objecto

Este recurso é útil para excluir números específicos (como números de teste, números de monitoramento interno ou contatos de prioridade) da lógica de compensação, garantindo a entrega ininterrupta de mensagens.

![White List Numbers](images/whitelist1.png)

---

## Adicionando Números à Lista Branca

1. Navegar para o **Números da Lista Branca** seção do painel de administração.
2. Clique em **Adicionar um Novo**.
3. Digite os números móveis no campo de entrada.
4. Vários números podem ser adicionados de uma só vez, separando-os com vírgulas (<span data-ph="0"></span>).
5. Garantir que **cada número móvel inclui o código do país** (por exemplo, +91XXXXXXXXXX).
6. Salve as alterações para aplicar globalmente os itens da lista branca.

![Add Whitelist Numbers](images/whitelist2.png)

---

## Excluindo números na lista branca

O aplicativo suporta **exclusão em massa**, permitindo que os administradores removam vários itens da lista branca em uma única ação.

Administradores também podem excluir **itens selecionados individualmente** Se necessário.

![Bulk Delete Whitelist](images/whitelist4.png)

---

## Notas-chave

!!! info "Importante"
    - Números listados em branco são aplicados **globalmente em toda a aplicação**.
    - As mensagens enviadas para estes números são **Excluídos dos cálculos de compensação DLR**.
    - Formatação adequada com códigos de país é obrigatória para a funcionalidade correta.
