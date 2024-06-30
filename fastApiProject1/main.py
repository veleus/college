from fastapi import FastAPI
from db import engine, Session
from database.database import Base

from starlette_admin.contrib.sqla import Admin, ModelView
from database.database import User, Group, Academic, Grade, Student
from authorized import auth
from routers.routers import router
import uvicorn

app = FastAPI()
app.include_router(router)



admin = Admin(engine, title="Админка", base_url='/foobaradminmain')
admin.add_view(ModelView(User))
admin.add_view(ModelView(Group))
admin.add_view(ModelView(Academic))
admin.add_view(ModelView(Grade))
admin.add_view(ModelView(Student))
admin.mount_to(app)

Base.metadata.create_all(bind=engine)


app.include_router(auth.app)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)