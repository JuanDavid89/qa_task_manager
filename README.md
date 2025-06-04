# QA Task Manager — Comparativo Flask vs FastAPI

## Objetivo del proyecto

Desarrollar dos mini APIs paralelas para gestionar tareas de testing (QA Task Manager) usando Flask y FastAPI.  
El propósito es comprender las diferencias, ventajas y buenas prácticas de ambos frameworks en proyectos reales.

## Estructura del proyecto

```text
qa_task_manager/
│
├── flask_version/
│ └── app.py # API básica con Flask
│
├── fastapi_version/
│ └── main.py # API con FastAPI y validación Pydantic
│
└── README.md # Documentación y comparación
```

## Estado actual (Sprint 1 - CRUD básico de tareas)

- Carpetas y archivos inicializados.  
- Entornos instalados con Flask y FastAPI (`pip install flask fastapi uvicorn`).  
- Implementado: 

✅ Flask
 GET /tasks: lista todas las tareas en memoria.

 POST /tasks: crea una nueva tarea con id, title y description.

✅ FastAPI
 GET /tasks: lista tareas usando tipado y response_model.

 POST /tasks: crea tareas con validación Pydantic, id autogenerado.

## Cómo ejecutar los servidores
🔹 Flask

```text
cd flask_version
python app.py

Acceso:

GET http://127.0.0.1:5000/tasks

POST http://127.0.0.1:5000/tasks
```
🔹 FastAPI
```text
cd fastapi_version
uvicorn main:app --reload

Acceso:

GET http://127.0.0.1:8000/tasks

POST http://127.0.0.1:8000/tasks

Documentación Swagger: http://127.0.0.1:8000/docs

Documentación Redoc: http://127.0.0.1:8000/redoc
```

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

1. Agregar validaciones adicionales en ambos frameworks.

2. Implementar PUT /tasks/{id} y DELETE /tasks/{id}.

3. Añadir manejo de errores más robusto.

4. Persistencia básica en archivo JSON o base de datos.

5. Comparativa más profunda en cuanto a rendimiento, extensibilidad y documentación.

---

## Contacto

Cualquier duda o sugerencia, contactarme para continuar mejorando el proyecto.

### Proyecto creado por Juan David, QA Tester e Ingeniero de Automatización / Futuro Desarrollador Backend.


