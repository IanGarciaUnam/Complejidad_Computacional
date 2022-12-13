import random
from collections import deque
import time
class Vertice:
    """
    Esta implementación de la clase gráfica nos permitirá modelar
    los vértices de una gráfica, si la lista de vecinos es vacía
    significa que tenemos un vértice aislado, vecinos es una lista de vértices,
    asismo
    """
    def __init__(self,vertice:int,vecinos:list):
        self.vertice=vertice
        self.vecinos=vecinos
        self.vecinos_dict={}

    def tiene_vecinos(self):
        """
        Devuelve true si la longitud lista de vecinos es mayor a 0
        """
        return len(self.vecinos)>0

    def get_peso(self):
        """
        Devuelve el peso del vértice
        """
        return self.weight

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

    def add_vecino(self, vecino, peso):
        """
        Agrega un vecino:Vertice a la lista
        """
        if vecino in self.vecinos or vecino.get_value()==self.vertice:
            pass
        else:
            self.vecinos.append(vecino)
            self.vecinos_dict[vecino.get_value()]=tuple((vecino,peso))

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
    como una lista de vértices
    """
    def __init__(self,vertices_l:list):
        self.vertices_list=vertices_l

    def get_graph_as_list(self):
        return self.vertices_list

    def get_graph(self):
        """
        Devuelve el diccionario utilizado para modelar la gráfica
        """
        return self.vertices_list

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
        self.generate_conexion()
        self.create_graph()



    def generate_conexion(self):
        """
        Genera conexiones aleatorias entre los vértices de una gráfica,
        aseguramos que es conexa, y asignamos peso entre aristas
        """
        for v in self.vertices_list:
            no_vecinos=random.randint(0,len(self.vertices_list))
            k=random.randint(0, 100)#peso de la arista
            for i in range(no_vecinos):
                nvo_vecino=random.choice(self.vertices_list)
                if nvo_vecino in v.get_vecinos():
                    continue
                else:
                    v.add_vecino(nvo_vecino,k)
                    nvo_vecino.add_vecino(v,k)

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




class Tree_Min_Span:

    def __init__(self, min, max,k):
        """
        Inicializa la gráfica entre 10 y 20 vértices, define el valor para k
        """
        generador_grafica=Generador_Grafica(min,max)
        self.peso_maximo_esperado=k
        self.peso_maximo=k
        self.grafica=generador_grafica.get_graph()
        self.grafica_list=generador_grafica.get_graph_as_list()
        self.tree_gen_vertices=[]
        self.tree_gen_aristas=[]

    def genera_arbol(self):
        vertice_alfa=random.choice(self.grafica_list)
        self.tree_gen_vertices.append(vertice_alfa)
        #for v in self.grafica_list:
        #    print(str(v))
        peso_logrado=self.genera_arbol_rec(vertice_alfa, False)
        vertices,vertices_graf="",""
        for v in self.tree_gen_vertices:
            vertices+=str(v)
        for v in self.grafica_list:
            vertices_graf+=str(v)+",\n"
        print("Gráfica:", "[",vertices_graf,"]")
        print("Vertices del árbol:\n","[",vertices,"]")
        print("Ejemplar creado:\n", self.tree_gen_aristas)
        print("Peso mínimo esperado: ", self.peso_maximo_esperado,"|","Peso mínimo logrado: ",self.peso_maximo_esperado-self.peso_maximo)
        return peso_logrado

    def genera_arbol_rec(self, vertice, flag_2nd_case):
        #for v in self.tree_gen_vertices:
        #    print(str(v))
        if len(self.tree_gen_vertices)==len(self.grafica_list) or self.peso_maximo<0:
            return self.peso_maximo>=0
        ver_nuevo,peso=self.choose_min_vert(vertice)
        if not self.esta_en_arbol(ver_nuevo):#El vertice no esta en el arbol generado, evitamos crear ciclos, buscando el de menor peso
            self.peso_maximo-=peso
            self.tree_gen_vertices.append(ver_nuevo)
            self.tree_gen_aristas.append((vertice.get_value(),ver_nuevo.get_value(), "p["+str(peso)+"]"))
            return self.genera_arbol_rec(ver_nuevo,False)#Paso recursivo
        elif len(self.tree_gen_vertices)>1 and  not flag_2nd_case:#El vertice anterior si estaba, seleccionamos otro vertice de movimiento
            while True:
                ver =  random.choice(self.tree_gen_vertices)
                if ver != vertice:
                    return self.genera_arbol_rec(ver,True)
        else:#Seleccionamos alguno de sus vecinos al azar sin importar su peso
            while True:
                vecino=random.choice(vertice.get_vecinos())
                ver_nuevo,peso=vertice.get_vecinos_dict()[vecino.get_value()]
                if vecino not in self.tree_gen_vertices:
                    self.peso_maximo-=peso
                    self.tree_gen_vertices.append(ver_nuevo)
                    self.tree_gen_aristas.append((vertice.get_value(),ver_nuevo.get_value(), "p["+str(peso)+"]"))
                    return self.genera_arbol_rec(ver_nuevo, False)
                elif len(self.tree_gen_vertices)==1:
                    self.tree_gen_vertices.clear()
                    self.tree_gen_aristas.clear()
                    return self.genera_arbol_rec(vecino,False)
                break
            return self.genera_arbol_rec(vertice, False)



    def esta_en_arbol(self, vertice_nvo):
        """
        si el vertice ya esta en la lista de vertices del tree_gen_vertices
        devolvemos true
        """
        return vertice_nvo in self.tree_gen_vertices


    def choose_min_vert(self, vertice):
        """
        Escoge el vertice cuya arista sea de menor peso
        """
        k=100000
        vertice_chosen=None
        for vecino in vertice.get_vecinos_dict():
            vec,peso=vertice.get_vecinos_dict()[vecino]
            if peso<k:
                k=peso
                vertice_chosen=vec
        return vertice_chosen,k



tree_min_span=Tree_Min_Span(10,20,500)
start = time.time()
x=tree_min_span.genera_arbol()
if x:
    print("YES")
else:
    print("NO")
end = time.time()
print("Time:",end - start)






"""
r =Tree_Min_Span(10,20)
start = time.time()
r.print_cover_set()
end = time.time()
print("Time:",end - start)
print("Complejidad O(n^{3})")
"""
