import json
import os
import keyboard
import pyautogui

# Usar variáveis de ambiente para acessar os caminhos
local_appdata = os.getenv('LOCALAPPDATA')
layout_file = os.path.join(local_appdata, r"Microsoft\PowerToys\FancyZones\custom-layouts.json")

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def modify_zone(percent_change):
    data = load_json(layout_file)
    for layout in data["custom-layouts"]:
        if layout["name"] == "dynamic":
            columns_percentage = layout["info"]["columns-percentage"]
            
            col1 = columns_percentage[0] + percent_change * 100
            col2 = columns_percentage[1] - percent_change * 100

            col1 = max(0, min(10000, col1))
            col2 = max(0, min(10000, col2))

            layout["info"]["columns-percentage"] = [col1, col2]
            save_json(layout_file, data)
            pyautogui.hotkey('ctrl', 'win', 'alt', '1')
            return

def invert_zones():
    data = load_json(layout_file)
    for layout in data["custom-layouts"]:
        if layout["name"] == "dynamic":
            columns_percentage = layout["info"]["columns-percentage"]
            
            col1, col2 = columns_percentage[1], columns_percentage[0]

            layout["info"]["columns-percentage"] = [col1, col2]
            save_json(layout_file, data)
            pyautogui.hotkey('ctrl', 'win', 'alt', '1')
            return

def run_script():
    keyboard.add_hotkey('alt+=', lambda: modify_zone(5))
    keyboard.add_hotkey('alt+-', lambda: modify_zone(-5))
    keyboard.add_hotkey('alt+x', invert_zones)
    keyboard.wait('esc')

run_script()