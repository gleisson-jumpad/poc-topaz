# 18. GLOSSÁRIO DE SIGLAS E TERMOS TÉCNICOS

> Referência rápida de siglas e termos usados nesta base de conhecimento e no dia a dia de vendas de tecnologia financeira.

## Siglas Regulatórias e de Compliance

| Sigla | Significado | Contexto |
|---|---|---|
| **BACEN** | Banco Central do Brasil | Regulador do sistema financeiro brasileiro; define normas de operação bancária, pagamentos e reportes |
| **PCI-DSS** | Payment Card Industry Data Security Standard | Padrão global de segurança para processamento de cartões; obrigatório para quem transaciona com bandeiras |
| **LGPD** | Lei Geral de Proteção de Dados (Brasil) | Regulamentação de proteção de dados pessoais; impacta armazenamento e tratamento de dados de clientes |
| **PLD/FT** | Prevenção à Lavagem de Dinheiro e Financiamento ao Terrorismo | Obrigação legal de monitoramento e reporte de operações suspeitas; SecureJourney cobre essa necessidade |
| **AML** | Anti-Money Laundering | Equivalente internacional de PLD; framework para prevenção à lavagem de dinheiro |
| **CFT** | Combate ao Financiamento do Terrorismo | Complemento de AML; regulações para prevenir uso do sistema financeiro para fins de terrorismo |
| **KYC** | Know Your Customer | Processo de identificação e verificação de clientes; essencial no onboarding e na originação |
| **PSTI** | Provedor de Serviço de Tecnologia para Instituições financeiras | Certificação que credencia prestadores de serviço de tecnologia para o setor financeiro; TechPay é o primeiro certificado |
| **ISO 9001** | Sistema de Gestão da Qualidade | Certificação de processos padronizados e qualidade; a Topaz possui |
| **ISO 27001** | Sistema de Gestão de Segurança da Informação | Certificação de segurança da informação; a Topaz possui |
| **ISO 27701** | Gestão de Privacidade da Informação | Extensão da ISO 27001 para proteção de dados pessoais; a Topaz possui |
| **iBeta** | Laboratório independente de certificação biométrica | Certificação que valida a qualidade de autenticação facial; SecureJourney é certificada |

## Siglas Técnicas e de Arquitetura

| Sigla | Significado | Contexto |
|---|---|---|
| **API** | Application Programming Interface | Interface de comunicação entre sistemas; essencial para integração entre produtos Topaz e sistemas de terceiros |
| **REST** | Representational State Transfer | Padrão de arquitetura de APIs; as APIs da Topaz seguem REST |
| **K8s** | Kubernetes | Orquestrador de contêineres; usado na infraestrutura de deploy da Topaz |
| **BPM** | Business Process Management | Gestão de processos de negócio; usado no FinancialCore para fluxos operacionais |
| **JMS** | Java Message Service | Serviço de mensageria assíncrona em Java; usado na comunicação entre microserviços |
| **SaaS** | Software as a Service | Modelo de entrega onde o software é acessado via nuvem com mensalidade |
| **PaaS** | Platform as a Service | Modelo que fornece a plataforma e infraestrutura; mais autonomia técnica para o cliente |
| **CAPEX** | Capital Expenditure | Modelo de investimento inicial (licenciamento) seguido de manutenção anual |
| **TCO** | Total Cost of Ownership | Custo total de propriedade; inclui licença, implementação, manutenção, infraestrutura e operação |
| **ROI** | Return on Investment | Retorno sobre o investimento; métrica-chave para CFOs avaliarem projetos |
| **BaaS** | Banking as a Service | Modelo onde infraestrutura bancária é oferecida como serviço via APIs para terceiros |

## Termos de Negócio Financeiro

