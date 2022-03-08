from enum import unique
from itertools import count
from operator import index
from peewee import *
import datetime
import sqlite3

db = SqliteDatabase('tp_adv.db')


class Alumnos(Model):
    id = AutoField()
    nombre = CharField()
    apellido = CharField()
    dni = CharField(unique=True)

    class Meta:
        database = db


db.connect()
db.create_tables([Alumnos])


class Funciones():
    def alta(self, name, last_name, dni):
        data = Alumnos(nombre=name,
                       apellido=last_name,
                       dni=dni
                       )
        data.save()

    def baja(self, aid):
        Alumnos.delete().where(Alumnos.id == aid).execute()

    def modificar(self, name, last_name, dni, aid):
        Alumnos.update(nombre=name,
                       apellido=last_name,
                       dni=dni).where(Alumnos.id == aid).execute()
