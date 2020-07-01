#!/usr/bin/env python3

import os


class Student:
    _id = 0
    _name = ''
    _year = 1
    _sex = ''
    _department = ''
    _block = 1

    def addStudent(self):
        decor()
        print('Enter Student Name: ')
        self._id = input('ID: ')
        self._name = input('Name: ').upper()
        self._year = input('Year: ')
        self._sex = input('Sex: ').upper()
        self._department = input('Department: ').upper()
        self._block = input('Block: ')
        student = {'ID': self._id, 'Name': self._name, 'Year': self._year,
                   'Sex': self._sex, 'Department': self._department, 'Block': self._block}
        outfile = open('student.txt', 'at')
        print(student, file=outfile)
        outfile.close()
        print('\t\t Student has been added successfully!')

    def displayAll(self):
        decor()
        infile = open('student.txt', 'rt')
        if(infile == ''):
            print("""
                No Student on the database!
             """)
        else:
            count = 0
            print()
            for line in infile:
                count += 1
                diction = eval(str(line))
                ID = diction['ID']
                Name = diction['Name']
                Year = diction['Year']
                Department = diction['Department']
                Block = diction['Block']
                print(
                    f'{count}) ID: {ID} \t Name: {Name} \t Year: {Year} \t Department: {Department} \t Block: {Block}')
                # print(line.rstrip())
            print()

    def updateStudent(self):
        decor()
        update = False
        dict1 = {}
        id = input('Enter the Id of the student u wanna update: ')
        infile = open('student.txt', 'r')
        outfile = open('student1.txt', 'at')
        for line in infile:
            if line == '':
                break
            diction = eval(str(line))
            if(diction['ID'] == id):
                dict1['ID'] = diction['ID']
                dict1['Name'] = diction['Name']
                dict1['Year'] = diction['Year']
                dict1['Department'] = diction['Department']
                dict1['Block'] = diction['Block']
                update = True
                updateField = input('Enter the field u wanna update: ').upper()
                if(updateField == 'ID'):
                    dict1['ID'] = int(input('Enter ID: '))
                elif(updateField == 'NAME'):
                    dict1['Name'] = input('Enter Name: ').upper()
                elif(updateField == 'YEAR'):
                    dict1['Year'] = int(input('Enter Year'))
                elif(updateField == 'DEPARTMENT'):
                    dict1['Department'] = input('Enter Department: ').upper()
                elif(updateField == 'BLOCK'):
                    dict1['Block'] = int(input('Enter Block'))
                else:
                    print(f'Field {updateField} does not exist')
                print(dict1, file=outfile)
                continue
            print(line, end="", file=outfile)
        outfile.close()
        if update:
            os.remove('student.txt')
            os.rename('student1.txt', 'student.txt')
            print('\n Student has been successfully Updated!')
        else:
            print(f'No Student found with ID {id}')
            os.rename('student1.txt', 'student.txt')

    def removeStudent(self):
        decor()
        delete = False
        name = input('Enter the name of the student u wanna delete: ').upper()
        infile = open('student.txt', 'r')
        outfile = open('student1.txt', 'at')
        for line in infile:
            if line == '':
                break
            diction = eval(str(line))
            if(diction['Name'] == name):
                delete = True
                continue
            print(line, end="", file=outfile)
        outfile.close()
        if delete:
            os.remove('student.txt')
            os.rename('student1.txt', 'student.txt')
            print('\n Student removed successfully!')
        else:
            print(f'No Student found with Name {name}')
            os.rename('student1.txt', 'student.txt')


def decor():
    print('\t\t\t\t  AASTU')
    print('\t\t==Welcome to student Registration==')


def main():
    print('\t\t\t\t==================================')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t|      AASTU STUDENT             |')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t|      REGISTRATION              |')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t|         System                 |')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t|         Press                  |')
    print('\t\t\t\t|   1. To add a student          |')
    print('\t\t\t\t|   2. To display students       |')
    print('\t\t\t\t|   3. to Update student         |')
    print('\t\t\t\t|   4. to remove student         |')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t==================================')

    choice = int(input('Choice: '))
    student = Student()
    if(choice == 1):
        student.addStudent()
    elif(choice == 2):
        student.displayAll()
    elif(choice == 3):
        student.updateStudent()
    elif(choice == 4):
        student.removeStudent()


if __name__ == '__main__':
    main()
