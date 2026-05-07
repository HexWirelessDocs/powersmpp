

# Permissões

## Privilégios Executivos de Papel da Conta no iTextPRO

In **iTextPRO**, administradores e revendedores podem conceder privilégios específicos a **Executivos de Funções da Conta**, adaptando o seu acesso às áreas de trabalho designadas. 
Vários papéis executivos podem ser criados para acomodar diversas responsabilidades.

### Funções de Exemplo

**Papel da equipe de finanças**
- Acesso à Secção de Cobrança
- Acesso à Secção de Relatórios
- Outros privilégios relevantes

**Papel da Equipe NOC**
- Acesso ao Registo de Monitorização
- Acesso à Secção de Relatórios
- Opções de administração
- Outros privilégios relevantes

**Procedimentos de Login:**
- **Executivo do administrador:** Use o URL e porta de login do administrador.
- **Executivo do revendedor:** Use o URL de login e porta do revendedor.

Essa segregação garante uma experiência de login segura e específica para executivos, simplificando o acesso a funcionalidades alinhadas com suas responsabilidades.

![Permission Example](images/permission1.png)

---

## Categorias de Permissão

Permissões para usuários executivos no iTextPRO são categorizadas com base no nível de acesso e ações dentro de módulos.

### Categorias

**Ver** 
- Pode visualizar o conteúdo dentro do módulo especificado. 
- *Não são permitidas modificações ou exclusões.*

**Adicionar** 
- Pode adicionar novos itens ao módulo. 
- *Não foi possível editar ou excluir os itens existentes.*

**Editar** 
- Pode editar/atualizar os itens existentes. 
- *Sem direitos de eliminação.*

**Apagar** 
- Pode apagar entradas do módulo. 
- *Sem direitos de edição.*

**Controle completo** 
- Permite visualizar, adicionar, editar e excluir direitos para o módulo especificado. 
- Acesso irrestrito.

![Permission Categories](images/permission2.png)

---

## Controle completo e hierarquia

In **iTextPRO**, **Controle completo** proporciona acesso abrangente.

**Cenários de ativação:**
1. Ativando o controle completo no **nível superior** concede-o automaticamente a todos os submódulos.
2. Habilitando - o para uma **módulo específico** capas Ver, Adicionar, Editar e Apagar.

**Hierarquia:**
- Os níveis representam diferentes seções, funcionalidades ou categorias de dados.
- Controle total em cascatas de nível superior para todos os sub-níveis.

**Desactivação Explícita:**
- Permissões específicas em submódulos podem ser desabilitadas manualmente, mesmo com controle completo.

![Permission Hierarchy](images/permission3.png)

---

## Tipos de Permissão

### Permissões individuais do usuário
- Concede permissões a um usuário executivo específico.

**Procedimento:**
1. Ir para **Gerenciar Permissão** Page.
2. Selecionar **Individual** como tipo de permissão.
3. Escolha um usuário na lista.
4. Clique **Mostrar** para ver/gerir permissões.

![Individual Permissions](images/permission4.png)

---

### Permissões do Grupo de Usuário Executivo
- Concede permissões a um grupo; herdado por todos os membros do grupo.

**Procedimento:**
1. Ir para **Gerenciar grupos de usuários executivos** Page.
2. Clique **Adicionar grupo de usuários**.
3. Indique o nome do grupo e seleccione os utilizadores.
4. Salvem o grupo.
5. Utilização **Total de Utilizadores** Ver os membros.
6. Editar ou excluir grupos conforme necessário.

□ *Se um executivo tem permissões específicas do usuário e do grupo, eles obtêm ambas.*

![Group Permissions](images/permission5.png)

---

## Visibilidade do Módulo

- Se um Executivo não tiver permissões, **"Acesso negado"** página após login.
- Se as permissões forem revogadas durante o login, as ações serão exibidas **"Acesso negado"**.
- Os módulos são exibidos sequencialmente com base em permissões concedidas.

Exemplo: 
- Se **Configuração** e **Faturação** são concedidos, apenas esses módulos aparecem.

![All Modules](images/permission6.png) 
![Filtered Modules](images/permission7.png)