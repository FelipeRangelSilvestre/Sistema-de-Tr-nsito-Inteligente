#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Trânsito Inteligente
Estruturas: Grafo Ponderado + Árvore AVL
"""

import os
import time
from datetime import datetime


def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa a execução até pressionar Enter"""
    input("\nPressione ENTER para continuar...")


def exibir_cabecalho():
    """Exibe o cabeçalho do sistema"""
    print("=" * 60)
    print(" " * 15 + "SISTEMA DE TRÂNSITO INTELIGENTE")
    print("=" * 60)


def menu_principal():
    """Menu principal do sistema"""
    print("\n┌─────────────────────────────────────────────────┐")
    print("│  1. Gerenciar Malha Viária                     │")
    print("│  2. Gerenciar Eventos de Trânsito              │")
    print("│  3. Cálculo de Rotas                            │")
    print("│  4. Análise e Estatísticas                     │")
    print("│  5. Persistência de Dados                      │")
    print("│  0. Sair                                        │")
    print("└─────────────────────────────────────────────────┘")
    return input("\nEscolha uma opção: ").strip()


def menu_malha_viaria():
    """Submenu para gerenciar a malha viária"""
    print("\n┌─────────────────────────────────────────────────┐")
    print("│  GERENCIAR MALHA VIÁRIA                         │")
    print("├─────────────────────────────────────────────────┤")
    print("│  1. Adicionar interseção                        │")
    print("│  2. Adicionar via                               │")
    print("│  3. Remover via                                 │")
    print("│  4. Visualizar mapa                             │")
    print("│  0. Voltar                                      │")
    print("└─────────────────────────────────────────────────┘")
    return input("\nEscolha uma opção: ").strip()


def menu_eventos():
    """Submenu para gerenciar eventos"""
    print("\n┌─────────────────────────────────────────────────┐")
    print("│  GERENCIAR EVENTOS DE TRÂNSITO                  │")
    print("├─────────────────────────────────────────────────┤")
    print("│  1. Registrar novo evento                       │")
    print("│  2. Remover evento                              │")
    print("│  3. Listar eventos ativos                       │")
    print("│  4. Buscar evento por ID                        │")
    print("│  0. Voltar                                      │")
    print("└─────────────────────────────────────────────────┘")
    return input("\nEscolha uma opção: ").strip()


def menu_rotas():
    """Submenu para cálculo de rotas"""
    print("\n┌─────────────────────────────────────────────────┐")
    print("│  CÁLCULO DE ROTAS                               │")
    print("├─────────────────────────────────────────────────┤")
    print("│  1. Calcular rota ótima                         │")
    print("│  2. Comparar rotas (com/sem eventos)            │")
    print("│  3. Identificar eventos na rota                 │")
    print("│  0. Voltar                                      │")
    print("└─────────────────────────────────────────────────┘")
    return input("\nEscolha uma opção: ").strip()


def executar_sistema(sistema):
    """Executa o loop principal do sistema"""
    
    while True:
        limpar_tela()
        exibir_cabecalho()
        opcao = menu_principal()
        
        if opcao == '1':
            gerenciar_malha_viaria(sistema)
        elif opcao == '2':
            gerenciar_eventos(sistema)
        elif opcao == '3':
            calcular_rotas(sistema)
        elif opcao == '4':
            exibir_estatisticas(sistema)
        elif opcao == '5':
            gerenciar_persistencia(sistema)
        elif opcao == '0':
            print("\n✓ Encerrando o sistema...")
            time.sleep(1)
            break
        else:
            print("\n✗ Opção inválida!")
            pausar()


