# NEON ESCAPE — Jogo 2D em Python + Pygame

## 1. Identificação

**Nome:** Neon Escape — Fuga da Cidade  
**Gênero:** arcade/sobrevivência  
**Disciplina:** Computação Gráfica  
**Tecnologia:** Python 3 + Pygame

## 2. Descrição

Neon Escape é um jogo 2D de sobrevivência ambientado em uma cidade futurista. O jogador controla uma unidade de fuga, coleta núcleos de energia e bônus e evita drones inimigos enquanto a dificuldade aumenta.

O objetivo é atingir **1000 pontos** ou sobreviver durante **60 segundos**. A partida termina em vitória ao cumprir uma dessas condições e em Game Over quando as vidas ou a energia chegam a zero.

## 3. Requisitos

- Python 3.11 recomendado para a execução deste pacote.
- Pygame 2.6.1.
- Windows, Linux ou macOS.

## 4. Instalação reproduzível

Abra o terminal dentro da pasta do projeto.

### Windows PowerShell

```powershell
python -m pip install -r requirements.txt
```

Se houver mais de uma versão do Python instalada, selecione explicitamente o Python 3.11 no VS Code ou execute:

```powershell
py -3.11 -m pip install -r requirements.txt
```

### Ambiente virtual recomendado

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 5. Execução

```bash
python main.py
```

No VS Code, abra `main.py` e use **Run Python File**.

## 6. Controles

- **WASD / setas:** movimentação.
- **ENTER:** iniciar/reiniciar.
- **I:** instruções no menu.
- **ESC:** pausar durante o jogo.
- **ESC:** voltar ao menu nas instruções/telas finais.
- **ESC:** continuar durante a pausa.
- **M:** voltar ao menu durante a pausa.
- **X da janela:** encerrar.

## 7. Regras

- Núcleo verde: +100 pontos e recuperação de energia.
- Núcleo amarelo: +250 pontos.
- Colisão com drone: perde uma vida e 30 de energia.
- Após uma colisão, o jogador recebe 1,2 s de invulnerabilidade.
- Com 0 vidas ou 0 energia: Game Over.
- Com 1000 pontos ou 60 segundos: Vitória.
- A cada 15 segundos ocorre progressão de fase.
- Conforme a fase aumenta, mais inimigos podem aparecer e eles ficam mais rápidos.

## 8. Técnicas de Computação Gráfica

1. **Renderização 2D por primitivas:** círculos, retângulos, linhas e polígonos.
2. **Animação baseada em tempo:** movimento oscilatório dos coletáveis e dos inimigos.
3. **Transformação de escala:** pulso visual do personagem calculado por seno.
4. **Composição por camadas:** fundo, grade, prédios, coletáveis, inimigos, jogador, partículas e HUD.
5. **Paralaxe simples:** deslocamento diferente das camadas do cenário.
6. **Sistema de partículas:** explosões visuais em coleta, colisão e mudança de fase.
7. **Coordenadas e colisão:** `pygame.Rect` para limites e interseção espacial.
8. **Interface gráfica/HUD:** pontuação, vidas, fase, tempo e barra de energia.

## 9. Colisões

As entidades possuem áreas retangulares representadas por `pygame.Rect`. A detecção usa `rect.colliderect()`. Quando há interseção, o jogo aplica a resposta correspondente: coleta de item ou dano do jogador. O jogador também usa `clamp_ip()` para permanecer dentro da área jogável.

## 10. Progressão

A fase aumenta a cada 15 segundos, limitada a oito fases. O intervalo de surgimento de inimigos diminui e o limite de inimigos cresce conforme a fase. A velocidade dos drones também aumenta com a dificuldade.

## 11. Estrutura

```text
NeonEscape/
├── main.py
├── settings.py
├── game.py
├── player.py
├── enemy.py
├── collectible.py
├── particles.py
├── ui.py
├── requirements.txt
├── README.md
├── CREDITOS.md
├── EVOLUCAO.md
├── TESTES.md
├── APRESENTACAO.md
├── APRESENTACAO.pptx
└── APRESENTACAO.pdf
```

## 12. Qualidade e testes

O pacote inclui `TESTES.md` com os testes funcionais e de reprodução. Antes da entrega, executar:

```bash
python -m compileall .
```

Depois executar o jogo e preencher os resultados de `TESTES.md`.

## 13. Evolução

O arquivo `EVOLUCAO.md` organiza os quatro marcos exigidos pelo enunciado e indica quais evidências devem ser anexadas. Não foram inventadas capturas históricas.

## 14. Créditos e uso de IA

Consulte `CREDITOS.md`. O uso de ChatGPT é declarado conforme solicitado pelo enunciado, incluindo finalidade, partes afetadas e método de validação.

## 15. Referências técnicas

- Pygame Documentation — https://www.pygame.org/docs/
- Python Games — https://github.com/itspyguru/Python-Games
- Pygame Simple Examples — https://github.com/Leonardpepa/pygame-simple-examples
- Python Games Collection — https://github.com/veddegre/python-games-collection

## 16. Checklist final

- [ ] Jogo inicia pelo comando do README.
- [ ] Controles, regras e objetivo conferidos.
- [ ] Vitória, Game Over e reinício testados.
- [ ] Colisões e limites testados.
- [ ] `requirements.txt` testado em ambiente limpo.
- [ ] Caminhos são relativos.
- [ ] Não há senhas ou caminhos pessoais no código.
- [ ] Capturas reais de evolução inseridas na apresentação.
- [ ] Créditos e uso de IA declarados.
- [ ] Vídeo curto de segurança preparado.
- [ ] Backup do projeto criado.
