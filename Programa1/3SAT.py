import random
#from collections import sort
import string
class Clausula:
    """
    Esta clase nos permite modelar las Clausulas correspondientes, así
    como obtener su valor de verdad
    """
    def __init__(self, variables, flag_bool="+"):
        self.variables=variables
        self.flag_bool:str=flag_bool

    def get_variables(self):
        """
        Devuelve la lista de variables
        """
        return self.variables

    def __eq__(self, other):
        if not isinstance(other, Clausula):
            return False
        self.variables.sort()
        other.variables.sort()
        return self.variables == other.variables and self.flag_bool==other.flag_bool

    def agrega_variable(self, variable):
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
        for var in self.variables:
            out_str+=" "+str(var)+ "V"
        out_str=")"
        return f'{out_str}'

    def __repr__(self):
        return f'{self.flag_bool}{self.variables}'



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

    def get_variable(self)->str:
        return self.variable

    def get_valor_booleano(self):
        """
        Devuelve el valor booleano de la variable
        """
        if self.boolean_flag=="-":
            return not self.valor
        return self.valor

    def __eq__(self,other):
        if not isinstance(other,Variable):
            return False
        return self.variable==other.variable

    def __str__(self):
        out_str=""
        if self.boolean_flag=="-":
            out_str+=self.boolean_flag
        return f'{out_str}{self.variable}({self.valor})'
    def __repr__(self):
        out_str=""
        if self.boolean_flag=="-":
            out_str+=self.boolean_flag
        return f'{out_str}{self.variable}({self.get_valor_booleano()})'

class Creator:
    """
    Crea una serie de clausulas, en un principio, 10 variables, 5 claúsulas
    """
    def __init__(self, no_variables=10, no_clausulas=5):
        if no_variables%no_clausulas!=0:
            print("El número de variables debe ser divisible entre el número de claúsulas")
            return
        self.no_variables=no_variables
        self.no_clausulas=no_clausulas
        self.clausulas=[]
        self.letters = string.ascii_lowercase
        self.rand_letters = random.choices(self.letters,k=self.no_variables)
        self.variables_global=[]
        self.create()
        self.complete_to_3()
    def create(self):
        """
        Crea la serie de claúsulas bajo los parámetro y no. de variables
        """
        conteo_clausulas=self.no_clausulas
        no_variables_per_clausula=int(self.no_variables/self.no_clausulas)
        while conteo_clausulas>0:
            conteo_clausulas-=1
            self.clausulas.append(Clausula(self.variables_generator(no_variables_per_clausula), "+"))
        return self.clausulas

    def variables_generator(self, no_variables_per_clausula):
        """
        Devuelve una lista con variables, evita tautologías como
        (p V p), (p V ¬p), etc
        """
        caracteres_tomados=[]
        caracter=random.choices(self.rand_letters)[0]
        variables_list=[]
        while no_variables_per_clausula>0:
            while caracter[0] in caracteres_tomados:
                caracter=random.choices(self.rand_letters)[0]
            caracteres_tomados.append(caracter[0])
            #print("Caracteres_tomados", caracter, caracteres_tomados)
            v =Variable(caracter, random.choice([True, False]), random.choice(["+","-"][0]))
            #print(v, self.variables_global)
            if  v not in self.variables_global and v not in variables_list:
                variables_list.append(v)
                self.variables_global.append(v)
            else:
                variables_list.append(Variable(caracter, self.get_variable(v).get_valor_booleano(), random.choice(["+","-"])))
            no_variables_per_clausula-=1
        return variables_list

    def get_variable(self, v:Variable):
        for var in self.variables_global:
            if var==v:
                return var
        return None


    def complete_to_3(self):
        if self.clausulas==[]:
            print("NOT DEFINED YET")
            return
        if len(self.clausulas[0].get_variables())%3==0:
            return self.clausulas
        if len(self.clausulas[0].get_variables())<=2:
            num_boolean_flag=random.choice([0,1])
            boolean_value=random.choice([False, True])
            caracter=random.choices(self.letters)[0]
            while caracter in self.rand_letters:
                caracter=random.choices(self.letters)[0]
            for clausula in self.clausulas:
                if num_boolean_flag==1:
                    clausula.agrega_variable(Variable(caracter, boolean_value, "-"))
                else:
                    clausula.agrega_variable(Variable(caracter, boolean_value, "+"))
            return self.complete_to_3()
        else:
            print("El número de variables por claúsula es mayor o igual a 4")
            return

    def evaluates(self):
        """
        Realiza la evaluación por cada clausula para obtener el valor de verdad de
        la proposición
        """
        print("Ejemplar", str(self.clausulas))
        result=True
        fst_time=False
        for clausula in self.clausulas:
            if fst_time:
                fst_time!=fst_time
                result=clausula.get_valor_booleano()
            else:
                result&=clausula.get_valor_booleano()
        print("Respuesta: ",result)
        return result

c = Creator(10, 5)
c.evaluates()
