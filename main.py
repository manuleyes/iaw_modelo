from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from data.dao.dao_alumnos import DaoAlumnos

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

dao = DaoAlumnos()


# Pagina 1 – Listado de alumnos con todas sus notas
@app.get("/alumnos", response_class=HTMLResponse)
async def listar_alumnos(request: Request):
    alumnos = dao.get_all()
    return templates.TemplateResponse(
        "alumnos.html",
        {"request": request, "alumnos": alumnos}
    )


# Pagina 2 – Filtrar alumnos con media superior a un numero
@app.get("/filtrar", response_class=HTMLResponse)
async def filtrar_get(request: Request):
    return templates.TemplateResponse(
        "filtrar.html",
        {"request": request, "alumnos": None, "numero": None}
    )


@app.post("/filtrar", response_class=HTMLResponse)
async def filtrar_post(request: Request, numero: float = Form(...)):
    alumnos = dao.filtrar_por_media(numero)
    return templates.TemplateResponse(
        "filtrar.html",
        {"request": request, "alumnos": alumnos, "numero": numero}
    )


# Pagina 3 – Cambiar nombre (solo si no tiene ninguna nota suspendida)
@app.get("/cambiar_nombre", response_class=HTMLResponse)
async def cambiar_nombre_get(request: Request):
    alumnos = dao.get_aprobados()
    return templates.TemplateResponse(
        "cambiar_nombre.html",
        {"request": request, "alumnos": alumnos, "mensaje": None}
    )


@app.post("/cambiar_nombre", response_class=HTMLResponse)
async def cambiar_nombre_post(
    request: Request,
    alumno_id: int = Form(...),
    nuevo_nombre: str = Form(...)
):
    filas = dao.cambiar_nombre(alumno_id, nuevo_nombre)
    alumnos = dao.get_aprobados()
    if filas > 0:
        mensaje = f"Nombre actualizado correctamente a '{nuevo_nombre}'."
    else:
        mensaje = "No se pudo actualizar: el alumno tiene notas suspendidas."
    return templates.TemplateResponse(
        "cambiar_nombre.html",
        {"request": request, "alumnos": alumnos, "mensaje": mensaje}
    )


# Pagina 4 – Actualizar notas de un alumno
@app.get("/actualizar_notas", response_class=HTMLResponse)
async def actualizar_notas_get(request: Request):
    alumnos = dao.get_all()
    return templates.TemplateResponse(
        "actualizar_notas.html",
        {"request": request, "alumnos": alumnos, "mensaje": None}
    )


@app.post("/actualizar_notas", response_class=HTMLResponse)
async def actualizar_notas_post(
    request: Request,
    alumno_id: int = Form(...),
    nota1: int = Form(...),
    nota2: int = Form(...),
    nota3: int = Form(...)
):
    dao.actualizar_notas(alumno_id, nota1, nota2, nota3)
    alumnos = dao.get_all()
    return templates.TemplateResponse(
        "actualizar_notas.html",
        {"request": request, "alumnos": alumnos, "mensaje": "Notas actualizadas correctamente."}
    )


# Pagina 5 – Borrar alumno (solo los que tienen todo aprobado)
@app.get("/borrar", response_class=HTMLResponse)
async def borrar_get(request: Request):
    alumnos = dao.get_aprobados()
    return templates.TemplateResponse(
        "borrar.html",
        {"request": request, "alumnos": alumnos, "mensaje": None}
    )


@app.post("/borrar", response_class=HTMLResponse)
async def borrar_post(request: Request, alumno_id: int = Form(...)):
    nombre = dao.borrar(alumno_id)
    alumnos = dao.get_aprobados()
    return templates.TemplateResponse(
        "borrar.html",
        {
            "request": request,
            "alumnos": alumnos,
            "mensaje": f"Se borró al alumno '{nombre}' correctamente."
        }
    )