| Termo | Significado | Contexto |
|---|---|---|
| **Core Banking** | Sistema central que processa operações bancárias | Contas, transações, crédito, câmbio, compliance; FinancialCore é o core da Topaz |
| **Full Banking** | Plataforma que cobre todas as necessidades de operação bancária | Diferencial da Topaz One — não é só core, é core + canais + fraude + pagamentos + investimentos + originação + automação |
| **Open Finance** | Ecossistema de compartilhamento de dados financeiros entre instituições | Regulado pelo BACEN; a Topaz integra nativamente |
| **Open Banking** | Precursor do Open Finance; compartilhamento de dados bancários | Conceito mais restrito que evoluiu para Open Finance no Brasil |
| **Embedded Finance** | Serviços financeiros embutidos em plataformas não-financeiras | Varejo, telecom, utilities oferecendo crédito, pagamento, seguros dentro de seus apps |
| **Omnichannel** | Experiência unificada em todos os canais | Mobile, internet banking, agência, ATM, chatbot, POS — todos conectados pelo FinChannels |
| **Churn** | Taxa de cancelamento ou abandono de clientes | FinXperience atua na retenção preditiva para reduzir churn |
| **Time-to-Market** | Tempo entre concepção e lançamento de um produto | Topaz Open e FinOrigination aceleram o time-to-market |
| **Low-code** | Desenvolvimento com pouca ou nenhuma codificação | FinancialCore permite parametrização low-code para autonomia do cliente |
| **Lock-in** | Dependência tecnológica de um fornecedor | APIs abertas e microserviços da Topaz reduzem o risco de lock-in |
| **Wallet Digital** | Carteira digital para pagamentos e transferências | TechPay + FinancialCore habilitam operações de wallet |
| **NDF** | Non-Deliverable Forward | Derivativo cambial; gerenciado pelo TechInvest |
| **CDB** | Certificado de Depósito Bancário | Produto de renda fixa; processado pelo TechInvest |
| **LCI/LCA** | Letra de Crédito Imobiliário / do Agronegócio | Títulos de renda fixa incentivados; gerenciados pelo TechInvest |
| **CRI/CRA** | Certificado de Recebíveis Imobiliários / do Agronegócio | Securitização de recebíveis; gerenciados pelo TechInvest |
| **Consórcio** | Grupo de autofinanciamento | Modalidade brasileira de aquisição de bens; FinancialCore possui ERP de Consórcio |

## Termos Topaz Específicos

| Termo | Significado | Contexto |
|---|---|---|
| **Topaz One** | Plataforma full banking da Topaz | Ecossistema que integra as 8 famílias de produtos |
| **Topaz Open** | Versão padronizada do core banking | Focada em fintechs e operações que precisam de go-to-market acelerado |
| **FinancialCore** | Core banking universal da Topaz | 4 sub-produtos: Core Universal, Core Digital, Core Microfinanças, ERP Consórcio |
| **SecureJourney** | Plataforma de antifraude e segurança | Módulos: Decision Manager, Onboarding Seguro, Prevenção a Fraudes, PLD/FT |
| **FinChannels** | Plataforma de canais omnichannel | Orquestrador de Canais, Canais Digitais, Canais Físicos, Serviços Especializados |
| **FinXperience** | Experiência personalizada com IA | Retenção e Fidelização, Open Experiences, motor de recomendação inteligente |
| **TechPay** | Orquestração de pagamentos | Moedas Digitais, Pagamentos Instantâneos, certificação PSTI |
| **TechInvest** | Gestão de investimentos | Renda Fixa, Renda Variável, Fundos, Derivativos, Wealth Management |
| **FinOrigination** | Originação digital de produtos | Originação Digital, Originação em Campo, Aceite Eletrônico |
| **BankingTools** | Automação financeira e de TI | Ferramentas de TI e Automação, Regulatório e Contábil |

## Analistas e Reconhecimentos

| Nome | Significado | Contexto |
|---|---|---|
| **Gartner** | Empresa global de pesquisa e consultoria em TI | Reconhece a Topaz como player relevante em tecnologia financeira |
| **Forrester** | Empresa global de pesquisa em tecnologia | Avalia e classifica fornecedores de tecnologia financeira |
| **Celent** | Consultoria especializada em tecnologia para serviços financeiros | Reconhece a Topaz como referência em soluções bancárias |
