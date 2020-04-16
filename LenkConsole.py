from Interpreter import Parse
from sys import exit

def main():
    try:
        Input = str(input(f'Lenk {Parse("version:only")}>'))
    except KeyboardInterrupt:
        exit(0)
    Output = Parse(Input)
    print(f'{Output}\n')
    main()

main()
