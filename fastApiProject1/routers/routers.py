from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
import csv
from db import query_data
from database.database import User, Academic, Grade, Student, Group
from io import StringIO
from sqlalchemy.orm import Session

router = APIRouter()
@router.post("/users/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    csv_reader = csv.reader(StringIO(contents.decode("utf-8")), delimiter=',')

    try:
        for row in csv_reader:
            if row:  
                id, fio, group_name, phone, snils, god_postupleniya, passport = row
                
                
               
                user = Student(
                    fio=fio,
                    group_name=group_name,
                    phone=phone,
                    snils=snils,
                    god_postupleniya=god_postupleniya,
                    passport=passport
                )
                
                query_data.add(user)
        
        query_data.commit()
    except Exception as e:
        query_data.rollback()
        raise e
    finally:
        query_data.close()



@router.post("/groups/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    csv_reader = csv.reader(StringIO(contents.decode("utf-8")), delimiter=',')

    try:
        for row in csv_reader:
            if row:  
                id, short_name, full_name = row
                
                
                
                group = Group(
                    short_name=short_name,
                    full_name=full_name
                )

                query_data.add(group)
        
        query_data.commit()
    except Exception as e:
        query_data.rollback()
        raise e
    finally:
        query_data.close()

@router.post("/academics/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    csv_reader = csv.reader(StringIO(contents.decode("utf-8")), delimiter=',')
    
    try:
        for row in csv_reader:
            if row:  
                id, name = row
                
                
                
                group = Academic(
                    name=name
                )

                
               
                query_data.add(group)
        
        query_data.commit()
    except Exception as e:
        query_data.rollback()
        raise e
    finally:
        query_data.close()


@router.post('/grades/')
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    csv_reader = csv.reader(StringIO(contents.decode("utf-8")), delimiter=',')
    
    try:
        for row in csv_reader:
            if row:  
                
                id, mark, semester,academic_name, student_name , teacher_name = row
                
                
               
                group = Grade(
                    mark=mark,
                    semester=semester,
                    academic_name=academic_name,
                    student_name=student_name,
                    teacher_name=teacher_name,
                )

            
                query_data.add(group)
        
        query_data.commit()
    except Exception as e:
        query_data.rollback()
        raise e
    finally:
        query_data.close()

@router.post('/users/')

async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    csv_reader = csv.reader(StringIO(contents.decode("utf-8")), delimiter=',')
    
    try:
        for row in csv_reader:
            if row:  
                id, fio, login, password, academic_id = row
                
                
                
                group = User(
                    fio=fio,
                    login=login,
                    password=password,
                    academic_id=academic_id,
                )
                
               
                query_data.add(group)
            query_data.commit()
    except Exception as e:
        query_data.rollback()
        raise e
    finally:
        query_data.close()
            


