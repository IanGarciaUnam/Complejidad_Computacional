import random
from collections import deque

class Vertice:
    """
    Esta implementación de la clase gráfica nos permitirá modelar
    los vértices de una gráfica, si la lista de vecinos es vacía
    significa que tenemos un vértice aislado, vecinos es una lista de vértices
    """
    def __init__(self,vertice:int,vecinos:list):
        self.vertice=vertice
        self.vecinos=vecinos

    def tiene_vecinos(self):
        """
        Devuelve true si la longitud lista de vecinos es mayor a 0
        """
        return len(self.vecinos)>0

    def get_peso(self):
        """
        Devuelve el peso del vértice
        """
        return len(self.vecinos)

    def get_vecinos(self):
        """
        Devuelve la lista de vecinos del vértice
        """
        return self.vecinos

    def get_value(self):
        """
        Devuelve el valor del vértice
        """
        return self.vertice

    def add_vecino(self, vecino):
        """
        Agrega un vecino:Vertice a la lista
        """
        if vecino in self.vecinos or vecino.get_value()==self.vertice:
            pass
        else:
            self.vecinos.append(vecino)

    def __eq__(self, other):
        if isinstance(other, Vertice):
            return self.vertice == other.vertice
        return False

    def __str__(self):
        vec_s="["
        for vec in self.vecinos:
            vec_s+=str(vec.vertice)+","
        vec_s+="]"
        return "{"+str(self.vertice)+","+vec_s+" }"

class Grafica:
    """
    Esta implementación de la clase gráfica nos permitirá modelarla
    la llave corresponde al vertice y el valor a su lista de vecinos,
    convierte la lista en un diccionario
    """
    def __init__(self,vertices_l:list):
        self.vertices_list=vertices_l
        self.vertices={}
        for v in vertices_l:
            self.vertices[v.get_value()]=tuple(v.get_vecinos())

    def get_graph_as_list(self):
        return self.vertices_list

    def get_graph(self):
        """
        Devuelve el diccionario utilizado para modelar la gráfica
        """
        return self.vertices

    def __str__(self):
        out_str="{"
        for key in self.vertices:
            out_str+="("+str(key)+",["
            for v in self.vertices[key]:
                out_str+=str(v.get_value())+","
            out_str+="]),"
        return out_str+"}"

class Generador_Grafica:
    """
    Genera un gráfica aleatoria con elementos entre el tamaño mínimo
    y el máximo
    """

    def __init__(self, min,max):
        """
        Generamos una gráfica inconexa de un tamaño entre el número
        mínimo y máximo indicado, genera conexiones aleatorias y finalmente
        crea un objeto tipo gráfica
        """
        self.numeros_usados=[]
        self.vertices_list=[]
        no_vertices=random.randint(min,max)
        for i in range(1,no_vertices):
            vertice_value=i
            v = Vertice(vertice_value,[])
            self.vertices_list.append(v)
            self.numeros_usados.append(vertice_value)
        #v_s=Vertice(s,[])
        #v_t=Vertice(t,[])
        #if v_s not in self.vertices_list:
            #self.vertices_list.append(v_s)
        #if v_t not in self.vertices_list:
            #self.vertices_list.append(v_t)
        #self.numeros_usados.append(s)
        #self.numeros_usados.append(t)
        self.generate_conexion()
        self.create_graph()



    def generate_conexion(self):
        """
        Genera conexiones aleatorias entre los vértices de una gráfica
        """
        for v in self.vertices_list:
            no_vecinos=random.randint(0,len(self.vertices_list))
            for i in range(no_vecinos):
                nvo_vecino=random.choice(self.vertices_list)
                if nvo_vecino in v.get_vecinos():
                    continue
                else:
                    v.add_vecino(nvo_vecino)
                    nvo_vecino.add_vecino(v)

    def get_graph_as_list(self):
        return self.vertices_list

    def create_graph(self):
        """
        Crea un objeto tipo gráfica
        """
        self.graph=Grafica(self.vertices_list)

    def get_graph(self):
        """
        Devuelve una gráfica, una vez que esta fue creada
        """
        return self.graph




class Covering_Set_Problem:

    def __init__(self, min, max):
        """
        Inicializa el enrutador para que este pueda crear una
        gráfica de min<=tamaño<=max, con s y t como vértices distinguidos,
        además guarda la ruta tomada por el algoritmo, obligatoriamente agrega
        los vértices distinguidos s,t
        """
        generador_grafica=Generador_Grafica(min,max)
        #self.s=s
        #self.t=t
        self.grafica=generador_grafica.get_graph()
        self.grafica_list=generador_grafica.get_graph_as_list()
        self.cubierta_generada=[]

    def signalizer(self,value):
        """
        Devuelve una referencia al objeto vértice que tiene el mismo valor que value
        None en caso de que no exista
        """
        print(self.grafica)
        for key in self.grafica.get_graph():
            if key.get_value()==value:
                return key
        return None

    def vertice_tiene_vecino(self, vertice:int):
        x=self.grafica.get_graph()[vertice]
        return len(x)>0

    def pick_random(self):
        """
        Toma un vértice al azar
        """
        return random.choice(list(self.grafica.get_graph()))



    def pick_maximal_vertex(self):
        """
        Toma el vértice maximal siempre que este no haya sido utilizado
        o sea vecino
        """
        flag_flux=True
        vertice=None
        max_weight=0
        for vertice_main in self.grafica_list:
            vecs=vertice_main.get_vecinos()
            #print(vertices_utilizados,vertice_main not in vertices_utilizados)
            if vertice == None and max_weight==0:
                vertice=vertice_main
                max_weight=len(vecs)
            elif max_weight<len(vecs) and not self.found_in_grafica_list(vertice_main):
                max_weight=len(vecs)
                vertice=vertice_main
        return vertice

    def found_in_grafica_list(self, vertice):
        for vex in self.cubierta_generada:
            if vertice == vex:
                return True
            else:
                for vec in vex.get_vecinos():
                    #print(vec==vertice, vec.get_value(),vertice.get_value())
                    if vec==vertice:
                        return True

        return False

    def greedy_set_cover(self):
        """
        Tomamos un vértice cuya familia de vértices correspondiente sea
        máxima, hasta que todos los vértices hayan sido seleccionados (como vértice
        principal o de las listas de vécinos), se devuelve la
        solución
        """
        vertices_origin=list(self.grafica.get_graph().keys())
        vertices_vecinos_usados=[]
        for v in self.grafica.get_graph_as_list():
            print(v)
        print("=====================================")
        while len(self.grafica_list)>0:
            #print(self.grafica_list)
            v_max=self.pick_maximal_vertex()
            #vertices_vecinos_usados.append(v_max)
            self.cubierta_generada.append(v_max)
            for vec in v_max.get_vecinos():
                if vec in self.grafica_list:
                    self.grafica_list.remove(vec)
            self.grafica_list.remove(v_max)

        return self.cubierta_generada

    def print_cover_set(self):
        self.greedy_set_cover()
        for v in self.cubierta_generada:
            #print(isinstance(v, Vertice))
            print(str(v))









r = Covering_Set_Problem(10,20)
#print(isinstance(r.greedy_set_cover(), Vertice))
r.print_cover_set()
