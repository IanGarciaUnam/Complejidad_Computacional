import random
from collections import deque
import time
class Vertice:
    """
    Esta implementación de la clase gráfica nos permitirá modelar
    los vértices de una gráfica, si la lista de vecinos es vacía
    significa que tenemos un vértice aislado, vecinos es una lista de vértices
    """
    def __init__(self,vertice:int,vecinos:list):
        self.vertice=vertice
        self.vecinos=vecinos
        self.color=None
        self.vecinos_dict={}

    def set_color(self,color):
        self.color=color

    def get_color(self):
        return self.color

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

    def get_vecinos_dict(self):
        """
        Devuele el diccionario referente a los
        vecinos
        """
        return self.vecinos_dict

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
            self.vecinos_dict[vecino.get_value()]=vecino.get_value()

    def __eq__(self, other):
        if isinstance(other, Vertice):
            return self.vertice == other.vertice
        return False

    def __str__(self):
        vec_s="["
        for vec in self.vecinos:
            vec_s+=str(vec.vertice)+","
        vec_s+="]-"+"color:"+str(self.color)
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




class Graph_Coloration:

    def __init__(self, min, max, colores):
        """
        Crea la gráfica y para esta implementación los colores serán
        asignados como números
        """
        generador_grafica=Generador_Grafica(min,max)
        self.colores=[]
        self.grafica=generador_grafica.get_graph()
        self.grafica_list=generador_grafica.get_graph_as_list()
        for i in range(1,colores+1):
            self.colores.append(i)

    def vertice_tiene_vecino(self, vertice:int):
        x=self.grafica.get_graph()[vertice]
        return len(x)>0

    def pick_random(self):
        """
        Toma un vértice al azar
        """
        return random.choice(list(self.grafica.get_graph()))

    def execute(self):
        self.guess_phase()
        #self.print_grafica()
        print(self.verify_phase())

    def guess_phase(self):
        """
        Realiza un recorrido bfs sobre los vértices y
        asigna un color al azar
        """
        v=random.choice(self.grafica_list)
        visitados=[]
        cola=[]
        cola.append(v)
        while len(visitados)<len(self.grafica_list):
            v=cola.pop()
            #print(v)
            v.set_color(random.choice(self.colores))
            visitados.append(v)
            v=random.choice(v.get_vecinos())
            #self.print_grafica()
            #print(len(cola),len(visitados))
            if len(visitados)==len(self.grafica_list):
                break
            while v in visitados:
                v=random.choice(v.get_vecinos())
            cola.append(v)

    def print_grafica(self):
        for v in self.grafica_list:
            print(str(v))

    def verify_phase(self):
        for v in self.grafica_list:
            for vec in v.get_vecinos():
                if v.get_color()==vec.get_color():
                    return "NO"
        return "YES"


    def print_cover_set(self):
        print("{")
        for v in self.grafica_list:
            print(str(v))
        print("}")







g=Graph_Coloration(10,20,20)

start = time.time()
g.execute()
g.print_cover_set()
end = time.time()
print("Time:",end - start)
