from Interpreter import Parse

while True:
    try:
        Input = str(input(f'Lenk {Parse("version:only")}>'))
        Output = Parse(Input)
        print(f'{Output}\n')
    except KeyboardInterrupt:
        import sys
        sys.exit(0)
