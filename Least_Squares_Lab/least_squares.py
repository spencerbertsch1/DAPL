import time

class LeastSquares:

    def __init__(self, path_to_data: str):
        self.abspath: str = path_to_data

    def print_something(self):
        print(self.abspath)

# some test code 
if __name__=="__main__":
    ls = LeastSquares(path_to_data = 'poopoopeepee')
    ls.print_something()