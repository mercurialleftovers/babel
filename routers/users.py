from typing import Annotated
from fastapi import (
    FastAPI,
    Request,
    Response,
    HTTPException,
    Form,
    APIRouter,
    File,
    UploadFile,
)
from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
)
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# TODO(bader): why is schemas accessible from this directory, even if it is in parent,
# maybe because fastapi runs in parent, so everything there is accessible ?
# and no need for relative paths
from schemas import (
    UserResponse,
    UserCreate,
)


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/register", name="user_register_view")
def render_user_register(req: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        req,
        "user_register.html",
        {"title": "add new user"},
    )


@router.post("/register", name="user_register")
@router.post("/signup", name="user_signup")
def register_user(
    user: Annotated[UserCreate, Form()],
) -> UserResponse:
    return user


@router.post("/add_picture", name="user_add_picture")
def user_add_picture(
    userImage: UploadFile | None = None,
):
    return {"userImage": userImage}
