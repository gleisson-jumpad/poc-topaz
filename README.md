# POC Topaz — Professional Service

Proof of concept para agentes de IA aplicados ao ciclo de vendas da Topaz, empresa de tecnologia financeira (full banking). O projeto inclui bases de conhecimento, prompts de agentes e simulações de reunião por voz.

## Estrutura do Projeto

```
.
├── knowledge_base/
│   ├── topaz_knowledge_base.md      # KB consolidada (18 seções)
│   ├── build_kb.py                  # Script que concatena as seções
│   └── sections/                    # Seções individuais da KB
│       ├── 01_empresa.md
│       ├── 02_topaz_one.md
│       ├── ...
│       └── 18_glossario.md
│
├── competitors/
│   └── matera.md                    # KB do concorrente Matera
│
├── meeting_agent_topaz.md           # Prompt do agente Onyx (co-piloto de vendas)
├── meeting_agent_template.md        # Template base para meeting agents
│
├── simulation/
│   ├── client_matera.md             # Agente cliente (conhece Matera, avalia Topaz)
│   ├── salesperson_pleno.md         # Vendedor Topaz — nível Pleno (~30% da KB)
│   ├── salesperson_senior.md        # Vendedor Topaz — nível Senior (~60% da KB)
│   └── salesperson_expert.md        # Vendedor Topaz — nível Expert (~80% da KB)
│
├── topaz_one.md                     # Notas brutas — vídeo Topaz One
├── topaz_core_banking.md            # Notas brutas — vídeo Core Banking
└── cursor_prompt.md                 # Prompt de contexto para o Cursor
```

## Componentes

### 1. Knowledge Base (`knowledge_base/`)

Base de conhecimento completa da Topaz com 18 seções cobrindo: empresa, plataforma Topaz One (8 famílias de produtos), soluções por setor, cases de sucesso, cenário competitivo, modelos comerciais, playbook de vendas, guia problema-produto, objeções e glossário.

As seções ficam em arquivos individuais em `sections/` e são consolidadas em `topaz_knowledge_base.md` pelo script `build_kb.py`.

### 2. Agente Onyx (`meeting_agent_topaz.md`)

Co-piloto de vendas que acompanha reuniões em tempo real via transcrição. Opera em canal privado (DM) com o vendedor, com 4 modos de atuação:

- **Reforço Positivo** — confirma acertos e complementa com dados
- **Injeção Estratégica** — antecipa informações relevantes
- **Correção** — corrige erros factuais com discrição
- **Assistência sob Demanda** — responde perguntas diretas do vendedor

### 3. Competitor Analysis (`competitors/`)

Base de conhecimento da Matera (concorrente), incluindo empresa, 9 soluções, arquitetura, cases e métricas. Usada para inseminar o agente cliente nas simulações.

### 4. Simulação de Reunião (`simulation/`)

Conjunto de prompts self-contained para simular uma reunião de vendas por voz usando OpenAI Realtime API. Cada arquivo é independente — basta copiar e colar no agente.

| Agente | Arquivo | Descrição |
|--------|---------|-----------|
| Cliente | `client_matera.md` | CTO avaliando Topaz, já conhece Matera, faz perguntas comparativas |
| Pleno | `salesperson_pleno.md` | Vendedor com ~30% da KB. Visão geral, defere detalhes técnicos |
| Senior | `salesperson_senior.md` | Vendedor com ~60% da KB. Domina 4 produtos principais + cases + playbook |
| Expert | `salesperson_expert.md` | Vendedor com ~80% da KB. Domina tudo, trata objeções, posiciona vs. concorrentes |

Cada prompt tem uma seção **PARÂMETROS (edite aqui)** no topo para configurar nome, cargo, idioma, tempo de silêncio entre turnos, etc.

#### Protocolo de Voz

Os agentes seguem regras de turn-taking para evitar sobreposição:
- Vendedor Topaz fala primeiro (apresentação)
- 3 segundos de silêncio antes de cada fala
- Nunca interromper
- Máximo de 45 segundos por turno

## Como Usar

### Agente Onyx (co-piloto de reunião)
1. Copie o conteúdo de `meeting_agent_topaz.md`
2. Cole como prompt do agente na plataforma de meeting agents
3. O agente receberá transcrições em tempo real e responderá via DM

### Simulação de Reunião por Voz
1. Abra o arquivo do agente desejado em `simulation/`
2. Edite os **PARÂMETROS** no topo conforme necessário
3. Copie o conteúdo completo
4. Cole como system prompt no OpenAI Realtime API
5. Repita para o segundo agente (cliente + um dos salespersons)
6. Inicie a sessão de voz

## Stack

- Prompts em Markdown
- OpenAI Realtime API (simulação por voz)
- ElevenLabs (síntese de voz opcional)
- Knowledge base modular com builder em Python
