import os


def main():
    i = 0

    # Pasta de destino dos arquivos a serem renomeados
    path = "C:/Users/davia/OneDrive/Documents/arquivosTeste/"

    for filename in os.listdir(path):
        my_dest = "file" + str(i) + ".txt"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == '__main__':
    main()
