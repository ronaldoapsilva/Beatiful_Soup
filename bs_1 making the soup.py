def titulo(msg):
    cores = {'verde':'\033[32m',
            'amarelo':'\033[33m',
            'vermelho':'\033[31m',
            'limpa':'\033[m'}
    print(f'{cores["vermelho"]}{msg}{cores["limpa"]}')
def exemplo(msg2):
    print('{:=^50}'.format(msg2))            

from bs4 import BeautifulSoup
def making_the_soup():
    titulo("Making the soup")
    from bs4 import BeautifulSoup

    with open("index.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    soup = BeautifulSoup("<html>data</html>", 'html.parser')

  
#making_the_soup()
