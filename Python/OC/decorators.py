def hello_decorator(function):
    print ('Hello from my decorator !')
    return function

class DoNotCare():
    def __init__(self, *largs,  **kwargs):
        self.hello_function()

    @hello_decorator
    def hello_function(self):
        print('hello world !')

if __name__ == '__main__':
    print('runtime !')
    DoNotCare()
