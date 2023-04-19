
def main():

# TODO Exception

    try: 
        myfile = open("lco.txt", "r")
        print("Success in Reading.")
    except IOError:
        print("File does not exists.")

    print("Task Done")

if __name__ == "__main__":
    main()