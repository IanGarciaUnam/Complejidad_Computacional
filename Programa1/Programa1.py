import random
from collections import deque

class Vertice:
    """
    Esta implementación de la clase gráfica nos permitirá modelar
    los vértices de una gráfica, si la lista de vecinos es vacía
    significa que tenemos un vértice aislado, vecinos es una lista de vértices
    """
    self.vecinos=[]
    def __init__(self,vertice,vecinos):
        self.vertice=vertice
        self.vecinos=vecinos

    def tiene_vecinos(self):
        """
        Devuelve true si la longitud lista de vecinos es mayor a 0
        """
        return len(self.vecinos)>0

    def get_vecinos(self):
        """
        Devuelve la lista de vecinos del vértice
        """
        return self.vecinos

    def get_value(self):
        """
        Devuelve el valor del vértice
        """
        return vertice

    def add_vecino(self, vecino):
        """
        Agrega un vecino:Vertice a la lista
        """
        vecinos.add(vecino)

    def __eq__(self, other):
        if isinstance(other, Vertice):
            return self.vertice == other.vertice
        return False

    def __str__(self):
        vec_s="["
        for vec in vecinos:
            vec_s+=str(vec.get_value())+","
        vec_s+="]"
        return "{"+str(vertice)+","+vec_s+" }"

class Grafica:
    """
    Esta implementación de la clase gráfica nos permitirá modelarla
    la llave corresponde al vertice y el valor a su lista de vecinos,
    convierte la lista en un diccionario
    """
    self.vertices={}
    def __init__(self,vertices:list):
        for v in vertices:
            self.vertices[v]=v.get_vecinos()

    def __str__(self):
        out_str=""
        for key in vertices:
            out_str+=key+" : "+vertices[key])
        return out_str

class Generador_Grafica:
    """
    Genera un gráfica aleatoria con elementos entre el tamaño mínimo
    y el máximo
    """
    self.numeros_usados=[]
    self.vertices_list=[]
    def __init__(self, min,max):
        """
        Generamos una gráfica inconexa de un tamaño entre el número
        mínimo y máximo indicado, genera conexiones aleatorias y finalmente
        crea un objeto tipo gráfica
        """
        no_vertices=random.rand_int(min,max)
        for i in range(1,no_vertices):
            vertice_value=0
            while vertice_value in numeros_usados:
                vertice_value=random.rand_int(1,no_vertices)
            v = Vertice(vertice_value,[])
            numeros_usados.add(vertice_value)
            self.generate_conexion()
            self.create_graph()

    def generate_conexion(self):
        """
        Genera conexiones aleatorias entre los vértices de una gráfica
        """
        for v in self.vertices_list:
            no_vecinos=random.rand_int(0,len(vertices_list))
            for i in range(no_vecinos):
                nvo_vecino=random.choice(self.vertices_list)
                if nvo_vecino in v.get_vecinos():
                    continue
                else:
                    v.add_vecino(nvo_vecino)
                    nvo_vecino.add_vecino(v)

    def create_graph(self):
        """
        Crea un objeto tipo gráfica
        """
        self.graph=Grafica(vertices_list)

    def get_graph(self):
        """
        Devuelve una gráfica, una vez que esta fue creada
        """
        return self.graph




class Router:

    def __init__(self, min, max, s,t):
        """
        Inicializa el enrutador para que este pueda crear una
        gráfica de min<=tamaño<=max, con s y t como vértices distinguidos,
        además guarda la ruta tomada por el algoritmo
        """
        generador_grafica=Generador_Grafica(min,max)
        self.s=s
        self.t=t
        self.grafica=generador_grafica.get_graph()
        self.ruta=deque()

    def signalizer(self,value):
        """
        Devuelve una referencia al objeto vértice que tiene el mismo valor que value
        None en caso de que no exista
        """
        for key in self.grafica:
            if key.get_value()==value:
                return key
        return None

    def movilizer(self):
        """
        Recorre la gráfica desde el punto s, en búsqueda del punto t sin repetir
        vértices, devuelve verdadero si lo logra y falso en caso contrario, además
        salva la ruta tomada
        """
        S_vertice=self.signalizer(self.s)
        T_vertice=self.signalizer(self.t)
        self.ruta.append(S_vertice)
        V=S_vertice
        while V.tiene_vecinos() or V != T_vertice:
            while V in self.ruta:
                V=random.choice(self.grafica[V])
            self.ruta.append(V)
        print(ruta)
        return T_vertice==self.ruta.peek()
r = Router(10,20, 1,9)
print(r.movilizer())
