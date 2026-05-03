from fastapi import (
    FastAPI,
    Request,
    Response,
    HTTPException,
    Form,
    File,
    UploadFile,
    APIRouter,
)
from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
)
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from tools import clean
clean()

from schemas import UserResponse
from routers.users import (
    router as UserRouter,
)


# TODO(bader):
# [ ] - login system (with profile pictures)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(UserRouter, prefix="/user")


@app.get("/", name="home")
@app.get("/index.html")
def render_home(req: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        req,
        "home.html",
        {"title": "Home sweet home"},
    )
