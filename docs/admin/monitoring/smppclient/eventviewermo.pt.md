---
tags:
  - Monitoring
  - MO
  - Event Viewer
---

# Visualizador de eventos (MO) — móvel originado

**Navegação:** <span data-ph="0"></span> □ <span data-ph="1"></span> □ <span data-ph="2"></span>.

## Visão geral

A **Visualizador de eventos (MO)** a secção é usada para monitorizar **Móvel Originado (MO)** mensagens e eventos de sistema relacionados dentro PowerSMPP. Mensagens MO são mensagens de entrada recebidas de um fornecedor de gateway ou usuário final direcionado para o aplicativo.

---

## Objecto

O Visualizador de Eventos (MO) ajuda os administradores a monitorar, auditar e solucionar problemas em todas as atividades relacionadas ao MO no sistema.

!!! info "Casos de Uso Primário"
    - Monitorização da atividade da mensagem MO em tempo real
    - Verificando os logs de comunicação de usuários ou fornecedores
    - Resolução de problemas de entrega ou roteamento relacionados ao MO
    - Revisão de eventos MO gerados pelo sistema
    - Verificação dos registos de comunicações de gateway para o tráfego de entrada

---

## Informação disponível

O módulo exibe os seguintes campos para cada registro:

| Campo | Designação das mercadorias |
|-------|-------------|
| **Tempo** | Data exata do evento MO. |
| **Tipo de Registo** | Classificação do evento — <span data-ph="0"></span> ou <span data-ph="1"></span>. |
| **Mensagem** | Descrição do evento ou atividade MO. |

![Event Viewer (MO) — Info log entries](images/eventmo-01-info.png)

![Event Viewer (MO) — Error log type (no entries shown)](images/eventmo-02-error.png)

---

## Tipos de Registo

| Tipo de Registo | Designação das mercadorias |
|----------|-------------|
| **Informação** | Eventos de sistema informativo, mudanças de gateway bem-sucedidas, atualizações de lista de usuários. |
| **Erro** | Eventos de nível de erro indicando falhas, mensagens MO rejeitadas ou exceções do sistema. |

---

## Características

!!! info "Capacidades do Visualizador de Eventos (MO)"
    - Ver registros de eventos MO em tempo real.
    - Monitore gateway e atividades de entrada do usuário.
    - Acompanhe os pedidos de mensagem MO.
    - Resolver problemas relacionados com o MO.
    - Atualizar logs sob demanda usando o **Atualizar** Botão.
    - Registos de filtros por **tipo de registo** (Info / Erro).
    - Registos de filtros por **intervalo de datas** para revisão histórica.

---

## Filtro de Intervalo de Datas

Os administradores podem selecionar um intervalo de datas específico para recuperar **histórico MO logs de eventos**. Isto suporta a resolução retrospectiva de problemas, auditoria de conformidade e revisão operacional.

!!! tip
 Ao perseguir um problema intermitente, definir **Tipo de Registo = Erro** primeiro focar apenas em falhas, em seguida, ampliar para **Tudo** se não houver eventos de erro visíveis durante a janela.
