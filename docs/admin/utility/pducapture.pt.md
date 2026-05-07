
# Captura de PDU

A **Captura de PDU** opção é uma ferramenta poderosa para capturar **tráfego de mensagens ao vivo** entrando ou saindo da **Centro de Serviços de Mensagens Curtas (SMSC)**. 
É especificamente concebido para **Resolução de problemas em tempo real** do portal ou **Entidade de Mensagem Curta Externa (ESME)** utilizadores.

---

![PDU Capture Screenshot](images/pducapture1.png)

---

## Detalhes da Configuração

Para iniciar a captura de PDU, fornecer as seguintes informações:

- **Máquina** 
 Especificar o **endereço da máquina** ou **endereço IP do servidor** da interface Ethernet conectada ao servidor. 
 Isso identifica o caminho da rede para capturar PDUs.

- **Filtro** 
 Escolha o desejado **filtro** Começar a capturar PDUs vivos. 
 Por exemplo, selecionando **número do porto 8585** Capturarão PDUs apenas para esse porto específico. 
 Consulte a documentação para orientações detalhadas sobre captura de PDU com **porto 8585**.

- **Intervalo de tempo** 
 Introduza o intervalo de tempo desejado (em minutos), com **limite máximo de 90 minutos**. 
 Isso determina quanto tempo os PDUs vivos serão capturados.

---

## Nota
A **Captura de PDU** opção é uma ferramenta de diagnóstico inestimável para **Investigação em tempo real**. 
É especialmente útil para usuários que podem não ter acesso a uma equipe NOC ou possuir habilidades avançadas de solução de problemas de rede. 

Garantir que **detalhes da máquina**, **filtros**, e **intervalos de tempo** são configurados com precisão para obter resultados ótimos.
