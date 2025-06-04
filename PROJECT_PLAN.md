# Project Plan - QA Task Manager

## Objetivo General

Desarrollar una API backend robusta para gestión de tareas enfocada en equipos de QA, con soporte para usuarios, roles, autenticación y control de accesos. El proyecto se implementa con FastAPI, priorizando escalabilidad, validación automática y buena documentación.

---

## Fases del Proyecto

| Fase       | Descripción                                   | Objetivos principales                         | Duración estimada |
|------------|-----------------------------------------------|----------------------------------------------|-------------------|
| Fase 1     | Base inicial y CRUD básico                     | Estructura, CRUD tareas, validación Pydantic| 1 semana          |
| Fase 2     | Persistencia y modelos de usuarios y roles    | Integración con base de datos (SQLite)       | 2 semanas         |
| Fase 3     | Autenticación y autorización                   | JWT, control de accesos según roles           | 3 semanas         |
| Fase 4     | Pruebas automáticas y mejora de documentación | Test unitarios e integración, mejorar docs   | 1 semana          |
| Fase 5     | Integración con equipo y despliegue inicial   | Uso colaborativo, despliegue local o nube     | 1 semana          |
| Fase 6     | Optimización, documentación y entrega final   | Refactor, documentación técnica, checklist QA     | 1 semana          |

---

## Roadmap por Sprint

## Sprint 1 – Base Inicial y CRUD Básico de Tareas  
**Duración estimada:** 1 semana  

**Objetivos:**  
Definir la estructura base del proyecto con FastAPI (dejando la versión legacy en Flask como referencia). Implementar CRUD básico para tareas con validación automática mediante Pydantic. Crear endpoints `GET /tasks` y `POST /tasks` que gestionen tareas en memoria. Configurar documentación automática (Swagger, Redoc) y establecer entorno con dependencias iniciales.

**Entregables:**  
- Estructura de carpetas y archivos base definida.  
- Endpoints `/tasks` funcionales (GET y POST).  
- Validaciones básicas de datos con Pydantic.  
- Documentación interactiva generada automáticamente.  
- `README.md` con instrucciones claras del proyecto.  
- `requirements.txt` con dependencias mínimas.  

**Tareas técnicas:**  
- Crear carpetas base (`service/app`, `api`, etc.) y archivos (`main.py`, `crud.py`, `models.py`, `schemas.py`).  
- Implementar modelos de datos con Pydantic.  
- Programar endpoints para crear y listar tareas (sin persistencia).  
- Configurar Swagger y Redoc.  
- Probar funcionalidad básica en Swagger UI o Postman.  

**Aprendizajes clave:**  
- Fundamentos de FastAPI y estructura de proyectos.  
- Validación automática con Pydantic.  
- Documentación API autogenerada.  
- Diferencias prácticas entre Flask y FastAPI.



---

## Sprint 2 – Persistencia y Gestión de Usuarios/Roles
**Duración estimada:** 1 semana

### Objetivos
- Implementar persistencia de datos usando SQLite con SQLAlchemy.
- Crear modelos de usuario y rol.
- Establecer relaciones entre tareas y usuarios.
- Agregar endpoints para gestión de usuarios (CRUD básico).
- Preparar la base para control de accesos por rol.

### Entregables
- Base de datos SQLite funcional con migraciones iniciales.
- Modelos ORM definidos y sincronizados (`User`, `Role`, `Task`).
- Endpoints CRUD de usuarios operativos.
- Asociaciones entre tareas y usuarios listas para extender.
- Documentación actualizada.

### Tareas Técnicas
- Configurar SQLAlchemy y conexión SQLite.
- Definir modelos ORM (`User`, `Role`, `Task`) y relaciones.
- Crear esquemas de validación con Pydantic para usuarios.
- Implementar endpoints `/users`, `/roles`.
- Probar operaciones básicas de persistencia.

---

## Sprint 3 – Autenticación y Autorización por Rol
**Duración estimada:** 1 semana

### Objetivos
- Implementar autenticación con JWT (login, tokens).
- Proteger rutas con dependencias de seguridad.
- Aplicar autorización por roles para controlar el acceso a operaciones CRUD.

### Entregables
- Sistema de autenticación con JWT operativo.
- Rutas protegidas por autenticación.
- Control de acceso por rol (admin, tester, lead, etc.).
- Registro y login funcionales.

### Tareas Técnicas
- Crear endpoints `/login`, `/signup`, `/me`.
- Implementar seguridad con `OAuth2PasswordBearer` y JWT.
- Añadir decoradores para roles en endpoints críticos.
- Crear middlewares o dependencias de autorización.
- Probar con distintos roles y accesos.

---

## Sprint 4 – Pruebas Automatizadas y Mejora de Documentación
**Duración estimada:** 1 semana

### Objetivos
- Escribir pruebas unitarias y de integración para endpoints principales.
- Validar reglas de negocio y control de accesos.
- Mejorar y extender documentación automática con ejemplos y descripciones.
- Establecer buenas prácticas de desarrollo y testeo continuo.

