# Implementación servidor HTTP

Desarrollamos un servidor HTTP en Python que permite manejar múltiples conexiones de clientes de forma concurrente, permite obtener respuestas estandar, leer archivos y crear archivos. 

# Librerias utilizadas

Utilizamos la libreria socket para tener el protocolo TCP.
Utilizamos la libreria concurrent.futures para maneja la concurrencia de los clientes.

# Rutas

## /index

```bash
curl -i http://localhost:4221/files/index.html
```

## GET /files/{args} 
```bash
curl -i http://localhost:4221/files/index.html
```

## /user-agent
```bash
curl -i http://localhost:4221/files/index.html
```
## POST /files/{args}
```bash
curl -v --data "print('hello world')" -H "Content-Type: application/octet-stream" http://localhost:4221/files/H.py
```

## Como ejecutar

```bash
cd app
python main.py

```

