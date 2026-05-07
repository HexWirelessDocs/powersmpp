---
tags:
  - SMPP
  - Error Codes
  - Reference
  - Gateway
---

# Lista de códigos de erro SMPP padrão

Esta página fornece uma referência completa de todos os códigos de erro de protocolo SMPP, códigos de erro de aplicação iTextPro e códigos de erro de gateway HTTP do iTextHub. Use esta referência para diagnosticar falhas de entrega de mensagens vistas em relatórios, registros de PDU e visualizadores de eventos.

---

## Códigos de Erro Padrão SMPP

São códigos de erro de nível de protocolo definidos pela especificação SMPP v3.4. Eles são devolvidos pelo SMSC (Short Message Service Centre) em resposta às operações SMPP.

| Não | Código de Erro (Hex) | Código de Erro (Decimal) | Nome do Erro | Descrição do Erro |
|--------|-----------------|---------------------|------------|-------------------|
| 1 | 0x00 | 0 | Comando executado com sucesso | O comando SMPP foi processado sem erros |
| 2 | 0x01 | 1 | O comprimento da mensagem é inválido | O comprimento do corpo da mensagem excede os limites permitidos |
| 3 | 0x02 | 2 | O comprimento do comando é inválido | O campo de comprimento do comando PDU está incorreto |
| 4 | 0x03 | 3 | ID de Comando Inválido | O ID de comando não é reconhecido pelo SMSC |
| 5 | 0x04 | 4 | Estado do BIND incorreto para o comando fornecido | O ESME tentou um comando que não é permitido no seu estado de ligação atual |
| 6 | 0x05 | 5 | ESME já em estado fechado | O ESME já está ligado e não pode voltar a ligar |
| 7 | 0x06 | 6 | Bandeira Prioritária Inválida | O valor da bandeira de prioridade no PDU não é válido |
| 8 | 0x07 | 7 | Bandeira de Entrega Registrada Inválida | O valor da bandeira de entrega registada não é válido |
| 9 | 0x08 | 8 | Erro no Sistema | Ocorreu um erro geral no sistema SMSC |
| 10 | 0x0A | 10 | Endereço de origem inválido | O endereço de origem (enviar) é inválido ou não é permitido |
| 11 | 0x0B | 11 | Endereço de destino inválido | O endereço de destino (receptor) é inválido |
| 12 | 0x0C | 12 | ID da mensagem é inválido | O ID da mensagem referenciado não existe |
| 13 | 0x0D | 13 | Falha na ligação | A operação de vinculação falhou devido a problemas de autenticação ou configuração |
| 14 | 0x0E | 14 | Senha inválida | A senha fornecida durante a ligação está incorreta |
| 15 | 0x0F | 15 | ID do sistema inválido | O ID do sistema fornecido durante a ligação não é reconhecido |
| 16 | 0x11 | 17 | Cancelar SM Falhou | A operação cancel sm não pôde ser concluída |
| 17 | 0x13 | 19 | Substituir o SM Falhou | A operação substitut sm não pôde ser concluída |
| 18 | 0x15 | 21 | Tipo de serviço inválido | O parâmetro service type não é válido |
| 19 | 0x33 | 51 | Número inválido de destinos | O número de destinos no submit multi é inválido |
| 20 | 0x34 | 52 | Nome da lista de distribuição inválido | O nome da lista de distribuição referenciada não existe |
| 21 | 0x40 | 64 | A bandeira do destino é inválida (submit multi) | O dest flag no submit multi contém um valor inválido |
| 22 | 0x42 | 66 | Enviar w/substituir não suportado | Enviar com funcionalidade de substituição foi solicitado quando não é suportado ou inadequado para o MC específico |
| 23 | 0x43 | 67 | Dados de campo esm class inválidos | O campo esm class contém dados inválidos |
| 24 | 0x44 | 68 | Não foi possível enviar para a lista de distribuição | A mensagem não pode ser enviada para a lista de distribuição especificada |
| 25 | 0x45 | 69 | send sm, data sm ou submit multi falhou | A operação de envio falhou |
| 26 | 0x48 | 72 | Endereço de origem inválido TON | O Tipo de Número para o endereço de origem é inválido |
| 27 | 0x49 | 73 | Endereço de origem inválido NPI | O indicador do plano de numeração do endereço de origem é inválido |
| 28 | 0x51 | 81 | Endereço de destino inválido NPI | O indicador do plano de numeração para o endereço de destino é inválido |
| 29 | 0x53 | 83 | Campo tipo de sistema inválido | O parâmetro system type não é válido |
| 30 | 0x54 | 84 | Bandeira inválida de substituição  se  presente | A bandeira substitut if presente contém um valor inválido |
| 31 | 0x55 | 85 | Número de mensagens inválido | O parâmetro número de mensagens é inválido |
| 32 | 0x58 | 88 | Erro de Throttling | ESME ultrapassou os limites permitidos de mensagens (TPS) |
| 33 | 0x61 | 97 | Tempo de entrega agendado inválido | O formato ou valor do tempo de entrega agendado é inválido |
| 34 | 0x62 | 98 | Período de validade da mensagem inválido | O período de validade da mensagem (tempo de expiração) é inválido |
| 35 | 0x63 | 99 | O ID da mensagem predefinido é inválido | A mensagem predefinida especificada não foi encontrada |
| 36 | 0x65 | 101 | Código de erro de aplicação permanente do receptor ESME | Um erro de aplicação permanente no receptor ESME |
| 37 | 0x66 | 102 | Código de Erro de Rejeição do Receptor ESME | O receptor ESME rejeitou a mensagem |
| 38 | 0x67 | 103 | Falha na requisição do Sm | A operação query sm não pôde ser concluída |
| 39 | 0xC0 | 192 | Erro na parte opcional do corpo PDU | Os parâmetros TLV facultativos no corpo PDU contêm erros |
| 40 | 0xC1 | 193 | TLV não permitido | O parâmetro TLV não é permitido para esta operação |
| 41 | 0xC2 | 194 | Comprimento do parâmetro inválido | Um parâmetro TLV tem um comprimento inválido |
| 42 | 0xC3 | 195 | TLV esperado em falta | Falta um parâmetro TLV necessário no PDU |
| 43 | 0xC4 | 196 | Valor TLV inválido | Um parâmetro TLV contém um valor inválido |
| 44 | 0xFE | 254 | Falha na entrega da transação | A transação de mensagem não pôde ser entregue |
| 45 | 0xFF | 255 | Erro Desconhecido | Ocorreu um erro desconhecido ou não especificado |
| 46 | 0x100 | 256 | ESME Não autorizado a utilizar o tipo de serviço especificado | O ESME não está autorizado para o tipo de serviço solicitado |
| 47 | 0x101 | 257 | ESME Proibido de usar a operação especificada | O ESME está na lista negra ou proibido de utilizar a operação especificada |
| 48 | 0x102 | 258 | O tipo de serviço especificado não está disponível | O tipo de serviço solicitado está atualmente indisponível |
| 49 | 0x103 | 259 | O tipo de serviço especificado é negado | O tipo de serviço solicitado foi negado |
| 50 | 0x105 | 261 | A Subunidade de Endereço de Origem é Inválida | O parâmetro sub- unidade do endereço de origem é inválido |
| 51 | 0x106 | 262 | A Subunidade de Endereço de Destino é Inválida | O parâmetro sub- unidade do endereço de destino é inválido |
| 52 | 0x107 | 263 | Intervalo de Frequência de Transmissão é inválido | O parâmetro intervalo de frequência de transmissão é inválido |
| 53 | 0x108 | 264 | Nome do Apelido de Transmissão é inválido | O nome do apelido de difusão não é válido |
| 54 | 0x109 | 265 | O formato da área de transmissão é inválido | O parâmetro de formato da área de transmissão é inválido |
| 55 | 0x10A | 266 | O número de áreas de transmissão é inválido | O número de áreas de difusão especificadas é inválido |
| 56 | 0x10B | 267 | O tipo de conteúdo de transmissão é inválido | O parâmetro tipo de conteúdo de transmissão é inválido |
| 57 | 0x10C | 268 | Classe de mensagem de transmissão é inválida | A classe de mensagem de transmissão é inválida |
| 58 | 0x10D | 269 | Falha na operação de transmissão | Não foi possível completar a operação de transmissão sm |
| 59 | 0x10F | 271 | Falha na operação Cancel broadcast sm | A operação cancel broadcast sm não pôde ser concluída |
| 60 | 0x110 | 272 | O número de transmissões repetidas é inválido | O número de emissões repetidas é inválido |
| 61 | 0x111 | 273 | O Grupo de Serviços de Transmissão é inválido | O parâmetro do grupo de serviços de radiodifusão é inválido |
| 62 | 0x112 | 274 | Indicador de canal de transmissão é inválido | O indicador de canal de transmissão é inválido |
| 63 | 0x15F95 | 90005 | Exceção local | Verifique a propriedade LastException para obter detalhes |

