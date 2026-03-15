import json
from pprint import pprint

# str_json = '''{
#   "order_id": "ORD-2026-000123",
#   "created_at": "2026-02-26T00:14:00+03:00",
#   "customer": {
#     "id": 42,
#     "name": "Иван Петров",
#     "email": "ivan.petrov@example.com",
#     "address": {
#       "city": "Amsterdam",
#       "country": "NL",
#       "postal_code": "1012AB",
#       "street": "Damrak 1"
#     }
#   },
#   "items": [
#     {
#       "sku": "SKU-APPLE-001",
#       "title": "Яблоки, 1 кг",
#       "qty": 2,
#       "price_eur": 3.49
#     },
#     {
#       "sku": "SKU-MILK-002",
#       "title": "Молоко 1 л",
#       "qty": 1,
#       "price_eur": 1.29
#     }
#   ],
#   "payment": {
#     "method": "card",
#     "status": "paid",
#     "transaction_id": "TXN-9f3c1a2b"
#   },
#   "delivery": {
#     "type": "courier",
#     "eta_days": 2,
#     "tracking_number": "TRK-123-456-789"
#   },
#   "total_eur": 8.27,
#   "notes": null
# }
# '''

# json.loads() (строка → объект Python)
# json.dumps() (объект Python → строка)
# Чтение JSON-файла делается через json.load()
# запись — через json.dump()

# data = json.loads(str_json)


# with open('txt.json', 'w', encoding="utf-8") as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)

with open("txt.json", "r", encoding="utf-8") as file:
    data = json.load(file)

pprint(data)
