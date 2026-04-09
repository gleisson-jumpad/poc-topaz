# 3. FINANCIALCORE -- CORE BANKING

## Resumo Executivo

O FinancialCore é a solução de core banking de última geração da Topaz, projetada para modernizar o coração da operação bancária. Com arquitetura modular baseada em nuvem, opera 100% online e em tempo real, substituindo cores legados monolíticos que dependem de processos batch, possuem baixa integração e custos elevados de manutenção.

Atende bancos tradicionais, bancos digitais, fintechs, cooperativas de crédito, financeiras, IPs, SCDs, instituições B2B e B2C, de investimento e de tesouraria.

## Sub-produtos

### Core Universal
Para grandes e médias instituições que buscam um portfólio completo de produtos financeiros. Sistema robusto e escalável para gerenciar captação e colocação, com interoperabilidade total entre agências, ATMs, internet banking e aplicativos móveis.

### Core Digital
Para bancos digitais e neobancos. Permite lançar produtos e serviços em tempo recorde, com foco total na experiência do usuário. Integra IA, APIs e tecnologias de última geração, sem necessidade de agências físicas, garantindo baixos custos operacionais.

### Core Microfinance
Para microcréditos e produtos financeiros de curto prazo. Reduz custos operacionais para permitir inclusão financeira com eficiência e impacto social. Transforma a vida de clientes não bancarizados ou sub-bancarizados.

### ERP de Consórcio
Solução robusta e escalável para administradoras de consórcio. Gestão completa de grupos e cotas, automação de sorteios e contemplações, integração com bancos, OCR para validação de documentos e conformidade total com o Banco Central. Disponível em SaaS, cloud privada ou on-premises.

### Topaz Open

Versão padronizada e pré-configurada do core bancário, criada para fintechs, cooperativas e instituições que precisam iniciar a operação com velocidade máxima e custo reduzido.

**Características:**
- Produtos de **conta e crédito pré-configurados**, prontos para uso
- Implantação significativamente mais rápida que o Core Universal (semanas vs. meses)
- Funciona como **porta de entrada** para o ecossistema Topaz One — conforme a operação cresce, o cliente pode migrar para o Core Universal ou Digital sem reescrita
- Ideal para **SCDs, SIPs, fintechs em fase de lançamento** e cooperativas menores que precisam de conformidade BACEN desde o dia 1
- Modelo comercial flexível, incluindo **Revenue Share** (a Topaz ganha conforme o cliente ganha)
- Stack tecnológica idêntica ao core principal (Java, microserviços, K8s), garantindo que a migração futura seja suave
- Integração nativa com SecureJourney (antifraude) e TechPay (pagamentos instantâneos) desde a primeira versão

**Quando recomendar o Topaz Open:**
- Cliente quer lançar operação financeira em **até 3 meses**
- Budget inicial é limitado mas há projeção de crescimento
- Precisa de conformidade regulatória sem complexidade de configuração
- É uma fintech ou cooperativa em fase inicial que ainda não precisa do portfólio completo do Core Universal

## Funcionalidades Principais

- **Cadastro de clientes**: simplificado e integrado
- **Gestão de cestas e tarifas**: parametrização flexível
- **Contabilidade transacional**: em tempo real
- **Contas**: corrente PF/PJ, pagamentos, salário, capital, poupança
- **Serviços de conta**: transferências, bloqueios, extratos, cash-in/cash-out
- **Produtos de crédito**: pessoal, CDC, capital de giro, consignado, financiamento
- **Emissão de cartões**: débito, crédito e pré-pagos
- **Integração omnichannel**: agências, aplicativos móveis e internet banking

## Arquitetura Técnica

O FinancialCore é organizado em três camadas:

1. **Camada de Domínio**: objetos e serviços de negócio reutilizáveis, representados em seus próprios domínios. Permite instalações e migrações granulares sem afetar o restante das aplicações.

2. **Biblioteca Topaz Lógica de Aplicação**: sustenta customizações e variações por cliente usando linguagem de alto nível e ambientes de desenvolvimento integrados. Garante flexibilidade e personalização sem codificação complexa.

