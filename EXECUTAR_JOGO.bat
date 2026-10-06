@echo off
title Neon Escape
echo =====================================
echo        NEON ESCAPE - CONFIGURACAO
echo =====================================
echo.

where py >nul 2>nul
if errorlevel 1 (
    echo Python Launcher nao encontrado.
    echo No VS Code, selecione o Python 3.11 e execute:
    echo python -m pip install -r requirements.txt
    echo python main.py
    pause
    exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
    echo Criando ambiente virtual com Python 3.11...
    py -3.11 -m venv .venv
    if errorlevel 1 (
        echo Nao foi possivel criar o ambiente Python 3.11.
        pause
        exit /b 1
    )
)

echo Instalando/verificando Pygame...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo Falha na instalacao das dependencias.
    pause
    exit /b 1
)

echo.
echo Iniciando Neon Escape...
".venv\Scripts\python.exe" main.py

echo.
echo Jogo encerrado.
pause
