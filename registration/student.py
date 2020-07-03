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
        print('\nEnter Student Name: ')
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
        print('\t\t Student has been added successfully!\n')
        permission = input('Do U wanna Continue? [Y|N] ').upper()
        if(permission == 'Y'):
            main()
        else:
            print("""
            
                        Good Bye!
            
            \n\n""")

    def displayAll(self):
        decor()
        print()
        infile = open('student.txt', 'rt')
        if(infile == ''):
            print("""
                \nNo Student on the database!
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
            infile.close()
            print()
        permission = input('Do U wanna Continue? [Y|N] ').upper()
        if(permission == 'Y'):
            main()
        else:
            print("""
            
                        Good Bye!
            
            \n\n""")

    def updateStudent(self):
        decor()
        update = False
        dict1 = {}
        id = input('\nEnter the Id of the student u wanna update: ')
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
                print(
                    f'\n\t\tID: { dict1["ID"]} \t Name: { dict1["Name"]} \t Year: { dict1["Year"]} \t Department: { dict1["Department"]} \t Block: { dict1["Block"]}\n')
                update = True
                updateField = input(
                    'Enter the field u wanna update: ').upper()
                if(updateField == 'ID'):
                    dict1['ID'] = int(input('Enter ID: '))
                elif(updateField == 'NAME'):
                    dict1['Name'] = input('Enter Name: ').upper()
                elif(updateField == 'YEAR'):
                    dict1['Year'] = int(input('Enter Year'))
                elif(updateField == 'DEPARTMENT'):
                    dict1['Department'] = input(
                        'Enter Department: ').upper()
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
            print(f'No Student found with ID "{id}"')
            os.rename('student1.txt', 'student.txt')
        permission = input('Do U wanna Continue? [Y|N] ').upper()
        if(permission == 'Y'):
            main()
        else:
            print("""
            
                        Good Bye!
            
            \n\n""")

    def search(self):
        decor()
        searchName = input('Enter the Name of the Student: ').upper()
        infile = open('student.txt', 'r')
        for line in infile:
            diction = eval(str(line))
            if(diction['Name'] == searchName):
                ID = diction['ID']
                Name = diction['Name']
                Year = diction['Year']
                Department = diction['Department']
                Block = diction['Block']
                print('\n\t\t\t\tStudent Found!')
                print(
                    f'\n\t\tID: {ID} \t Name: {Name} \t Year: {Year} \t Department: {Department} \t Block: {Block}\n')
                break
        else:
            print("""
                            No Student found with given Name!
            """)

        permission = input('Do U wanna Continue? [Y|N] ').upper()
        if(permission == 'Y'):
            main()
        else:
            print("""
            
                        Good Bye!
            
            \n\n""")

    def removeStudent(self):
        decor()
        delete = False
        name = input(
            '\nEnter the name of the student u wanna delete: ').upper()
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
        permission = input('Do U wanna Continue? [Y|N] ').upper()
        if(permission == 'Y'):
            main()
        else:
            print("""
            
                        Good Bye!
            
            \n\n""")


def decor():
    print('\n\t\t\t\t  AASTU')
    print('\t\t==Welcome to student Registration==')


def main():
    print('\n\t\t\t\t==================================')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t|          AASTU  STUDENT        |')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t|           REGISTRATION         |')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t|         System                 |')
    print('\t\t\t\t|                                |')
    print('\t\t\t\t|           Press                |')
    print('\t\t\t\t|     1. To add a student        |')
    print('\t\t\t\t|     2. To display students     |')
    print('\t\t\t\t|     3. to Update student       |')
    print('\t\t\t\t|     4. Search for a Student    |')
    print('\t\t\t\t|     5. to remove student       |')
    print('\t\t\t\t|     0. EXIT                    |')
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
        student.search()
    elif(choice == 5):
        student.removeStudent()
    else:
        print("""
            
                        \t\tGood Bye!
            
            """)
        SystemExit()


if __name__ == '__main__':
    main()
