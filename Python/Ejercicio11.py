import sqlite3

class Base():
  def main(self):
    print("--------MENU--------")
    print("1. Crear base de datos")
    print("2. Ingresar datos")
    print("3. Buscar nombre de persona en base de datos")
    print("4. Imprimir base de datos")
    print()
    Value= None
    while Value != 0:
      Value = int(input("Ingrese el numero de la operacion deseada: "))
      if Value == 1:
        self.create()
      elif Value == 2:
        self.add()
      elif Value == 3:
        self.search()
      elif Value == 4:
        self.printer()
      else:
        print("El número ingresado no es válido")
      break

  def create(self):
    conn = sqlite3.connect('Mibase.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Alumnos(Id INT,Nombre TEXT,Apellido TEXT)")
    cursor.close
    conn.close()

  def add(self):
    conn = sqlite3.connect('Mibase.db', isolation_level= None)
    cursor = conn.cursor()
    id = str(input("Ingrese el ID de registro: "))
    nombre = str(input("Ingrese el nombre de registro: ")).title()
    apellido = str(input("Ingrese el apellido de registro: ")).title()      
    dat = '''INSERT INTO Alumnos(Id, Nombre, Apellido) VALUES(?,?,?)'''
    cursor.execute(dat,(id,nombre,apellido))
    conn.commit()
    cursor.close
    conn.close()

  def search(self):
    conn = sqlite3.connect('Mibase.db',isolation_level = None)
    cursor = conn.cursor()
    nombreb = str(input("Ingrese el nombre de la persona a buscar: ")).title()
    rows = cursor.execute(f'SELECT * FROM Alumnos WHERE Nombre = "{nombreb}"')
    for row in rows:
      print(row)
    cursor.close
    conn.close()

  def printer(self):
    conn = sqlite3.connect('Mibase.db')
    cursor = conn.cursor()
    rows = cursor.execute('SELECT * FROM Alumnos')
    for row in rows:
      print(row)
    cursor.close
    conn.close()

bd= Base()
bd.main()
