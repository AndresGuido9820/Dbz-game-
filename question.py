import pygame

class QuizManager:
    
    def __init__(self):
        self.level_questions = {
            1: [
                {"question": "¿Qué significa Python?", "options": ["Un reptil", "Un lenguaje de programación", "Una herramienta de diseño", "Un software de edición"], "answer": "Un lenguaje de programación"},
                {"question": "¿Cuál es el operador para la suma en Python?", "options": ["+", "-", "*", "/"], "answer": "+"},
                {"question": "¿Cómo se crea una lista en Python?", "options": ["[]", "{}", "()", "<>"], "answer": "[]"},
                {"question": "¿Qué palabra clave se usa para definir una función?", "options": ["def", "function", "func", "define"], "answer": "def"},
                {"question": "¿Cómo se crea un comentario en Python?", "options": ["// comentario", "# comentario", "/* comentario */", "<!-- comentario -->"], "answer": "# comentario"},
                {"question": "¿Cuál de las siguientes opciones es un tipo de dato en Python?", "options": ["integer", "str", "booleano", "number"], "answer": "str"},
                {"question": "¿Qué hace el método 'append()' en una lista?", "options": ["Elimina un elemento", "Añade un elemento al final", "Ordena la lista", "Convierte la lista en un conjunto"], "answer": "Añade un elemento al final"},
                {"question": "¿Cómo se llama el proceso de transformar un string en un entero?", "options": ["int() a str()", "str() a int()", "int() a char()", "float() a int()"], "answer": "str() a int()"},
                {"question": "¿Cómo puedes importar una librería en Python?", "options": ["import nombre", "include nombre", "use nombre", "require nombre"], "answer": "import nombre"},
                {"question": "¿Cómo puedes importar una librería en Python?", "options": ["import nombre", "include nombre", "use nombre", "require nombre"], "answer": "import nombre"},
                
            ],
            2: [
                {"question": "¿Cómo se define un diccionario en Python?", "options": ["{}", "[]", "()", "<>"], "answer": "{}"},
                {"question": "¿Qué hace el operador '==' en Python?", "options": ["Suma", "Multiplica", "Compara si son iguales", "Divide"], "answer": "Compara si son iguales"},
                {"question": "¿Cómo accedes al valor de una clave en un diccionario?", "options": ["diccionario[clave]", "diccionario{clave}", "diccionario.key(clave)", "diccionario.get(clave)"], "answer": "diccionario[clave]"},
                {"question": "¿Qué significa 'break' en un ciclo?", "options": ["Continúa el ciclo", "Detiene el ciclo", "Reinicia el ciclo", "Suma 1 a cada elemento"], "answer": "Detiene el ciclo"},
                {"question": "¿Cuál es el tipo de dato de 'None' en Python?", "options": ["int", "str", "float", "NoneType"], "answer": "NoneType"},
                {"question": "¿Cómo puedes crear un ciclo for que recorra una lista?", "options": ["for i in range(lista)", "for i in lista", "for range(i, lista)", "for i in len(lista)"], "answer": "for i in lista"},
                {"question": "¿Cómo se hace un condicional if en Python?", "options": ["if x == 10:", "if 10 = x:", "if x : 10", "if 10 == x:"], "answer": "if x == 10:"},
                {"question": "¿Cuál es el uso de la función 'len()'?", "options": ["Cuenta los elementos de una lista", "Convierte una lista en un diccionario", "Cuenta las palabras en una cadena", "Crea una lista nueva"], "answer": "Cuenta los elementos de una lista"},
                {"question": "¿Qué función convierte un valor en una cadena de texto?", "options": ["str()", "int()", "float()", "list()"], "answer": "str()"},
                {"question": "¿Qué hace la función 'input()' en Python?", "options": ["Obtiene datos de la consola", "Muestra un mensaje", "Recibe un valor de una lista", "Imprime en pantalla"], "answer": "Obtiene datos de la consola"}
            ],
            3: [
                {"question": "¿Qué es una tupla en Python?", "options": ["Una lista ordenada e inmutable", "Una lista desordenada", "Un diccionario", "Un tipo de función"], "answer": "Una lista ordenada e inmutable"},
                {"question": "¿Cuál es la sintaxis correcta para un ciclo while?", "options": ["while condición:", "while: condición", "while (condición):", "while condición {}"], "answer": "while condición:"},
                {"question": "¿Cómo puedes agregar un elemento al principio de una lista?", "options": ["insert(0, elemento)", "append(0, elemento)", "add(0, elemento)", "push(0, elemento)"], "answer": "insert(0, elemento)"},
                {"question": "¿Cómo puedes convertir una cadena en una lista?", "options": ["split()", "join()", "toList()", "convert()"], "answer": "split()"},
                {"question": "¿Qué hace la función 'map()' en Python?", "options": ["Aplica una función a cada elemento de un iterable", "Crea una lista", "Ordena un diccionario", "Convierte un valor en cadena"], "answer": "Aplica una función a cada elemento de un iterable"},
                {"question": "¿Qué se necesita para abrir un archivo en Python?", "options": ["open()", "read()", "file()", "load()"], "answer": "open()"},
                {"question": "¿Qué hace la función 'filter()'?", "options": ["Filtra elementos de un iterable", "Convierte una lista a tupla", "Crea un diccionario", "Cuenta los elementos de una lista"], "answer": "Filtra elementos de un iterable"},
                {"question": "¿Qué significa 'lambda' en Python?", "options": ["Una función anónima", "Una clase", "Una variable", "Un método"], "answer": "Una función anónima"},
                {"question": "¿Cómo se puede ordenar una lista en Python?", "options": ["sort()", "order()", "arrange()", "sequence()"], "answer": "sort()"},
                {"question": "¿Qué hace la función 'zip()'?", "options": ["Agrupa dos listas en un solo iterable", "Desempaqueta una lista", "Crea una lista de tuplas", "Convierte un diccionario en lista"], "answer": "Agrupa dos listas en un solo iterable"}
            ],
            4: [
                {"question": "¿Cómo se maneja una excepción en Python?", "options": ["try-except", "catch-finally", "if-else", "throw-catch"], "answer": "try-except"},
                {"question": "¿Cómo se puede hacer una función que reciba un número variable de parámetros?", "options": ["*args", "*kwargs", "args()", "**args"], "answer": "*args"},
                {"question": "¿Qué hace la función 'join()'?", "options": ["Une elementos de una lista en una cadena", "Convierte una lista en un conjunto", "Elimina elementos de una lista", "Cuenta los caracteres de una cadena"], "answer": "Une elementos de una lista en una cadena"},
                {"question": "¿Qué es un módulo en Python?", "options": ["Un archivo que contiene código Python", "Un tipo de variable", "Una función incorporada", "Una lista de objetos"], "answer": "Un archivo que contiene código Python"},
                {"question": "¿Qué palabra clave se usa para crear una clase?", "options": ["class", "def", "module", "object"], "answer": "class"},
                {"question": "¿Qué hace la palabra clave 'self' en Python?", "options": ["Se refiere a la instancia actual de la clase", "Define una función", "Llama a un método de la clase", "Crea una variable"], "answer": "Se refiere a la instancia actual de la clase"},
                {"question": "¿Qué es un decorador en Python?", "options": ["Una función que modifica el comportamiento de otra función", "Una clase que hereda de otra", "Un tipo de bucle", "Un tipo de excepción"], "answer": "Una función que modifica el comportamiento de otra función"},
                {"question": "¿Qué es un generador en Python?", "options": ["Una función que usa 'yield' para retornar valores", "Un tipo de objeto", "Un archivo de datos", "Una lista de elementos"], "answer": "Una función que usa 'yield' para retornar valores"},
                {"question": "¿Cómo se usa 'os' en Python?", "options": ["Para interactuar con el sistema operativo", "Para gestionar errores", "Para hacer operaciones matemáticas", "Para leer archivos CSV"], "answer": "Para interactuar con el sistema operativo"},
                {"question": "¿Qué hace la función 'open()' en modo 'r'?", "options": ["Lee un archivo", "Escribe en un archivo", "Abre un archivo para lectura", "Abre un archivo para escritura"], "answer": "Abre un archivo para lectura"}
            ],
            5: [
                {"question": "¿Qué es una función recursiva?", "options": ["Una función que se llama a sí misma", "Una función que se define fuera de una clase", "Una función que se ejecuta en paralelo", "Una función que recibe parámetros variables"], "answer": "Una función que se llama a sí misma"},
                {"question": "¿Qué hace 'yield' en Python?", "options": ["Devuelve un valor de forma paulatina en una función generadora", "Indica un valor por defecto", "Finaliza un ciclo", "Detiene la ejecución de un programa"], "answer": "Devuelve un valor de forma paulatina en una función generadora"},
                {"question": "¿Cuál es el propósito de 'super()' en Python?", "options": ["Llamar a métodos de la clase base", "Crear una nueva clase", "Definir una función", "Actualizar el valor de una variable"], "answer": "Llamar a métodos de la clase base"},
                {"question": "¿Qué significa un 'type hint' en Python?", "options": ["Especificar el tipo de un parámetro o retorno", "Crear una nueva variable", "Generar un tipo de excepción", "Indicar un comentario"], "answer": "Especificar el tipo de un parámetro o retorno"},
                {"question": "¿Cómo puedes realizar una búsqueda binaria en una lista ordenada?", "options": ["Usando un ciclo for", "Usando el método 'find'", "Usando 'bisect'", "Usando 'search'"], "answer": "Usando 'bisect'"},
                {"question": "¿Qué es 'pickle' en Python?", "options": ["Un módulo para serializar objetos", "Un tipo de archivo", "Una función de impresión", "Una clase para manejar excepciones"], "answer": "Un módulo para serializar objetos"},
                {"question": "¿Cómo puedes verificar el tipo de una variable?", "options": ["type()", "isinstance()", "getType()", "varType()"], "answer": "type()"},
                {"question": "¿Qué es una excepción 'IndexError'?", "options": ["Acceder a un índice fuera de los límites de una lista", "Acceder a un archivo que no existe", "Usar una variable no definida", "Intentar dividir entre cero"], "answer": "Acceder a un índice fuera de los límites de una lista"},
                {"question": "¿Qué hace la función 'sorted()'?", "options": ["Devuelve una lista ordenada", "Ordena la lista original", "Reversa una lista", "Elimina elementos duplicados"], "answer": "Devuelve una lista ordenada"},
                {"question": "¿Qué hace 'str.format()' en Python?", "options": ["Reemplaza partes de una cadena con valores", "Convierte un número a cadena", "Añade texto al final de una cadena", "Elimina espacios en blanco"], "answer": "Reemplaza partes de una cadena con valores"}
            ],
            6: [
                {"question": "¿Qué es el concepto de 'desempaquetado' en Python?", "options": ["Extraer elementos de una lista o tupla", "Asignar un valor a varias variables", "Añadir elementos a una lista", "Crear una nueva tupla"], "answer": "Extraer elementos de una lista o tupla"},
                {"question": "¿Qué hace la función 'enumerate()'?", "options": ["Devuelve los índices y valores de una lista", "Ordena una lista", "Convierte una lista a conjunto", "Elimina los elementos duplicados"], "answer": "Devuelve los índices y valores de una lista"},
                {"question": "¿Qué es una función lambda?", "options": ["Una función anónima y de una sola línea", "Una función que toma múltiples argumentos", "Una función recursiva", "Una función con nombre"], "answer": "Una función anónima y de una sola línea"},
                {"question": "¿Cómo se puede acceder a la clase base desde una clase hija?", "options": ["super()", "base()", "parent()", "class()"], "answer": "super()"},
                {"question": "¿Qué es 'itertools'?", "options": ["Un módulo para crear iteradores", "Una función para trabajar con listas", "Una herramienta para manejar diccionarios", "Una función para trabajar con cadenas"], "answer": "Un módulo para crear iteradores"},
                {"question": "¿Qué hace 'assert' en Python?", "options": ["Comprueba que una condición sea verdadera", "Lanza una excepción", "Crea una nueva variable", "Termina la ejecución de un ciclo"], "answer": "Comprueba que una condición sea verdadera"},
                {"question": "¿Qué es un generador en Python?", "options": ["Una función que devuelve valores uno a uno", "Una variable de tipo especial", "Un tipo de excepción", "Una función que genera cadenas"], "answer": "Una función que devuelve valores uno a uno"},
                {"question": "¿Qué es la 'memoria caché' en Python?", "options": ["Un espacio temporal donde se guardan datos para ser accesibles más rápidamente", "Una estructura de datos", "Una función", "Un tipo de archivo"], "answer": "Un espacio temporal donde se guardan datos para ser accesibles más rápidamente"},
                {"question": "¿Qué hace 'filter()' en Python?", "options": ["Filtra elementos de una lista", "Ordena una lista", "Genera un diccionario", "Convierte una lista a tupla"], "answer": "Filtra elementos de una lista"},
                {"question": "¿Qué es un conjunto en Python?", "options": ["Una colección de elementos únicos", "Una lista con elementos repetidos", "Un tipo de diccionario", "Una lista ordenada"], "answer": "Una colección de elementos únicos"}
            ],
            7: [
                {"question": "¿Qué es el concepto de 'desempaquetado' en Python?", "options": ["Extraer elementos de una lista o tupla", "Asignar un valor a varias variables", "Añadir elementos a una lista", "Crear una nueva tupla"], "answer": "Extraer elementos de una lista o tupla"},
                {"question": "¿Qué hace la función 'enumerate()'?", "options": ["Devuelve los índices y valores de una lista", "Ordena una lista", "Convierte una lista a conjunto", "Elimina los elementos duplicados"], "answer": "Devuelve los índices y valores de una lista"},
                {"question": "¿Qué es una función lambda?", "options": ["Una función anónima y de una sola línea", "Una función que toma múltiples argumentos", "Una función recursiva", "Una función con nombre"], "answer": "Una función anónima y de una sola línea"},
                {"question": "¿Cómo se puede acceder a la clase base desde una clase hija?", "options": ["super()", "base()", "parent()", "class()"], "answer": "super()"},
                {"question": "¿Qué es 'itertools'?", "options": ["Un módulo para crear iteradores", "Una función para trabajar con listas", "Una herramienta para manejar diccionarios", "Una función para trabajar con cadenas"], "answer": "Un módulo para crear iteradores"},
                {"question": "¿Qué hace 'assert' en Python?", "options": ["Comprueba que una condición sea verdadera", "Lanza una excepción", "Crea una nueva variable", "Termina la ejecución de un ciclo"], "answer": "Comprueba que una condición sea verdadera"},
                {"question": "¿Qué es un generador en Python?", "options": ["Una función que devuelve valores uno a uno", "Una variable de tipo especial", "Un tipo de excepción", "Una función que genera cadenas"], "answer": "Una función que devuelve valores uno a uno"},
                {"question": "¿Qué es la 'memoria caché' en Python?", "options": ["Un espacio temporal donde se guardan datos para ser accesibles más rápidamente", "Una estructura de datos", "Una función", "Un tipo de archivo"], "answer": "Un espacio temporal donde se guardan datos para ser accesibles más rápidamente"},
                {"question": "¿Qué hace 'filter()' en Python?", "options": ["Filtra elementos de una lista", "Ordena una lista", "Genera un diccionario", "Convierte una lista a tupla"], "answer": "Filtra elementos de una lista"},
                {"question": "¿Qué es un conjunto en Python?", "options": ["Una colección de elementos únicos", "Una lista con elementos repetidos", "Un tipo de diccionario", "Una lista ordenada"], "answer": "Una colección de elementos únicos"}
            ]
        }
        self.current_question_index = 0
        self.correct_answers = 0
        self.current_level = 1
        self.wrong_answer=0

    def get_question(self):
        level_questions = self.level_questions[self.current_level]
        return level_questions[self.current_question_index]
    def get_level(self):
        return self.current_level

    def check_answer(self, answer):
        level_questions = self.level_questions[self.current_level]
        correct_answer = level_questions[self.current_question_index]["answer"]
        is_correct = (answer == correct_answer)
        if is_correct:
            self.correct_answers += 1
        
        else:
            self.wrong_answer+=1
        self.current_question_index += 1
        
        if self.correct_answers >= 7 and not self.has_more_questions():
            self.advance_level()
        return is_correct

    def has_more_questions(self):
        return self.current_question_index < len(self.level_questions[self.current_level])
    def game_over(self):
        if self.wrong_answer>3:
            return True
        return False

    def advance_level(self):
        if self.current_level <= 7:
            self.current_level += 1
            self.current_question_index = 0
            self.correct_answers = 0
        else:
            print("¡Has completado todos los niveles!")
   

    def level_completed(self):
        """ Método para verificar si el nivel ha sido completado. """
        if self.correct_answers >= 7 and not self.has_more_questions():
            return True
        return False

    def reset(self):
        self.current_level = 1
        self.current_question_index = 0
        self.correct_answers = 0

