if __name__ == '__main__':
    i = 0
    mess = ""
    while i < 1:
        word = input()
        if word == 'stop':
            break
        else:
             mess += word + " "
    print(mess)