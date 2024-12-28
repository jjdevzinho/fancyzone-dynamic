import json
import os
import keyboard
import pyautogui
import pystray
from PIL import Image
from threading import Thread

# Usar variáveis de ambiente para acessar os caminhos
local_appdata = os.getenv('LOCALAPPDATA')
layout_file = os.path.join(local_appdata, r"Microsoft\PowerToys\FancyZones\custom-layouts.json")
fancyzones_icon_path = os.path.join(local_appdata, r"PowerToys\RunPlugins\PowerToys\Images\FancyZones.png")

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def modify_layout(columns_percentage):
    data = load_json(layout_file)
    layout = data["custom-layouts"][0]  # Acessa o primeiro (e único) layout
    if layout["name"] == "dynamic":
        layout["info"]["columns-percentage"] = columns_percentage
        save_json(layout_file, data)
        pyautogui.hotkey('ctrl', 'win', 'alt', '1')

def modify_zone(percent_change):
    data = load_json(layout_file)
    layout = data["custom-layouts"][0]  # Acessa o primeiro (e único) layout
    if layout["name"] == "dynamic":
        columns_percentage = layout["info"]["columns-percentage"]
        
        col1 = columns_percentage[0] + percent_change * 100
        col2 = columns_percentage[1] - percent_change * 100

        col1 = max(0, min(10000, col1))
        col2 = max(0, min(10000, col2))

        modify_layout([col1, col2])

def invert_zones():
    data = load_json(layout_file)
    layout = data["custom-layouts"][0]  # Acessa o primeiro (e único) layout
    if layout["name"] == "dynamic":
        columns_percentage = layout["info"]["columns-percentage"]
        
        col1, col2 = columns_percentage[1], columns_percentage[0]

        modify_layout([col1, col2])

def load_fancyzones_icon():
    if os.path.exists(fancyzones_icon_path):
        return Image.open(fancyzones_icon_path)
    else:
        return None

def on_activate(icon, item):
    global running
    running = True

def on_deactivate(icon, item):
    global running
    running = False

def on_exit(icon, item):
    global running
    running = False
    icon.stop()

def run_script():
    global running
    running = True
    keyboard.add_hotkey('alt+=', lambda: modify_zone(5), suppress=True)
    keyboard.add_hotkey('alt+-', lambda: modify_zone(-5), suppress=True)
    keyboard.add_hotkey('alt+x', invert_zones, suppress=True)
    while running:
        keyboard.wait('esc')

icon = pystray.Icon("FancyZones")
icon_image = load_fancyzones_icon()
if icon_image:
    icon.icon = icon_image
else:
    exit(1)

icon.title = "FancyZones Controller"
icon.menu = pystray.Menu(
    pystray.MenuItem("Ativar", on_activate),
    pystray.MenuItem("Desativar", on_deactivate),
    pystray.MenuItem("Sair", on_exit)
)

# Ativar o script por padrão ao iniciar
thread = Thread(target=run_script)
thread.start()
icon.run()