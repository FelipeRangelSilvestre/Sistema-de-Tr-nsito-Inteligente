# 📋 Guia de Organização do Projeto

## 🗂️ Estrutura de Pastas

```
sistema-transito-inteligente/
│
├── src/
│   ├── avl_tree.py              # Implementação da Árvore AVL
│   ├── grafo_ponderado.py       # Implementação do Grafo
│   ├── sistema_transito.py      # Integração das estruturas
│   ├── main.py                  # Interface principal
│   ├── test_sistema.py          # Testes unitários
│   └── criar_dados_exemplo.py   # Script para dados de teste
│
├── dados/                       # Criado automaticamente
│   ├── grafo.txt               # Persistência da malha viária
│   └── eventos.txt             # Persistência dos eventos
│
├── docs/
│   ├── relatorio.pdf           # Relatório técnico final
│   └── screenshots/            # Capturas de tela
│       ├── menu.png
│       ├── mapa.png
│       ├── eventos.png
│       └── rotas.png
│
├── README.md                    # Documentação principal
├── .gitignore                  # Arquivos a ignorar no Git
└── requirements.txt            # Dependências (vazio neste caso)
```

## 📝 Checklist de Tarefas por Membro

### Divisão Sugerida (5 membros):

#### 👤 Membro 1: Estrutura AVL
- [ ] Implementar classe `NoAVL`
- [ ] Implementar rotações (simples e duplas)
- [ ] Implementar inserção com balanceamento
- [ ] Implementar remoção com balanceamento
- [ ] Documentar complexidades

#### 👤 Membro 2: Estrutura Grafo
- [ ] Implementar classe `GrafoPonderado`
- [ ] Implementar adicionar/remover vértices e arestas
- [ ] Implementar algoritmo de Dijkstra
- [ ] Implementar visualização do grafo
- [ ] Documentar complexidades

#### 👤 Membro 3: Integração
- [ ] Implementar classe `SistemaTransito`
- [ ] Integrar registro de eventos (AVL + Grafo)
- [ ] Implementar comparação de rotas
- [ ] Implementar persistência de dados
- [ ] Documentar a integração

#### 👤 Membro 4: Interface e Testes
- [ ] Implementar menu interativo
- [ ] Criar todos os submenus
- [ ] Implementar testes unitários
- [ ] Criar dados de exemplo
- [ ] Validar funcionamento completo

#### 👤 Membro 5: Documentação
- [ ] Escrever README.md
- [ ] Criar relatório técnico no Overleaf
- [ ] Capturar screenshots
- [ ] Preparar apresentação
- [ ] Revisar documentação geral

## 📅 Cronograma Sugerido

### Semana 1 (1-7 Nov)
- [ ] Definição clara de tarefas
- [ ] Implementação das estruturas básicas (AVL e Grafo)
- [ ] Testes individuais de cada estrutura

### Semana 2 (8-14 Nov)
- [ ] Implementação da integração
- [ ] Desenvolvimento da interface
- [ ] Testes de integração

### Semana 3 (15-21 Nov)
- [ ] Finalização do código
- [ ] Escrita do relatório
- [ ] Capturas de tela
- [ ] Preparação da apresentação

### Semana 4 (22-25 Nov)
- [ ] Revisão final
- [ ] Testes completos
- [ ] Upload no GitHub
- [ ] Envio do relatório
- [ ] **Entrega: 25 de Novembro**

## 🐙 Configuração do GitHub

### 1. Criar Repositório

```bash
# Um membro cria o repositório
git init
git add .
git commit -m "Estrutura inicial do projeto"
git branch -M main
git remote add origin https://github.com/usuario/sistema-transito.git
git push -u origin main
```

### 2. Colaboradores Clonarem

```bash
git clone https://github.com/usuario/sistema-transito.git
cd sistema-transito
```

### 3. Workflow de Desenvolvimento

Cada membro trabalha em sua branch:

```bash
# Criar branch pessoal
git checkout -b feature/avl-tree

# Fazer alterações
git add src/avl_tree.py
git commit -m "Implementa inserção na AVL com balanceamento"

# Enviar para o GitHub
git push origin feature/avl-tree
```

### 4. Integrar Código (Pull Request)

1. Fazer Pull Request no GitHub
2. Outro membro revisa
3. Após aprovação, fazer merge na main

## 📖 Overleaf - Relatório

### 1. Criar Projeto no Overleaf

