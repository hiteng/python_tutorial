



def write_operation():

    file_1 = open("new_file.txt", "w")

    file_1.write("This is a new file\n")
    file_1.writelines(["fgggrkjkjkrk\n",
                " ndnfvkjdnkjk\n",
                "\tkfkjkfvfkvdjn\n"])

    file_1.close()

    file_1 = open("new_file.txt","r")
    print file_1.read()

def append_operation():
    file_1 = open("new_file.txt", "a")

    file_1.write("This is append operation\n")
    file_1.writelines(["Hello world\n",
                       " Again hello world\n",
                       "\tThis is Sydney\n"])

    file_1.close()

if __name__ == '__main__':

    append_operation()
