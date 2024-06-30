from pydantic import BaseModel


class Users(BaseModel):
    login: str
    password: str
    fio: str
    academic: str


class Academic(BaseModel):
    name: str


class Ads(BaseModel):
    info: str
    data: str


class Grades(BaseModel):
    student_name: str
    mark: int
    academic_name: str
    semester: int


class Students(BaseModel):
    fio: str
    groups_name: str


class Groups(BaseModel):
    short_name: int
    full_name: str
    teacher: str



