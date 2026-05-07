
# Números da Lista Negra

A **Números da Lista Negra** o recurso permite que os administradores definam uma lista de números móveis que estão bloqueados em toda a aplicação. Quando um número é adicionado à lista negra, **todas as mensagens de saída para esse número são automaticamente rejeitadas pelo aplicativo**, e nenhum usuário será capaz de enviar mensagens para ele.

## Objecto

Este recurso é usado para evitar a entrega de mensagens para números restritos, inválidos, não conformes ou proibidos, a fim de manter a conformidade regulamentar e controlar o mau uso.

![Blacklist Numbers](images/blacklist2.png)

---

## Adicionando números à lista negra

1. Navegar para o **Números da Lista Negra** seção no painel de administração.
2. Clique em **Adicionar um Novo**.
3. Digite os números móveis no campo de entrada.
    - Vários números podem ser adicionados de uma só vez, separando-os com vírgulas (<span data-ph="0"></span>).
4. Garantir que **cada número móvel inclui o código do país** (por exemplo, +91XXXXXXXXXX).
5. Salve as alterações para aplicar os itens da lista negra em toda a aplicação.

![Add Blacklist Numbers](images/blacklist3.png)

---

## Excluindo números na lista negra

O aplicativo suporta **exclusão em massa**, permitindo que os administradores removam vários itens da lista negra em uma única operação.

Os administradores também podem **apagar os itens selecionados individualmente** Se necessário.

![Bulk Delete Blacklist](images/blacklist4.png)

---

## Comportamento de Tratamento de Mensagens

!!! warning "Mensagens Bloqueadas"
    - Qualquer mensagem enviada para um número na lista negra será **bloqueados ao nível da aplicação**.
    - O pedido de mensagem será **rejeitado imediatamente**, e não será transmitido ao vendedor.

!!! tip
 Certifique-se de que cada número móvel inclui o **Código do país** (por exemplo, +91XXXXXXXXXX) para uma funcionalidade correcta.
