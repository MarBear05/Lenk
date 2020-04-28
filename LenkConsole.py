#Get Lenk
from Lenk import Run

print(Run("Clear"))

while True:
    try:
        Input = str(input(f'Lenk {Run("version:only")}>'))
    #if ^C is omited
    except KeyboardInterrupt:
        exit(0)

    Output = Run(Input)
    print(f'{Output}\n')