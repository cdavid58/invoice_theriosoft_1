import requests, json

url = "http://localhost:8000/api/Create_Invoice/"
for i in range(3000):
  print(i)
  payload = json.dumps({
    "prefix": "FFET",
    "number": i,
    "typeDocumentId": 1,
    "paymentForm": 1,
    "paymentMethods": 10,
    "durationMeasure": 0,
    "description": "Prueba",
    "code": "001",
    "price": "100",
    "quanty": "100",
    "ipo": "0",
    "iva": "19",
    "client": 1,
    "company": 1
  })
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
