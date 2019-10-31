def add_person(name, age):
    file_write = open('ex115/file.txt', 'a')
    file_write.writelines('NAME: {} | AGE: {} \n'.format(name, age))
    file_write.close()

def read_list():
    file_read = open('ex115/file.txt', 'r')
    with file_read:
        print(file_read.read())
    file_read.close()