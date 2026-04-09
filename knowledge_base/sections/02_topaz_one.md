# 2. TOPAZ ONE -- PLATAFORMA FULL BANKING

## Visão Geral

A Topaz One é a primeira plataforma full banking do mundo. Do core banking à experiência do cliente, suas soluções integradas capacitam bancos, fintechs e instituições prestadoras de serviços financeiros a evoluir com agilidade, segurança e escalabilidade.

A plataforma é composta por **8 famílias de produtos** que, juntas, cobrem entre **80% e 90% das necessidades transacionais** de uma instituição financeira. É possível contratar parte a parte, com a estratégia de iniciar por uma dor específica do cliente e expandir o engajamento ao longo do tempo.

## As 8 Famílias de Produtos

### FinancialCore
Core bancário modular de última geração na nuvem. Gerencia contas, crédito, câmbio e consórcio. Inclui variantes: Core Universal (grandes bancos), Core Digital (neobancos), Core Microfinance (inclusão financeira) e ERP de Consórcio.

### SecureJourney
Suíte de segurança adotada por mais de 90% do mercado financeiro brasileiro. Cobre antifraude, antilavagem de dinheiro (PLD/FT), onboarding seguro e gestão de decisões com IA, Machine Learning e biometria avançada.

### FinChannels
Plataforma omnichannel que conecta canais físicos (ATM, caixas, retaguarda) e digitais (mobile banking, internet banking, Open Finance). Inclui orquestrador de canais, força de vendas e autosserviço para consórcio.

### FinXperience
Experiência bancária personalizada com IA e Open Banking. Motor de recomendação inteligente que sugere venda, troca de produto ou cobrança no canal certo e momento certo. Foco em rentabilização, fidelização e redução de churn.

### TechPay
Orquestração de pagamentos instantâneos. Processa PIX, SPB, boleto, wallet digital e moedas digitais. Primeiro PSTI (Provedor de Serviços de TI) certificado pelo Banco Central do Brasil especializado em instituições financeiras.

### TechInvest
Back-office completo de investimentos. Gerencia renda fixa, renda variável, fundos, derivativos (futuros, opções, swaps, NDFs) e wealth management. Inclui gestão de tesouraria com posições de P&L e ALM.

### FinOrigination
Onboarding digital e originação de produtos financeiros. Cobre originação digital (canais online), originação em campo (atendimento presencial) e aceite eletrônico. Conexão com diversos birôs para validação.

### BankingTools
Automação financeira e de TI. Soluções de regulatórios fiscais e contábeis (Receita Federal, Banco Central, demonstrativos, Cadox), conciliação, auditoria e ferramentas para acelerar o desenvolvimento de novos produtos.

## Arquitetura Funcional

A plataforma se organiza em camadas funcionais:

- **Front-end**: FinChannels e FinOrigination (canais de interação com o cliente)
- **Mid-layer**: FinXperience (experiência e recomendação), SecureJourney (segurança transversal)
- **Back-end**: FinancialCore (motor transacional), TechPay (mensageria e pagamentos), TechInvest (investimentos e tesouraria), BankingTools (regulatório e automação)

## Mapa de Integrações entre Produtos

A tabela abaixo mostra como cada produto se conecta nativamente com os demais dentro do ecossistema Topaz One. Isso é um diferencial-chave: o cliente não precisa integrar fornecedores diferentes.

| Produto | Integra Com | Benefício da Integração |
|---|---|---|
| **FinancialCore** | SecureJourney, FinChannels, TechPay, TechInvest, BankingTools, FinOrigination | Core conectado a todos os módulos; transações protegidas, canais unificados, pagamentos, investimentos e compliance em uma stack |
| **SecureJourney** | FinancialCore, TechPay, FinXperience, FinChannels, FinOrigination | Antifraude e PLD/FT em todas as camadas: core, pagamentos, canais, onboarding e experiência do cliente |
| **FinChannels** | FinancialCore, SecureJourney, FinXperience, TechPay | Canais orquestrados com dados do core, segurança transversal, personalização por perfil e pagamentos integrados |
| **FinXperience** | FinancialCore, SecureJourney, TechPay, FinChannels | IA atua sobre dados do core e transações para personalizar em todos os canais com segurança |
| **TechPay** | FinancialCore, SecureJourney, FinXperience, FinChannels, BankingTools | Pagamentos orquestrados com proteção antifraude, experiência personalizada e automação contábil |
| **TechInvest** | FinancialCore, TechPay, BankingTools | Back-office de investimentos conectado ao core, pagamentos e automação regulatória/contábil |
| **FinOrigination** | FinancialCore, SecureJourney, TechPay | Onboarding alimenta o core diretamente, com validação antifraude e processamento de pagamentos |
| **BankingTools** | FinancialCore, FinChannels, TechInvest, FinXperience, SecureJourney | Automação transversal: contabilidade, compliance e TI conectados a todos os módulos operacionais |

**Implicação para vendas**: quando o cliente adota um produto Topaz, a integração com o próximo produto é nativa e sem custo adicional de integração. Isso reduz drasticamente o TCO comparado a montar um stack de fornecedores especializados.

## Diferenciais da Plataforma

1. **Riqueza funcional e flexibilidade**: arquitetura modular que permite contratar apenas o necessário e expandir gradualmente
2. **Tecnologia moderna**: IA, Machine Learning, APIs abertas, cloud native, DevSecOps
3. **Reconhecimento de mercado**: Gartner, Celent, Forrester e principais provedores de cloud
4. **Escalabilidade e robustez**: projetada para clientes massificados com altos volumes transacionais
5. **Implantação híbrida**: on-premise, multi-cloud ou modelo híbrido
6. **Presença global com experiência local**: 25 países com conhecimento regulatório regional
7. **Interoperabilidade nativa**: soluções que se conectam de forma integrada entre si
8. **Time-to-market acelerado**: produtos altamente parametrizáveis com entrega ágil
9. **Autonomia do cliente**: ferramentas low-code e agentes de IA para que o cliente crie e otimize seus próprios produtos sem dependência de longo prazo
10. **Cobertura transacional de 80-90%**: cobre a grande maioria das necessidades de uma instituição financeira
