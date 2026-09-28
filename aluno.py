from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplina = []
        self.notas_por_disciplina = {}

    def matricular(self, disciplina: Disciplina):
        if disciplina not in self.disciplina:
            self.disciplina.append(disciplina)