def gerenciar_malha_viaria(sistema):
    """Gerencia operações da malha viária"""
    while True:
        limpar_tela()
        exibir_cabecalho()
        opcao = menu_malha_viaria()
        
        if opcao == '1':
            # Adicionar interseção
            print("\n→ ADICIONAR INTERSEÇÃO")
            nome = input("Nome da interseção: ").strip().upper()
            if nome:
                sistema.grafo.adicionar_vertice(nome)
                print(f"✓ Interseção '{nome}' adicionada com sucesso!")
            else:
                print("✗ Nome inválido!")
            pausar()
            
        elif opcao == '2':
            # Adicionar via
            print("\n→ ADICIONAR VIA (BIDIRECIONAL)")
            origem = input("Interseção de origem: ").strip().upper()
            destino = input("Interseção de destino: ").strip().upper()
            try:
                peso = float(input("Distância (km): ").strip())
                if peso > 0:
                    sistema.grafo.adicionar_aresta(origem, destino, peso)
                    print(f"✓ Via {origem} <-> {destino} adicionada!")
                else:
                    print("✗ Distância deve ser positiva!")
            except ValueError:
                print("✗ Distância inválida!")
            pausar()
            
        elif opcao == '3':
            # Remover via
            print("\n→ REMOVER VIA")
            origem = input("Interseção de origem: ").strip().upper()
            destino = input("Interseção de destino: ").strip().upper()
            if sistema.grafo.remover_aresta(origem, destino):
                print(f"✓ Via {origem} <-> {destino} removida!")
            else:
                print("✗ Via não encontrada!")
            pausar()
            
        elif opcao == '4':
            # Visualizar mapa
            print("\n")
            print(sistema.grafo.visualizar_grafo())
            pausar()
            
        elif opcao == '0':
            break
        else:
            print("\n✗ Opção inválida!")
            pausar()


def gerenciar_eventos(sistema):
    """Gerencia eventos de trânsito"""
    while True:
        limpar_tela()
        exibir_cabecalho()
        opcao = menu_eventos()
        
        if opcao == '1':
            # Registrar evento
            print("\n→ REGISTRAR NOVO EVENTO")
            print("Tipos: acidente, obra, congestionamento")
            tipo = input("Tipo de evento: ").strip().lower()
            
            if tipo not in ['acidente', 'obra', 'congestionamento']:
                print("✗ Tipo inválido!")
                pausar()
                continue
            
            origem = input("Via - Origem: ").strip().upper()
            destino = input("Via - Destino: ").strip().upper()
            
            try:
                impacto = float(input("Impacto no tempo (km adicional): ").strip())
                if impacto > 0:
                    sucesso, msg = sistema.registrar_evento(tipo, origem, destino, impacto)
                    if sucesso:
                        print(f"✓ {msg}")
                    else:
                        print(f"✗ {msg}")
                else:
                    print("✗ Impacto deve ser positivo!")
            except ValueError:
                print("✗ Impacto inválido!")
            pausar()
            
        elif opcao == '2':
            # Remover evento
            print("\n→ REMOVER EVENTO")
            try:
                id_evento = int(input("ID do evento: ").strip())
                sucesso, msg = sistema.remover_evento(id_evento)
                if sucesso:
                    print(f"✓ {msg}")
                else:
                    print(f"✗ {msg}")
            except ValueError:
                print("✗ ID inválido!")
            pausar()
            
        elif opcao == '3':
            # Listar eventos
            print("\n→ EVENTOS ATIVOS")
            eventos = sistema.avl.listar_todos()
            
            if not eventos:
                print("Nenhum evento ativo no momento.")
            else:
                print(f"\nTotal: {len(eventos)} evento(s)\n")
                print("-" * 80)
                print(f"{'ID':<5} {'Tipo':<18} {'Localização':<15} {'Impacto':<10} {'Data/Hora'}")
                print("-" * 80)
                
                for evento in eventos:
                    data_hora = datetime.fromtimestamp(evento.timestamp).strftime('%d/%m/%Y %H:%M')
                    print(f"{evento.id:<5} {evento.tipo:<18} {evento.localizacao:<15} "
                          f"+{evento.impacto:<9.1f} {data_hora}")
                
                print("-" * 80)
            pausar()
            
        elif opcao == '4':
            # Buscar evento
            print("\n→ BUSCAR EVENTO POR ID")
            try:
                id_evento = int(input("ID do evento: ").strip())
                evento = sistema.avl.buscar(id_evento)
                
                if evento:
                    print("\n" + "=" * 50)
                    print(f"ID: {evento.id}")
                    print(f"Tipo: {evento.tipo}")
                    print(f"Localização: {evento.localizacao}")
                    print(f"Impacto: +{evento.impacto} km")
                    data_hora = datetime.fromtimestamp(evento.timestamp).strftime('%d/%m/%Y às %H:%M')
                    print(f"Registrado em: {data_hora}")
                    print("=" * 50)
                else:
                    print("✗ Evento não encontrado!")
            except ValueError:
                print("✗ ID inválido!")
            pausar()
            
        elif opcao == '0':
            break
        else:
            print("\n✗ Opção inválida!")
            pausar()


