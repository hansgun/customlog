from paiplog import paiplog
import log

@paiplog
def divide3(a=1,b=0) : 
    return a/b

if __name__ == '__main__':
    divide3()
