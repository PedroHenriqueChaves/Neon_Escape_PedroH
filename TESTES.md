# Plano de testes — Neon Escape

Este documento registra os testes necessários para a versão de entrega. Os itens devem ser marcados após a execução no computador da equipe.

## Testes funcionais

| ID | Teste | Resultado esperado | Status |
|---|---|---|---|
| T01 | Abrir `main.py` | Janela 1000x650 inicia sem erro | Pendente de execução final |
| T02 | ENTER no menu | Inicia uma partida | Pendente de execução final |
| T03 | I no menu | Abre instruções | Pendente de execução final |
| T04 | WASD/setas | Jogador se movimenta | Pendente de execução final |
| T05 | Limite da tela | Jogador não sai da área jogável | Pendente de execução final |
| T06 | Coletar núcleo verde | +100 pontos e energia recuperada | Pendente de execução final |
| T07 | Coletar núcleo amarelo | +250 pontos | Pendente de execução final |
| T08 | Colidir com drone | Perde vida/energia e retorna ao centro | Pendente de execução final |
| T09 | Invulnerabilidade | Colisões imediatas não descontam vidas repetidamente | Pendente de execução final |
| T10 | Energia/vidas em zero | Estado Game Over | Pendente de execução final |
| T11 | 1000 pontos | Estado Vitória | Pendente de execução final |
| T12 | 60 segundos | Estado Vitória | Pendente de execução final |
| T13 | A cada 15 s | Fase aumenta e dificuldade cresce | Pendente de execução final |
| T14 | ESC durante jogo | Pausa | Pendente de execução final |
| T15 | ESC na pausa | Retorna ao jogo | Pendente de execução final |
| T16 | M na pausa | Retorna ao menu | Pendente de execução final |
| T17 | ENTER em Vitória/Game Over | Reinicia partida | Pendente de execução final |
| T18 | ESC em Vitória/Game Over | Volta ao menu | Pendente de execução final |
| T19 | X da janela | Encerra o programa | Pendente de execução final |

## Teste de reprodução

1. Usar Python 3.11 em uma instalação limpa.
2. Criar/ativar um ambiente virtual.
3. Executar `python -m pip install -r requirements.txt`.
4. Executar `python main.py`.
5. Registrar o resultado e, se possível, capturar uma tela da execução.

## Teste de código

O pacote final deve passar por:

```bash
python -m compileall .
```

Isso verifica a sintaxe dos módulos Python. A execução gráfica precisa ser validada em uma máquina com Pygame instalado.
