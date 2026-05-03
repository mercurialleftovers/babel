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


router = APIRouter()


@router.post("/register", name="user_register")
@router.post("/signup", name="user_signup")
# def signup_user(user: Annotated[UserCreate, Form()], userImage: Annotated[bytes|None, File()] = None):
# def signup_user(user: Annotated[UserCreate, Form()]):
def signup_user(
    user: UserCreate = Form(),
    userImage: UploadFile = File(),
):
    print(user)
    print(userImage)
    return "done"
