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
    student_id_list = []
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


student2 = Student('10', 'João')
line()
#student2.update_student('Lax')
#line()
student2.delete_student()