def calcular_rotas(sistema):
    """Calcula e compara rotas"""
    while True:
        limpar_tela()
        exibir_cabecalho()
        opcao = menu_rotas()
        
        if opcao == '1':
            # Calcular rota ótima
            print("\n→ CALCULAR ROTA ÓTIMA")
            origem = input("Origem: ").strip().upper()
            destino = input("Destino: ").strip().upper()
            
            print("\nCalculando...")
            caminho, distancia, status = sistema.calcular_rota_otima(origem, destino)
            
            if status == "OK":
                print("\n" + "=" * 50)
                print("ROTA ÓTIMA ENCONTRADA")
                print("=" * 50)
                print(f"Caminho: {' → '.join(caminho)}")
                print(f"Distância total: {distancia:.2f} km")
                print("=" * 50)
                
                # Verificar eventos na rota
                eventos = sistema.eventos_na_rota(caminho)
                if eventos:
                    print(f"\n⚠ Atenção: {len(eventos)} evento(s) afetando esta rota:")
                    for ev in eventos:
                        print(f"  • {ev.tipo} em {ev.localizacao} (+{ev.impacto} km)")
            else:
                print(f"\n✗ {status}")
            pausar()
            
        elif opcao == '2':
            # Comparar rotas
            print("\n→ COMPARAR ROTAS (COM/SEM EVENTOS)")
            origem = input("Origem: ").strip().upper()
            destino = input("Destino: ").strip().upper()
            
            print("\nAnalisando...")
            resultado = sistema.comparar_rotas(origem, destino)
            
            caminho_ideal, dist_ideal = resultado['rota_ideal']
            caminho_atual, dist_atual = resultado['rota_atual']
            impacto = resultado['impacto']
            
            print("\n" + "=" * 60)
            print("COMPARAÇÃO DE ROTAS")
            print("=" * 60)
            
            if caminho_ideal:
                print("\n🟢 Rota ideal (sem eventos):")
                print(f"   Caminho: {' → '.join(caminho_ideal)}")
                print(f"   Distância: {dist_ideal:.2f} km")
            
            if caminho_atual:
                print("\n🔴 Rota atual (com eventos):")
                print(f"   Caminho: {' → '.join(caminho_atual)}")
                print(f"   Distância: {dist_atual:.2f} km")
            
            if impacto > 0:
                print(f"\n⚠ Impacto dos eventos: +{impacto:.2f} km ({(impacto/dist_ideal*100):.1f}%)")
            elif impacto == 0:
                print("\n✓ Nenhum impacto - rotas idênticas")
            
            print("=" * 60)
            pausar()
            
        elif opcao == '3':
            # Identificar eventos na rota
            print("\n→ IDENTIFICAR EVENTOS NA ROTA")
            origem = input("Origem: ").strip().upper()
            destino = input("Destino: ").strip().upper()
            
            caminho, distancia, status = sistema.calcular_rota_otima(origem, destino)
            
            if status == "OK":
                eventos = sistema.eventos_na_rota(caminho)
                print(f"\nRota: {' → '.join(caminho)}")
                print(f"Distância: {distancia:.2f} km\n")
                
                if eventos:
                    print(f"⚠ {len(eventos)} evento(s) afetando esta rota:\n")
                    for ev in eventos:
                        print(f"  ID {ev.id}: {ev.tipo} em {ev.localizacao}")
                        print(f"           Impacto: +{ev.impacto} km")
                        data = datetime.fromtimestamp(ev.timestamp).strftime('%d/%m/%Y %H:%M')
                        print(f"           Registrado: {data}\n")
                else:
                    print("✓ Nenhum evento afetando esta rota")
            else:
                print(f"\n✗ {status}")
            pausar()
            
        elif opcao == '0':
            break
        else:
            print("\n✗ Opção inválida!")
            pausar()


