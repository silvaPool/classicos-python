from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') #tipo para variável
D = TypeVar('D') #tipo para domínio

#Classe-base para todas as restrições
class Constraint(Generic[V, D], ABC):
    #As variáveis sujeitas à restrição
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    #deve ser sobrescrito pelas subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


#Um problema de satisfação de restrições é composto de variáveis do tipo V
#que têm intervalos de valores conhecidos como domínios do tipo D e restrições
#que determinam se a escolha de domínio de uma variável em particular é válida
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables #variáveis a serem restringidas
        self.domains: Dict[V, List[D]] = domains #domínio de cada variável
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    #Verifica se a atribuição de valor é consistente consultando todas as restrições
    #para a dada variável em relação a essa atribuição
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True