# Horizon Forge Test Script
# Автор: Твое имя

import json
from utils import helper_function

# Загрузка конфигурации
with open('config.json') as f:
    config = json.load(f)

print("Запуск Horizon Forge Module")
helper_function(config)