1. Acesse [overleaf.com](https://www.overleaf.com)
2. Criar novo projeto
3. Copiar template LaTeX fornecido
4. Compartilhar com todos os membros

### 2. Divisão do Relatório

- **Introdução**: Membro 5
- **Fundamentação Teórica**: Membros 1 e 2
- **Implementação**: Membros 1, 2 e 3
- **Testes**: Membro 4
- **Conclusões**: Todos revisam

### 3. Link no README

```markdown
## 📄 Relatório

O relatório técnico completo está disponível no Overleaf:
https://www.overleaf.com/read/xxxxxxxxxxxxx
```

## 🎯 Pontos de Atenção

### ✅ O que fazer:

1. **Comunicação constante**: Use WhatsApp/Discord
2. **Commits frequentes**: Commitar pequenas mudanças
3. **Testar constantemente**: Não deixe bugs acumularem
4. **Documentar código**: Comentários e docstrings
5. **Reuniões semanais**: Alinhar progresso

### ❌ O que evitar:

1. **Não deixar para última hora**
2. **Não fazer commits diretamente na main**
3. **Não copiar código sem entender**
4. **Não ignorar os testes**
5. **Não esquecer de citar fontes**

## 🧪 Como Testar

### Teste Individual das Estruturas

```bash
# Testar AVL
python -c "from src.avl_tree import ArvoreAVL; avl = ArvoreAVL(); avl.inserir(1, 100, 'teste', 'A-B', 1.0); print(avl.total_eventos)"

# Testar Grafo
python -c "from src.grafo_ponderado import GrafoPonderado; g = GrafoPonderado(); g.adicionar_aresta('A', 'B', 5); print(g.total_arestas())"
```

### Teste Completo do Sistema

```bash
# Executar bateria de testes
python src/test_sistema.py

# Executar sistema principal
python src/main.py
```

## 📸 Screenshots Necessários

Capture telas dos seguintes momentos:

1. **Menu principal** do sistema
2. **Visualização do mapa** com várias vias
3. **Listagem de eventos ativos**
4. **Cálculo de rota** mostrando caminho
5. **Comparação de rotas** (com/sem eventos)
6. **Resultado dos testes** unitários

Salvar em: `docs/screenshots/`

## 🎤 Preparação da Apresentação

### Estrutura (10-15 minutos):

1. **Introdução** (2 min)
   - Problema que resolve
   - Estruturas utilizadas

2. **Demonstração** (5-7 min)
   - Mostrar sistema funcionando
   - Criar mapa de exemplo
   - Registrar evento
   - Calcular rota

3. **Aspectos Técnicos** (3-4 min)
   - Explicar integração
   - Mostrar complexidades
   - Destacar desafios

4. **Conclusão** (1-2 min)
   - Resultados obtidos
   - Aprendizados

### Dicas:

- Todos devem falar
- Treinar antes
- Preparar backup (vídeo) caso falhe ao vivo
- Ter dados de exemplo prontos

## 📊 Critérios de Avaliação (Lembrete)

| Critério | Peso | Como atender |
|----------|------|--------------|
| Funcionamento | 5.0 | Testar TUDO antes de entregar |
| Implementação | 2.0 | Código limpo, sem bibliotecas |
| Documentação | 1.0 | Comentários, README completo |
| Relatório | 2.0 | Seguir template, análise detalhada |
| **Bônus Integração** | +1.0 | **Grafo + AVL bem integrados** |

## 🆘 Recursos de Ajuda

### Dúvidas Técnicas:
- Revisar material da disciplina
- Consultar livros indicados
- Perguntar ao professor

### Problemas com Git:
```bash
# Desfazer último commit (local)
git reset --soft HEAD~1

# Atualizar com mudanças remotas
git pull origin main

# Ver status
git status
```

### Debugging Python:
```python
# Adicionar prints para debug
print(f"DEBUG: variável = {variavel}")

# Usar try-except
try:
    # código
except Exception as e:
    print(f"Erro: {e}")
```

## ✅ Checklist Final Antes da Entrega

- [ ] Código completo no GitHub
- [ ] README.md atualizado com link do GitHub
- [ ] Relatório PDF no Overleaf
- [ ] Screenshots incluídos no relatório
- [ ] Testes executando sem erros
- [ ] Sistema salvando/carregando dados
- [ ] Todos os membros entendem o código
- [ ] Apresentação preparada
- [ ] Backup do projeto (ZIP local)

## 🎓 Contatos da Equipe

- Membro 1: [email/telefone]
- Membro 2: [email/telefone]
- Membro 3: [email/telefone]
- Membro 4: [email/telefone]
- Membro 5: [email/telefone]

---

**Última atualização**: Antes de começar o projeto

**Status do Projeto**: ⬜ Não iniciado | 🟡 Em andamento | ✅ Concluído