def exibir_estatisticas(sistema):
    """Exibe estatísticas do sistema"""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n→ ANÁLISE E ESTATÍSTICAS")
    
    stats = sistema.estatisticas()
    
    print("\n" + "=" * 50)
    print("RESUMO DO SISTEMA")
    print("=" * 50)
    print(f"Interseções cadastradas: {stats['total_intersecoes']}")
    print(f"Vias cadastradas: {stats['total_vias']}")
    print(f"Eventos ativos: {stats['eventos_ativos']}")
    print("=" * 50)
    
    if stats['eventos_ativos'] > 0:
        print("\nDistribuição por tipo de evento:")
        eventos = sistema.avl.listar_todos()
        tipos = {}
        for ev in eventos:
            tipos[ev.tipo] = tipos.get(ev.tipo, 0) + 1
        
        for tipo, qtd in sorted(tipos.items()):
            print(f"  • {tipo.capitalize()}: {qtd}")
    
    pausar()


def gerenciar_persistencia(sistema):
    """Gerencia salvamento e carregamento de dados"""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n┌─────────────────────────────────────────────────┐")
    print("│  PERSISTÊNCIA DE DADOS                          │")
    print("├─────────────────────────────────────────────────┤")
    print("│  1. Salvar dados                                │")
    print("│  2. Carregar dados                              │")
    print("│  0. Voltar                                      │")
    print("└─────────────────────────────────────────────────┘")
    
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == '1':
        sucesso, msg = sistema.salvar_dados()
        if sucesso:
            print(f"\n✓ {msg}")
        else:
            print(f"\n✗ {msg}")
        pausar()
        
    elif opcao == '2':
        sucesso, msg = sistema.carregar_dados()
        if sucesso:
            print(f"\n✓ {msg}")
        else:
            print(f"\n✗ {msg}")
        pausar()


def criar_dados_exemplo(sistema):
    """Cria dados de exemplo para demonstração"""
    # Adicionar interseções
    intersecoes = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in intersecoes:
        sistema.grafo.adicionar_vertice(i)
    
    # Adicionar vias
    vias = [
        ('A', 'B', 5.0),
        ('A', 'C', 3.0),
        ('B', 'C', 2.0),
        ('B', 'D', 6.0),
        ('C', 'D', 4.0),
        ('C', 'E', 7.0),
        ('D', 'E', 2.0),
        ('D', 'F', 5.0),
        ('E', 'F', 3.0),
    ]
    
    for origem, destino, peso in vias:
        sistema.grafo.adicionar_aresta(origem, destino, peso)
    
    # Adicionar alguns eventos
    sistema.registrar_evento('acidente', 'A', 'B', 3.0)
    sistema.registrar_evento('obra', 'C', 'D', 5.0)
    
    print("✓ Dados de exemplo carregados!")
    print("  • 6 interseções (A, B, C, D, E, F)")
    print("  • 9 vias bidirecionais")
    print("  • 2 eventos de trânsito")


def main():
    """Função principal"""
    # Importar as classes (assumindo que estão em arquivos separados)
    # from avl_tree import ArvoreAVL
    # from grafo_ponderado import GrafoPonderado
    # from sistema_transito import SistemaTransito
    
    # Para este exemplo, as classes estão no mesmo arquivo
    from avl_tree import ArvoreAVL
    from grafo_ponderado import GrafoPonderado
    from sistema_transito import SistemaTransito
    
    limpar_tela()
    exibir_cabecalho()
    
    print("\nInicializando sistema...")
    
    # Criar instâncias
    grafo = GrafoPonderado()
    avl = ArvoreAVL()
    sistema = SistemaTransito(grafo, avl)
    
    # Perguntar se quer carregar dados ou usar exemplo
    print("\n1. Carregar dados salvos")
    print("2. Usar dados de exemplo")
    print("3. Começar vazio")
    
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == '1':
        sucesso, msg = sistema.carregar_dados()
        print(f"\n{msg}")
        time.sleep(2)
    elif opcao == '2':
        criar_dados_exemplo(sistema)
        time.sleep(2)
    
    # Executar sistema
    executar_sistema(sistema)
    
    limpar_tela()
    print("\n" + "=" * 60)
    print(" " * 15 + "Obrigado por usar o sistema!")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
