#data/types.py
from distutils.command.build_scripts import first_line_re

import strawberry
from strawberry import auto
from strawberry_django.filters import FilterLookup

from typing import List
from . import models



@strawberry.django.filters.filter(models.Person)
class PersonFilter:
    id:auto
    fullname: FilterLookup[str]
    dateofbirth: str
    dlnumber: str

@strawberry.django.type(models.Person, filters=PersonFilter)
class Person:
    id:auto
    fullname: str
    dateofbirth: str
    dlnumber: str


@strawberry.django.input(models.Person)
class PersonInput:
    id:auto
    fullname: str
    dateofbirth: str
    dlnumber: str

@strawberry.django.input(models.Person, partial=True)
class PersonPartialInput(PersonInput):
    id:auto
    fullname: auto
    dateofbirth: auto
    dlnumber: auto