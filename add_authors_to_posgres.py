import sys
import os
from pathlib import Path
import json
from datetime import datetime
from quotes.models import Author

import django
sys.path.append(str(Path(__file__).resolve().parent.parent))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10.settings")

django.setup()

json_path = Path(__file__).resolve().parent / 'users.json'

with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    author = Author(
        fullname=item['fullname'],
        born_date=item['born_date'],
        born_location=item['born_location'],
        description=item['description'],
        created_at=datetime.now(),
    )
    author.save()

