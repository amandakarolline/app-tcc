import requests


class BaseAPI:
    def __init__(self):
        self.base_url = "http://localhost:1337/api"

    def get(self, endpoint):
        response = requests.get(f'{self.base_url}/{endpoint}')
        response.raise_for_status()
        return response.json()


class Discente(BaseAPI):
    def todos(self):
        discentes = self.get('discentes')
        return discentes

    def unico(self, atributo, valor):
        discente = self.get(f'discentes/{atributo}/{valor}')
        return discente


class Componente(BaseAPI):
    def todos(self):
        componentes = self.get('componentes-curriculares')
        return componentes

    def unico(self, atributo, valor):
        componente = self.get(f'componentes-curriculares/{atributo}/{valor}')
        return componente


class Turma(BaseAPI):
    def todos(self):
        turmas = self.get('turmas')
        return turmas

    def unico(self, atributo, valor):
        turma = self.get(f'turmas/{atributo}/{valor}')
        return turma


class Matricula(BaseAPI):
    def todos(self):
        matriculas = self.get('matriculas')
        return matriculas

    def unico(self, atributo, valor):
        matricula = self.get(f'matriculas/{atributo}/{valor}')
        return matricula


class GradeComponente(BaseAPI):
    def todos(self):
        gradeComponente = self.get('grade-componentes')
        return gradeComponente

    def unico(self, atributo, valor):
        gradeComponente = self.get(f'grade-componentes/{atributo}/{valor}')
        return gradeComponente

    def dois_atributos(self, atributo1, valor1, atributo2, valor2):
        gradeComponente = self.get(f'grade-componentes/{atributo1}/{valor1}/{atributo2}/{valor2}')
        return gradeComponente


class Docente(BaseAPI):
    def todos(self):
        docentes = self.get('docentes')
        return docentes

    def unico(self, atributo, valor):
        docente = self.get(f'docentes/{atributo}/{valor}')
        return docente
