import random
#from collections import sort
import string
class Clausula:
    """
    Esta clase nos permite modelar las Clausulas correspondientes, así
    como obtener su valor de verdad
    """
    def __init__(self, variables:list, flag_bool="+"):
        self.variables=variables
        self.flag_bool:str=flag_bool

    def __eq__(self, other):
        if not isinstance(other, Clausula):
            return False
        self.variables.sort()
        other.variables.sort()
        return self.variables == other.variables and self.flag_bool==other.flag_bool

    def agrega_variable(variable):
        """
        Permite agregar una variable a la lista de variables de la Clausula
        aunque la lista luce de esta forma [x,y,z], el concepto que tratamos
        a través de ella es un OR, i.e (x V y V z)
        """
        self.variables.append(variable)

    def get_valor_booleano(self):
        """
        Deveuelve el valor de la evaluación de todas las variables
        dentro de la claúsula conectadas por OR
        """
        evaluacion=False
        fst_time=True
        for var in self.variables:
            if fst_time:
                evaluacion=var.get_valor_booleano()
                fst_time!=fst_time
            else:
                evaluacion |=var.get_valor_booleano()
        if self.flag_bool=="-":
            return not evaluacion
        return evaluacion

    def __str__(self):
        out_str="("
        for var in self.variable:
            out_str+=str(var)+ "V"
        out_str=")"
        return out_str


class Variable:
    """
    Esta clase nos permitirá modelar variables, tales que contienen un
    valor booleano y se representan a través de un caracter
    """
    def __init__(self,variable, valor, boolean_flag="+"):
        """
        Constructor de variables
        variable:=char
        valor:=boolean
        boolean_flag:str(+,-)
        """
        self.variable=variable
        self.valor=valor
        self.boolean_flag=boolean_flag

    def get_valor_booleano(self):
        """
        Devuelve el valor booleano de la variable
        """
        if self.boolean_flag=="-":
            return not self.valor
        return self.valor

    def __eq__(self,other):
        if not isinstance(Variable, other):
            return False
        return self.variable==other.variable

    def __str__(self):
        out_str=""
        if self.boolean_flag=="-":
            out_str+=self.boolean_flag
        return out_str+" "+self.variable+"{"+str(self.valor)+"}"

class Creator:
    """
    Crea una serie de clausulas, en un principio, 10 variables, 5 claúsulas
    """
    def __init__(self, no_variables=10, no_clausulas=5):
        if no_variables%no_clausulas!=0:
            print("El número de variables debe ser divisible entre el número de
            claúsulas")
            self.no_variables=no_variables
            self.no_clausulas=no_clausulas
            self.clausulas=[]

    def create(self):
        conteo_clausulas=self.no_clausulas
        no_variables_per_clausula=int(self.no_variables/self.no_clausulas)
        while conteo_clausulas>0:
            