---

## Códigos de Erro iTextPro

Estes são códigos de erro de nível de aplicação gerados pela plataforma SMPP iTextPro / Power. Eles indicam problemas com roteamento, faturamento, configuração de conta ou operações do sistema.

| Não | Código de Erro (Hex) | Código de Erro (Decimal) | Nome do Erro | Descrição do Erro |
|--------|-----------------|---------------------|------------|-------------------|
| 64 | 0x439 | 1081 | País Undef | País não definido pelo administrador no Master Data Manager |
| 65 | 0x43A | 1082 | Rede inválida | Rede não definida pelo administrador no Master Data Manager |
| 66 | 0x43B | 1083 | Preço Indefinido | Preços não definidos pelo administrador para o respectivo país e rede no gateway primário |
| 67 | 0x43C | 1084 | Expirado (proteção perdida) | Mensagem não entregue devido à política de proteção contra perdas |
| 68 | 0x43D | 1085 | Rota Indefinida | Roteamento não definido pelo administrador para o respectivo país e rede |
| 69 | 0x43E | 1086 | Falha na Rota Indefinida | Failover mestre não definido pelo administrador para o respectivo país e rede |
| 70 | 0x43F | 1087 | Fracasso expirou | Mensagem não entregue devido à Proteção de Perdas no gateway failover |
| 71 | 0x440 | 1088 | Preço de falha Indefinição | Preços não definidos pelo administrador para o respectivo país e rede no gateway failover |
| 72 | 0x441 | 1089 | Falhar | Erro do sistema: Exceção não manuseada durante o roteamento do failover |
| 73 | 0x442 | 1090 | Validade da Conta Expirada | A validade da conta de usuário expirou |
| 74 | 0x443 | 1091 | Erro de Codificação | Erro do Sistema: Erro de codificação devido ao valor de codificação de dados inválido (pode ser regenerado enviando valores de codificação de dados exceto 0 & 8) |
| 75 | 0x444 | 1092 | Erro de OA/DA | Erro do Sistema: Erro OA/DA devido ao Regex inválido nas regras de normalização |
| 76 | 0x445 | 1093 | A mensagem da fila terminou | Erro do sistema: A mensagem da fila expirou devido à interrupção prolongada do gateway |
| 77 | 0x446 | 1094 | Configuração inválida do Gateway HTTP | Erro do sistema: Configuração ou código de resposta HTTP inválido |
| 78 | 0x417 | 1047 | Inativo da Conta de Usuário | A conta do usuário está inativa e não pode enviar mensagens |
| 79 | 0x400 | 1024 | Conta de usuário bloqueada | A conta de usuário foi bloqueada pelo administrador |
| 80 | 0x401 | 1025 | Saldo insuficiente | Saldo insuficiente na conta de utilizador (pré-pago) |
| 81 | 0x402 | 1026 | Mistura de Modelos | Modelo de erro detectado — o conteúdo da mensagem não corresponde ao modelo aprovado |
| 82 | 0x405 | 1029 | ID do remetente inválido | ID do remetente inválido ou não aprovado detectado |
| 83 | 0x407 | 1031 | Número da Lista Negra Global | O número de destino está na lista negra global |
| 83 | 0x40B | 1035 | Sem conexão ativa | Nenhuma conexão SMPP ativa disponível para o gateway |
| 84 | 0x40C | 1036 | Erro no Servidor em Fila | Erro do sistema: erro interno da fila de mensagens |
| 85 | 0x40D | 1037 | Erro no Servidor de Cache | Erro do sistema: erro na base de dados de cache |
| 86 | 0x40E | 1038 | Estado de Ligação Inválido | Erro de rede: Gateway não acessível |
| 87 | 0x40F | 1039 | Tempo limite de SMPP | Erro de rede: Tempo limite de gateway — nenhuma resposta recebida |
| 88 | 0x410 | 1040 | Erro SMPP desconhecido | Erro do sistema: Ocorreu um erro SMPP não classificado |
| 89 | 0x411 | 1041 | Desconexão final | A conexão SMPP foi desconectada permanentemente |
| 90 | 0x412 | 1042 | Tempo- limite final | A conexão cronometrada permanentemente |
| 91 | 0x413 | 1043 | Nenhuma Porta Encontrada | Nenhum gateway adequado encontrado para rotear a mensagem |
| 92 | 0x404 | 1028 | IP inválido | Endereço IP inválido para conta SMPP (a validação IP falhou) |
| 93 | 0x414 | 1044 | Spam Detectado | A mensagem falhou devido à palavra- chave de spam detectada no conteúdo |
| 94 | 0x448 | 1096 | Duração da Mensagem Excedida | O comprimento da mensagem SMS excedeu o limite permitido |

