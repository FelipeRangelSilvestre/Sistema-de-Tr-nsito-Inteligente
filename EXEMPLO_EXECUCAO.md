# 🚀 Exemplo de Execução do Sistema

## Cenário: Malha Viária de Manaus Simplificada

### Passo 1: Iniciar o Sistema

```bash
$ python src/main.py
```

```
============================================================
               SISTEMA DE TRÂNSITO INTELIGENTE
============================================================

Inicializando sistema...

1. Carregar dados salvos
2. Usar dados de exemplo
3. Começar vazio

Escolha uma opção: 2

✓ Dados de exemplo carregados!
  • 6 interseções (A, B, C, D, E, F)
  • 9 vias bidirecionais
  • 2 eventos de trânsito
```

---

### Passo 2: Visualizar o Mapa

```
┌─────────────────────────────────────────────────┐
│  1. Gerenciar Malha Viária                     │
│  2. Gerenciar Eventos de Trânsito              │
│  3. Cálculo de Rotas                            │
│  4. Análise e Estatísticas                     │
│  5. Persistência de Dados                      │
│  0. Sair                                        │
└─────────────────────────────────────────────────┘

Escolha uma opção: 1
```

```
┌─────────────────────────────────────────────────┐
│  GERENCIAR MALHA VIÁRIA                         │
├─────────────────────────────────────────────────┤
│  1. Adicionar interseção                        │
│  2. Adicionar via                               │
│  3. Remover via                                 │
│  4. Visualizar mapa                             │
│  0. Voltar                                      │
└─────────────────────────────────────────────────┘

Escolha uma opção: 4
```

```
==================================================
MALHA VIÁRIA
==================================================
Total de interseções: 6
Interseções: A, B, C, D, E, F

Vias (bidirecionais):
--------------------------------------------------
A <-> B: 8.0km (original: 5.0km) *
A <-> C: 3.0km
B <-> C: 2.0km
B <-> D: 6.0km
C <-> D: 9.0km (original: 4.0km) *
C <-> E: 7.0km
D <-> E: 2.0km
D <-> F: 5.0km
E <-> F: 3.0km
--------------------------------------------------
* Via com evento de trânsito ativo

Pressione ENTER para continuar...
```

**Observação**: Note que A-B tem peso aumentado de 5.0 para 8.0 (+3.0) por causa de um acidente, e C-D aumentou de 4.0 para 9.0 (+5.0) por causa de uma obra.

---

### Passo 3: Ver Eventos Ativos

```
Escolha uma opção: 2 (Gerenciar Eventos)
```

```
┌─────────────────────────────────────────────────┐
│  GERENCIAR EVENTOS DE TRÂNSITO                  │
├─────────────────────────────────────────────────┤
│  1. Registrar novo evento                       │
│  2. Remover evento                              │
│  3. Listar eventos ativos                       │
