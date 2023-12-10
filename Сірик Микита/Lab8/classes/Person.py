import enum

from classes.AssessVisitor import AssessVisitor
from dataclasses import dataclass


@dataclass
class PersonInfo:
    id: int
    first_name: str
    second_name: str
    role: enum


class Person:

    def __init__(self, person_info: PersonInfo) -> None:
        self.id = person_info.id
        self.first_name = person_info.first_name
        self.second_name = person_info.second_name
        self.role = person_info.role

    def get_info(self) -> str:
        return f"(ID={self.id}, first_name={self.first_name}, second_name={self.second_name}, role={self.role})"

    def accept(self, assess_visitor: AssessVisitor):
        pass
