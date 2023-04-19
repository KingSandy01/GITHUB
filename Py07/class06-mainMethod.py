
def main():

    # TODO Write
    # -------How to write in the File--------

    # file = open("lco.txt", "w+")
    # for i in range(20):
    #     file.write("this is my python code %d \n" %(i)) 
    # file.close()

    # TODO Read
    #---------How to read the file------------

    # t = input("Enter the filename: ")
    # txt1 = ".txt"
    # t1 = t + txt1
    # t_mode = "r"

    # print(t1)

    # file = open(t1,t_mode)
    # if file.mode == 'r':
    #     filecontent = file.read()
    #     print(filecontent)

    # TODO Exception
    
    try: 
        myfile = open("lco.txt", "r")
        print("Success in Reading.")
    except IOError:
        print("File does not exists.")

    print("Task Done")

if __name__ == "__main__":
    main()