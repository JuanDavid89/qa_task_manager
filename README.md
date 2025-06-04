# QA Task Manager

## Objetivo del proyecto

Desarrollar una API backend para gestión de tareas orientada a equipos de QA, con soporte para usuarios, roles y control de accesos.  
El proyecto se implementa con FastAPI para asegurar escalabilidad, validación automática y documentación interactiva.  
Actualmente en fase inicial, se planea ampliar con funcionalidades completas para uso real en equipos.

## Estructura del proyecto

```text
qa_task_manager/
│
├── flask_version/          # Versión legacy para referencia
│   └── app.py
│
├── service/                # Backend principal basado en FastAPI
│   ├── main.py             # Punto de entrada
│   ├── app/
│   │   ├── crud.py         # Lógica de acceso y gestión de datos
│   │   ├── database.py     # Configuración y conexión a base de datos
│   │   ├── models.py       # Modelos ORM y entidades
│   │   ├── schemas.py      # Esquemas Pydantic para validación
│   │   ├── __init__.py
│   │   └── api/            # Rutas y endpoints organizados por recurso
│   │       ├── task.py
│   │       ├── users.py
│   │       └── __init__.py
│   └── __pycache__/
│
└── tests/                  # Pruebas unitarias y de integración

├── .gitignore
├── README.md
└── requirements.txt
```
---

## Estado actual (Sprint 1 - CRUD básico de tareas)

- Estructura de carpetas y archivos creada para FastAPI y Flask (versión legacy como referencia).

- Proyecto preparado para iniciar desarrollo, sin implementaciones funcionales aún.

- README y plan de proyecto iniciales creados.

- Entornos y dependencias listos para instalar (requirements.txt).
---

## Se implementó anterioremente para comparar 
✅ Flask
 GET /tasks: lista todas las tareas en memoria.

 POST /tasks: crea una nueva tarea con id, title y description.

✅ FastAPI
 GET /tasks: lista tareas usando tipado y response_model.

 POST /tasks: crea tareas con validación Pydantic, id autogenerado.

 ---

## Cómo ejecutar los servidores
🔹 Flask
---

```text
cd flask_version
python app.py
```
#### Acceso:

##### GET http://127.0.0.1:5000/tasks

##### POST http://127.0.0.1:5000/tasks
---
🔹 FastAPI
---
```text
cd fastapi_version
uvicorn main:app --reload
```
#### Acceso:

##### GET http://127.0.0.1:8000/tasks

##### POST http://127.0.0.1:8000/tasks

#### Documentación interactiva:

##### Documentación Swagger: http://127.0.0.1:8000/docs

##### Documentación Redoc: http://127.0.0.1:8000/redoc

---

## Cómo probar los endpoints
Ejemplo JSON para POST /tasks (ambos frameworks):
```text
{
  "title": "Presentación Xray",
  "description": "Crear documento para presentación de Xray al Equipo de QA"
}
```

## Recomendado:
- Usar Postman o Swagger UI (solo para FastAPI) para probar los endpoints.

- Verificar el status code y que el id se autogenere correctamente.

- Validar que el title sea obligatorio. Si falta, debe devolver error 400 o 422.

## Comparación Técnica 

| Aspecto              | Flask                           | FastAPI                                |
| -------------------- | ------------------------------- | -------------------------------------- |
| Curva de aprendizaje | Muy accesible                   | Moderna pero más estructurada          |
| Validación de datos  | Manual o con librerías externas | Automática con Pydantic                |
| Documentación        | Manual                          | Automática con Swagger/Redoc           |
| Tipado               | No nativo                       | Nativo con anotaciones y Pydantic      |
| Ideal para...        | Proyectos simples y rápidos     | APIs modernas, rápidas, con validación |


## Próximos pasos

1. Implementar CRUD básico de tareas con validación.

2. Añadir persistencia en base de datos (SQLite inicialmente).

3. Crear rutas para usuarios y roles con control de acceso.

4. Implementar autenticación y autorización.

5. Desarrollar pruebas automáticas.

6. Mejorar documentación y manejo de errores.

7. Iniciar integración con el equipo para uso colaborativo.

---

## Contacto

Cualquier duda o sugerencia, contactarme para continuar mejorando el proyecto.

### Proyecto creado por Juan David, QA Tester e Ingeniero de Automatización / Futuro Desarrollador Backend


