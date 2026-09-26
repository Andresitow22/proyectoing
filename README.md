# Avisens API

API REST con Django + Django REST Framework para gestionar usuarios, galpones, sensores y sus lecturas.

## Módulos

| App | Modelo(s) | Endpoints |
|---|---|---|
| `users` | `User` | `/api/users/`, `/api/auth/me/` |
| `galpones` (nueva) | `Galpon`: nombre, ubicación, capacidad, usuario dueño | `/api/galpones/` |
| `sensores` (nueva) | `Sensor`: nombre, tipo, unidad, activo, galpón · `Lectura`: sensor, valor, fecha | `/api/sensores/`, `/api/lecturas/` |

Relaciones: un **usuario** tiene varios **galpones**, cada galpón tiene varios **sensores** y cada sensor registra varias **lecturas**.
Cada endpoint acepta `GET`, `POST`, `PUT`, `PATCH` y `DELETE`.

## Cómo ejecutarlo

```bash
python -m venv env
source env/Scripts/activate      # Windows (Git Bash)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Documentación interactiva: http://127.0.0.1:8000/swagger/

## Endpoints probados

Las capturas de las pruebas hechas desde Swagger están en [`capturas/`](capturas/):

| Captura | Prueba | Resultado |
|---|---|---|
| `00_swagger_endpoints.png` | Lista de endpoints en Swagger | — |
| `01_galpones_POST.png` | Crear galpón | 201 |
| `02_galpones_GET_lista.png` | Listar galpones | 200 |
| `03_galpones_GET_detalle.png` | Ver un galpón | 200 |
| `04_galpones_PATCH.png` | Cambiar capacidad | 200 |
| `05_galpones_PUT.png` | Actualizar galpón completo | 200 |
| `06_sensores_POST.png` | Crear sensor | 201 |
| `07_sensores_POST_tipo_invalido_400.png` | Crear sensor con tipo no válido | 400 |
| `08_sensores_GET_lista.png` | Listar sensores | 200 |
| `09_sensores_PATCH.png` | Desactivar sensor | 200 |
| `10_lecturas_POST.png`, `11_lecturas_POST_2.png` | Registrar lecturas | 201 |
| `12_lecturas_GET_lista.png` | Listar lecturas | 200 |
| `13_lecturas_DELETE.png` | Borrar lectura | 204 |
| `14_galpones_POST_temporal.png`, `15_galpones_DELETE.png` | Crear y borrar galpón | 201 / 204 |
