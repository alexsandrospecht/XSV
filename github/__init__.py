from github.Converter import Converter

def main():
    c = Converter('<Registros><Registro><campo1>valor1</campo1></Registro><Registro><campo1>valor2</campo1></Registro></Registros>')
    c.converter()

if __name__ == '__main__':
    main()
    