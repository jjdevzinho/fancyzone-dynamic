# FancyZones Dynamic Size

Este script permite ajustar dinamicamente o tamanho das zonas e janelas do FancyZones do PowerToys, mas apenas em um layout de 2 colunas.

## Requisitos

- Python 3.x
- PowerToys com FancyZones habilitado

## Instalação

1. Clone este repositório ou baixe o arquivo `fancyZone.py`.
2. Instale as bibliotecas necessárias executando o seguinte comando:

    ```sh
    pip install keyboard pyautogui
    ```

## Configuração

1. Certifique-se de que você tem um layout de 2 zonas horizontais no FancyZones com o nome `dynamic`.
2. Defina o atalho para este layout como `Ctrl + Win + Alt + 1`. Se você preferir outro atalho, ajuste o script para refletir isso.

## Uso

1. Execute o script utilizando o arquivo .bat:

    ```sh
    start.bat
    ```

2. Use os seguintes atalhos para controlar as zonas:

    - `Alt + =` para aumentar a primeira zona em 5%.
    - `Alt + -` para diminuir a primeira zona em 5%.
    - `Alt + X` para inverter as zonas.

3. Para parar o script, pressione `Esc`.

## Iniciar com o Windows

Para iniciar o script junto com o Windows, crie um atalho do arquivo [start.bat](http://_vscodecontentref_/1) e coloque-o na pasta de inicialização do Windows. Você pode acessar esta pasta pressionando `Win + R`, digitando `shell:startup` e pressionando Enter. Em seguida, mova o atalho para esta pasta.

## Nota

Este script foi projetado para funcionar apenas com layouts de 2 zonas horizontais. Certifique-se de que o layout tenha o nome `dynamic` e que o atalho esteja mapeado corretamente no script. O script lê e edita o arquivo custom-layout de nome `dynamic`.

## Exemplo de Configuração do FancyZones

- Nome do layout: `dynamic`
- Atalho: `Ctrl + Win + Alt + 1`

Se você usar um nome ou atalho diferente, ajuste a variável [layout_file](http://_vscodecontentref_/2) no script conforme necessário.

```python
layout_file = os.path.join(local_appdata, r"Microsoft\PowerToys\FancyZones\custom-layouts.json")
```

## Possível Problema

Os atalhos `Alt + =` e `Alt + -` podem não funcionar quando o Gerenciador de Tarefas está aberto e focado. Isso pode ser um bug do Gerenciador de Tarefas ou um atalho não documentado. Como alternativa, você pode mudar os atalhos no script ou simplesmente trocar o foco para outra janela.