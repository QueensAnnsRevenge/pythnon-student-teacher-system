import mysql.connector
from mysql.connector import Error
import classes as clss



def connection_open():
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='root',
                                         password='dusan')
    if connection.is_connected():
        cursor = connection.cursor()
        return [cursor, connection ]

def connection_close(cursor, connection):
    if connection.is_connected():
        cursor.close()
        connection.close()


def unesi_student(student):

    cursor_connection = connection_open();
    data = (student.ime, student.prezime)
    query = "INSERT INTO student  (student_Ime, student_prezime) VALUES ( %s,  %s)"
    try:
        cursor_connection[0].execute(query, data)
        cursor_connection[1].commit()
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor_connection[0], cursor_connection[1])


def unesi_predmet(predmet):
    
    cursor_connection = connection_open()

    data = (predmet.naziv, predmet.broj_ESPB)
    query = "INSERT INTO predmet (naziv_predmeta, broj_ESPB_bodova) VALUES (%s, %s)"
    try:
        cursor_connection[0].execute(query, data)
        cursor_connection[1].commit()
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor_connection[0], cursor_connection[1])


def unesi_profesora(profesor):

    cursor_connection = connection_open()
    data = (profesor.ime, profesor.prezime)
    query = "INSERT INTO profesor (profesor_ime, profesor_prezime) VALUES (%s, %s)"
    try:
        #upisivanje profesora u bazu
        cursor_connection[0].execute(query, data)
        cursor_connection[1].commit()
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor_connection[0], cursor_connection[1])



def get_predmet_i_student_id(student, predmet):

    cursor_connection = connection_open()
    query_student = "SELECT idStudent FROM student WHERE student_ime = %s AND  student_prezime LIKE %s"
    querry_predemt = "SELECT idPredmet FROM predmet WHERE naziv_predmeta LIKE %s AND broj_ESPB_bodova LIKE %s"
    try:
        # uzizamo id studenta 
        cursor_connection[0].execute(query_student,(student.ime, student.prezime))
        student_id = cursor_connection[0].fetchall()
        # uzizamo id predmeta
        cursor_connection[0].execute(querry_predemt, (predmet.naziv, predmet.broj_ESPB))
        predmet_id = cursor_connection[0].fetchall()
        # Iz nekog razloga dobijam listu u nizu pa moram ovako da vracam vrednosti 
        
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor_connection[0], cursor_connection[1])
        # Iz nekog razloga dobijam listu u nizu pa moram ovako da vracam vrednosti
        return (student_id[0][0], predmet_id[0][0])
    

def upis_na_precmet(student, predmet):

    ids = get_predmet_i_student_id(student, predmet)
    cursor_connection = connection_open()
    query = "INSERT INTO student_has_predmet (student_idStudent, predmet_idPredmet) VALUES (%s, %s)"
    try:
        cursor_connection[0].execute(query, (ids[0], ids[1]))
        cursor_connection[0].commit()
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor_connection[0], cursor_connection[1])


def get_predmet(predmet_id):

    cursor_connection = connection_open()
    query = "SELECT * FROM predmet WHERE idPredmet LIKE %s"
    try:
        cursor_connection[0].execute(query,(predmet_id,))
        predmet_list = cursor_connection[0].fetchall()
        predmet = clss.predmet(predmet_list[0][1], predmet_list[0][2])
        
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor_connection[0], cursor_connection[1])
        return predmet


def get_profesor(profesor_id):

    cursor_conection = connection_open()
    query = "SELECT * FORM profesor WHERE idProfesor LIKE %s"
    try:
        cursor_conection[0].execute(query, (profesor_id,))
        profesor_list = cursor_conection[0].fetchall()
        profesor = clss.profesor(profesor_list[0][1], profesor_list[0][2])
        
    except Error as e:
        print("Erroer: ", e)
    finally:
        connection_close(cursor_conection[0], cursor_conection[1])
        return profesor

def get_student(student_id):

    cursor_conection = connection_open()
    query = "SELECT * FORM profesor WHERE idStudent LIKE %s"
    try:
        cursor_conection[0].execute(query, (student_id, ))
        student_list = cursor_conection[0].fetchall()
        student = clss.pstudent(student_list[0][1], student_list[0][2])
        
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor_conection[0], cursor_conection[1])
        return student
       

def get_all_students():
    cursor_connection = connection_open()
    query = "SELECT * FROM student"

    try:
        cursor_connection[0].execute(query)
        students = cursor_connection[0].fetchall()
    except Error as e:
        print("Error: ", e)

    students_list = []
    
    for x in students:
        students_list.append(clss.student(x[0],x[1],x[2]))

    connection_close(cursor_connection[0], cursor_connection[1])
    return students_list


def get_all_proffesors():
    cursor_connection = connection_open()
    query = "SELECT * FROM profesor"

    try:
        cursor_connection[0].execute(query)
        students = cursor_connection[0].fetchall()
    except Error as e:
        print("Error: ", e)

    proffesor_list = []
    
    for x in students:
        proffesor_list.append(clss.profesor(x[0], x[1], x[2]))

    connection_close(cursor_connection[0], cursor_connection[1])
    return proffesor_list

def get_all_predmete():
    cursor_connection = connection_open()
    query = "SELECT * FROM predmet"

    try:
        cursor_connection[0].execute(query)
        students = cursor_connection[0].fetchall()
    except Error as e:
        print("Error: ", e)

    proffesor_list = []
    
    for x in students:
        proffesor_list.append(clss.profesor(x[0], x[1], x[2]))

    connection_close(cursor_connection[0], cursor_connection[1])
    return proffesor_list
        


        
    
    
    


