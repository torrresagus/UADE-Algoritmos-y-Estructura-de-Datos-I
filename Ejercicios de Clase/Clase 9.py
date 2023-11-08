def intdiv(a, b):
    try:
        result = a // b
        print( 'The result is: ', result)
    except TypeError:
        print( 'Check operands. Sorne of them seems strange...')
    except ZeroDivisionError:
        print( 'Please do not divide by zero. ')
    except Exception:
        print('Ups. Something went wrong... ')
        
def main():
    intdiv(5, 0)
    intdiv(5, 'a')
    intdiv(5, 2)

main()