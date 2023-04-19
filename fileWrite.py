def main():
    file = open("hostels.txt", "w+")
    for i in range(10):
        file.write("Student %d \n" %(i))
    file.close()

if __name__ == "__main__":
    main()