3. **Camada de Serviços**: integrações com sistemas satélites e exposição de APIs. Suporta webservices, ISO 8583, ETL, servidores de mensagens e diversos padrões de mercado.

## Stack Tecnológica

- **Linguagem**: Java
- **Arquitetura**: Microserviços, containers
- **Orquestração**: Kubernetes, OpenShift
- **Mensageria**: JMS
- **Processos**: BPM
- **Banco de dados**: Relacional agnóstico
- **Segurança**: SSL, TLS, certificados digitais

## Diferenciais Competitivos

- **Escalabilidade** para grandes volumes transacionais (PagBank: 33M transações/dia, 80K txns/min)
- **Redução de time-to-market** via parametrização low-code
- **Flexibilidade** para criar produtos customizados sem codificação complexa
- **Integração fluida** com sistemas legados
- **Conformidade regulatória** incorporada (BACEN, PCI-DSS, LGPD)
- **Cloud-ready** com elasticidade e resiliência
- **Menor TCO** (custo total de propriedade) do mercado
- **Operação 100% online** e em tempo real, sem processos batch

## Implantação

- **Modelo**: Ágil e incremental, com sprints e entregas progressivas
- **Prazo médio**: 8 a 12 meses
- **Abordagem**: Modular por domínio de negócio, sem necessidade de Big Bang
- **Migração**: Segura de dados com parametrização assistida
- **Equipe**: Especialistas Topaz acompanham todas as etapas

## Integração com o Ecossistema Topaz

O FinancialCore se conecta nativamente com:
- **SecureJourney**: proteção contra fraudes desde o início das operações
- **FinChannels**: experiência unificada em todos os pontos de contato
- **TechPay**: processamento de pagamentos
- **TechInvest**: gestão de investimentos integrada ao core
- **BankingTools**: automação contábil e regulatória

## FAQ

**"Quanto custa migrar para o FinancialCore?"**
Depende do modelo comercial escolhido. Para quem quer evitar investimento inicial alto, o Revenue Share é ideal — a Topaz ganha conforme o cliente ganha. Já quem prefere previsibilidade pode optar por SaaS (mensalidade + variável por transação). O ponto-chave: o TCO do FinancialCore é consistentemente menor que o de concorrentes globais como Temenos e Oracle, considerando licenciamento, implementação e manutenção.

**"E se a migração der errado? Já tivemos projetos que falharam."**
A abordagem é incremental — nada de Big Bang. Migramos carteira por carteira, produto por produto, com entregas a cada sprint. O PagBank escalou de 3 para 30 milhões de contas, e o Sicredi migrou mais de 100 cooperativas nessa abordagem. Prazo médio: 8 a 12 meses com acompanhamento especializado.

**"O core de vocês aguenta nosso volume transacional?"**
O PagBank processa 33 milhões de transações por dia e 80 mil transações por minuto no FinancialCore. Se seu volume for menor que isso, a resposta é sim com folga. Se for maior, vamos conversar — a arquitetura em microserviços e Kubernetes escala horizontalmente.

**"Qual a diferença entre o Topaz Open e o FinancialCore completo?"**
O Topaz Open é uma versão padronizada do core, com produtos de conta e crédito pré-configurados, pronta para rodar em semanas. É ideal para fintechs e cooperativas que precisam de agilidade. Conforme a operação cresce, a migração para o Core Universal ou Core Digital é suave porque a stack tecnológica é a mesma.

**"Funciona com Open Banking/Open Finance?"**
Sim. O FinancialCore possui APIs abertas que conectam com o ecossistema de Open Finance. É a base que sustenta o compartilhamento de dados, iniciação de pagamentos e portabilidade — tudo em tempo real e com segurança.

**"Vocês suportam múltiplas moedas e regulamentações internacionais?"**
Sim. A Topaz opera em 25 países com customizações regulatórias para cada mercado. O caso Bradescar no México (200M de transações, R$300bi de volume anual) é prova disso.