### Entregables
- Conjunto de pruebas automatizadas con cobertura inicial.
- Documentación Swagger/Redoc enriquecida.
- Script de testeo automatizado (`pytest`, `coverage`, etc.).
- Integración de pruebas locales en el flujo de desarrollo.

### Tareas Técnicas
- Implementar pruebas con `pytest` y `httpx`.
- Añadir validaciones de casos positivos y negativos.
- Documentar todos los endpoints con `responses`, `summary`, `description`.
- Automatizar pruebas locales con `Makefile` o `scripts`.

---

## Sprint 5 – Integración, Presentación al Equipo y Despliegue Inicial
**Duración estimada:** 1 semana

### Objetivos
- Preparar el sistema para uso real en entorno controlado (local/red interna).
- Crear usuarios y roles reales del equipo QA.
- Presentar funcionalidad al equipo para evaluación inicial.
- Implementar despliegue básico en entorno de pruebas.
- Recopilar feedback y registrar sugerencias para el backlog futuro.

### Entregables
- Versión funcional desplegada localmente o en servidor de pruebas.
- Módulo de gestión de usuarios y tareas operativo con control de acceso.
- Presentación ejecutiva del sistema al equipo QA.
- Documentación para onboarding de usuarios.
- Lista inicial de mejoras y ajustes sugeridos.

### Tareas Técnicas
- Crear script de inicialización de base de datos con roles y usuarios.
- Configurar entorno de ejecución (Docker, Uvicorn, .env, etc.).
- Realizar pruebas de extremo a extremo con datos reales.
- Preparar guía de uso inicial (README + onboarding markdown).
- Organizar reunión de presentación y recopilar retroalimentación.

### Aprendizajes clave
- Primer uso real del sistema por usuarios distintos al desarrollador.
- Validación de flujos completos y roles.
- Identificación de puntos de mejora funcional y técnica.

---
## Sprint 6 – Integración Final, Optimización y Documentación Profesional  
**Duración:** 1 semana  

### Objetivos:
- Consolidar la aplicación para uso real en equipo de QA.  
- Optimizar endpoints, manejo de errores y validaciones.  
- Mejorar estructura de código y aplicar principios de diseño limpio (Clean Architecture donde aplique).  
- Completar documentación técnica para desarrolladores y usuarios.  
- Preparar proyecto para mantenimiento continuo, pruebas ampliadas y escalabilidad.

### Entregables:
- Backend estable con estructura profesional y código optimizado.  
- Documentación técnica detallada (`README`, `API_DOCS`, `PROJECT_PLAN.md`, `CONTRIBUTING.md`).  
- Archivos de configuración listos para producción (por ejemplo, `.env.example`, configuración CORS, middlewares, etc.).  
- Manual de despliegue o guía para desarrolladores.  
- Checklist de control de calidad para futuras funcionalidades.

### Tareas técnicas:
- Refactorizar estructura de carpetas si es necesario.  
- Revisar y optimizar validaciones, manejo de errores y respuestas de API.  
- Implementar middlewares de logging y control de errores.  
- Separar configuraciones por entorno (`dev`, `prod`).  
- Finalizar documentación técnica detallada del proyecto.  
- Agregar sección de contribución y buenas prácticas de desarrollo.  
- Pruebas finales de validación funcional y técnica.

### Aprendizajes clave:
- Preparación de software para uso real y mantenibilidad a largo plazo.  
- Mejores prácticas de diseño y estructuración de proyectos FastAPI.  
- Organización de documentación profesional en proyectos colaborativos.

---

## Backlog Inicial

| Tarea                              | Prioridad | Estado     | Responsable | Notas                          |
|-----------------------------------|-----------|------------|-------------|-------------------------------|
| Definir estructura base            | Alta      | Completado | Juan David  |                               |
| CRUD tareas con validación         | Alta      | En progreso| Juan David  | Validar campos obligatorios   |
| Modelos ORM y SQLite               | Media     | Pendiente  | Juan David  |                               |
| CRUD usuarios y roles             | Media     | Pendiente  |             | Definir permisos básicos       |
| Autenticación JWT                  | Alta      | Pendiente  |             |                               |
| Control de acceso por roles        | Alta      | Pendiente  |             |                               |
| Pruebas unitarias y pytest         | Media     | Pendiente  |             |                               |
| Documentación Swagger y Redoc      | Media     | Parcial    | Juan David  | Completar en fases siguientes  |
| Despliegue y configuración         | Baja      | Pendiente  |             |                               |

---

## Próximos Pasos

1. Consolidar Sprint 1: terminar CRUD básico y validación.  
2. Definir modelos y esquema para persistencia.  
3. Configurar base de datos SQLite y conexión.  
4. Planificar Sprint 2 con tareas específicas.  
5. Crear backlog detallado en Notion con responsables y fechas.

---

## Contacto

#### Para dudas o sugerencias, contactar a Juan Saavedra, QA Tester e Ingeniero de Automatización / Futuro desarrollador.

---
