# Sistema de Trânsito Inteligente 🚦

## Descrição
Sistema desenvolvido para a disciplina de **Algoritmos e Estruturas de Dados II** que implementa um gerenciador inteligente de tráfego urbano utilizando **Grafo Ponderado** e **Árvore AVL**.

## 🎯 Objetivos
- Implementar estruturas de dados balanceadas (AVL) e grafos de forma funcional
- Aplicar algoritmos de busca, inserção, remoção e caminho mínimo
- Demonstrar integração entre duas estruturas de dados distintas
- Simular um sistema real de gerenciamento de tráfego

## 🏗️ Estruturas de Dados

### Grafo Ponderado
- **Vértices**: Representam interseções/pontos da cidade
- **Arestas**: Representam vias/ruas com pesos (distância em km)
- **Implementação**: Lista de adjacências com dicionários
- **Algoritmo**: Dijkstra para cálculo de caminho mínimo

### Árvore AVL
- **Nós**: Armazenam eventos de trânsito (acidentes, obras, congestionamentos)
- **Chave**: Timestamp do evento para ordenação temporal
- **Balanceamento**: Rotações simples e duplas mantêm altura O(log n)
- **Operações**: Inserção, remoção e busca em O(log n)

## 🔗 Integração das Estruturas

A integração entre Grafo e AVL ocorre da seguinte forma:

1. **Registro de Evento**: 
   - Evento é inserido na AVL (O(log n))
   - Peso da aresta correspondente no grafo é atualizado (O(1))

2. **Remoção de Evento**:
   - Evento é removido da AVL (O(log n))
   - Peso original da aresta é restaurado no grafo (O(1))

3. **Cálculo de Rota**:
   - Dijkstra considera os pesos atualizados pelos eventos ativos
   - Complexidade: O((V + E) log V)

## 📂 Estrutura do Projeto

```
sistema-transito/
│
├── src/
│   ├── avl_tree.py          # Implementação da Árvore AVL
│   ├── grafo_ponderado.py   # Implementação do Grafo
│   ├── sistema_transito.py  # Integração das estruturas
│   └── main.py              # Interface e menu principal
│
├── dados/
│   ├── grafo.txt           # Persistência da malha viária
│   └── eventos.txt         # Persistência dos eventos
│
├── docs/
│   └── relatorio.pdf       # Relatório técnico
│
├── README.md
└── requirements.txt
```

## 🚀 Como Executar

### Requisitos
- Python 3.8 ou superior
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-transito.git
cd sistema-transito

# Execute o sistema
python src/main.py
```

### Opções de Inicialização
1. **Carregar dados salvos**: Carrega dados de execuções anteriores
2. **Usar dados de exemplo**: Carrega um mapa pré-configurado para testes
3. **Começar vazio**: Inicia com o sistema vazio

## 📋 Funcionalidades

### 1. Gerenciar Malha Viária
- ✅ Adicionar interseções
- ✅ Adicionar vias bidirecionais com distâncias
- ✅ Remover vias
- ✅ Visualizar mapa completo

### 2. Gerenciar Eventos de Trânsito
- ✅ Registrar eventos (acidente, obra, congestionamento)
- ✅ Remover eventos
- ✅ Listar eventos ativos ordenados
- ✅ Buscar evento por ID

### 3. Cálculo de Rotas
- ✅ Calcular rota ótima (Dijkstra)
- ✅ Comparar rotas com e sem eventos
- ✅ Identificar eventos que afetam uma rota

### 4. Análise e Estatísticas
- ✅ Total de interseções e vias
- ✅ Eventos ativos
- ✅ Distribuição por tipo de evento

### 5. Persistência
- ✅ Salvar dados em arquivos texto
- ✅ Carregar dados salvos

## 🧪 Exemplos de Uso

### Exemplo 1: Criar Malha Viária
```
Adicionar interseções: A, B, C, D
Adicionar vias:
  A <-> B: 5.0 km
  B <-> C: 3.0 km
  C <-> D: 4.0 km
  A <-> D: 10.0 km
```

### Exemplo 2: Registrar Evento
```
Tipo: acidente
Via: A-B
Impacto: +3.0 km
Resultado: Via A-B passa de 5.0 km para 8.0 km
```

### Exemplo 3: Calcular Rota
```
Origem: A
Destino: D

Sem eventos:
  Caminho: A → B → C → D
  Distância: 12.0 km

Com evento em A-B:
  Caminho: A → D (rota alternativa)
  Distância: 10.0 km
  Sistema escolhe automaticamente a rota mais rápida!
```

## 📊 Complexidade das Operações

| Operação | Complexidade | Justificativa |
|----------|-------------|---------------|
| Inserir evento (AVL) | O(log n) | Árvore balanceada |
| Remover evento (AVL) | O(log n) | Árvore balanceada |
| Buscar evento (AVL) | O(log n) | Árvore balanceada |
| Adicionar via (Grafo) | O(1) | Lista de adjacências |
| Atualizar peso (Grafo) | O(1) | Acesso direto |
| Dijkstra | O((V+E) log V) | Com heap binário |

## 👥 Equipe

- Felipe Rangel Silvestre
- [Nome do Integrante 2]
- [Nome do Integrante 3]
- [Nome do Integrante 4]
- [Nome do Integrante 5]

## 📝 Relatório Técnico

O relatório completo está disponível em `docs/relatorio.pdf` e contém:
- Fundamentação teórica
- Análise de complexidade detalhada
- Capturas de tela dos testes
- Dificuldades encontradas e soluções
- Conclusões

## 🎓 Disciplina

**ITI275 - Algoritmos e Estruturas de Dados II**  
Prof. Alternei Brito  
Universidade Federal do Amazonas (UFAM)

## 📅 Entrega

**Data**: 25 de novembro de 2025

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.

---

**Nota**: Este sistema demonstra a aplicação prática de estruturas de dados avançadas em um problema real de otimização de rotas urbanas considerando eventos dinâmicos de trânsito.