---

## Códigos de Erro do Gateway HTTP do iTextHub

Estes códigos de erro são devolvidos pelo Gateway HTTP do iTextHub ao processar solicitações de API HTTP.

| Não | Código de Erro (Decimal) | Nome do Erro | Descrição do Erro |
|--------|---------------------|------------|-------------------|
| 95 | 110 | Erro ao obter resposta de texto | Falha ao obter a resposta de texto do gateway HTTP |
| 96 | 111 | Erro ao obter resposta JSON/XML | Falha ao processar a resposta JSON ou XML do gateway HTTP |
| 97 | 112 | Erro ao ler a resposta | Falha ao ler o fluxo de resposta HTTP |
| 98 | 113 | Erro ao ler a resposta do resultado | Falha ao extrair dados do resultado da resposta HTTP |
| 99 | 114 | Erro ao solicitar a API REST/JSON | Falha ao fazer uma solicitação de API REST/JSON para o gateway HTTP |
| 100 | 115 | Erro ao solicitar API HTTP Simples | Falha ao fazer uma solicitação simples de API HTTP para o gateway HTTP |
| 101 | 116 | Erro ao solicitar a API SOAP | Falha ao fazer uma solicitação de API SOAP para o gateway HTTP |
| 102 | 1095 | Erro ao solicitar a API SOAP/Simples/RestJson | Código de erro combinado para 114, 115 e 116 (utilizado na última versão) |

---

!!! tip "Como utilizar esta referência"
    - Quando você vê um código de erro em seu **Relatórios de Campanha**, **Registos PDU**, ou **Visualizador de eventos**, pesquise nas tabelas acima
    - **Códigos SMPP normalizados** (0–255) são devolvidos pelo SMSC/gateway externo
    - **Códigos iTextPro** (1024-1096) são gerados internamente pela plataforma Power SMPP
    - **Códigos HTTP GW** (110-1095) se relacionam com problemas de conectividade de gateway HTTP
    - Para configuração do código de erro específico do gateway, consulte [Códigos de Erro do Gateway](errorcode.md)
