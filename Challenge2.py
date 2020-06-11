# Creating a class and a CRUD with OOP

import pymysql

def line():
    print('-' * 50)

try:
    con = pymysql.connect(db='school1', user='root', passwd='')
    cursor = con.cursor()
except Exception as error:
    print('Problems with databank connection!')
    print(error)


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    # INSERT
    def insert_student(self, student_id, name):
        try:
            cursor.execute('''Insert into student (student_id, name) values (%s, %s)''', (student_id, name))
        except Exception as error_insert:
            print(error_insert)
            print('Problems in the insert')
        else:
            print('Student registered!')
            con.commit()
            con.close()

    # Update
    def update_student(self, new_name):
        try:
            cursor.execute('UPDATE student SET name = %s WHERE student_id = %s', (new_name, self.student_id))
        except Exception as error_update:
            print('Problems in the update')
            print(error_update)
        else:
            print('Student updated!')
            con.commit()
            con.close()

    # Delete
    def delete_student(self):
        try:
            cursor.execute('DELETE FROM student WHERE student_id = %s', (self.student_id,))
        except Exception as error_delete:
            print('Problems in the delete')
            print(error_delete)
        else:
            print('Student deleted!')
            con.commit()
            con.close()

    # Select
    def get_student_bd(self):
        try:
            list_student_id = []
            list_name = []
            cursor.execute('SELECT * FROM student where student_id = %s', (self.student_id,))
            for i in cursor.fetchall():
                list_student_id.append(i[0])
                list_name.append(i[1])
        except Exception as error_select:
            print('Problems in the Select')
            print(error_select)
        else:
            print(f'ID: {list_student_id[0]}\n'
                  f'Name: {list_name[0]}')

# def get_aluno():
#     try:
#         student_id = input('ID Student: ')
#         name = input('Name: ')
#     except Exception as error:
#         print('Problems!')
#         print(error)
#     else:
#         student = Student(student_id, name)
#         print(student.student_id)
#         student.register_student(student_id, name)


student2 = Student('2', 'João')
#student2.insert_student(student2.student_id, student2.name)
#student2.update_student('Lax')
#line()
line()
student2.get_student_bd()
