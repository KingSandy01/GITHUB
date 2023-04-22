# read the created file

def main():
    file = open(t1, t_mode)
    if file.mode == 'r':
        fileContent1 = file.read()
        print(fileContent1)

if __name__ == "__main__":
    t = input("Enter the filename: ")
    txt1 = ".txt"
    t1 = t + txt1
    t_mode = "r"
    main()