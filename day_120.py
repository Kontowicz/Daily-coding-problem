# Implement the singleton pattern with a twist. First, instead of storing one instance, store two 
# instances. And in every even call of getInstance(), return the first instance and in every odd 
# call of getInstance(), return the second instance.
class solution:
    instance = {}
    even = False

    def __init__(self, num):
        self.num = num


    @staticmethod
    def initialize():
        solution.instance[0] = solution(0)
        solution.instance[1] = solution(1)

    @staticmethod
    def getInstance():
        if not solution.instance:
            solution.initialize()

        if solution.even:
            solution.even = False
            return solution.instance[0]
        else:
            solution.even = True
            return solution.instance[1]