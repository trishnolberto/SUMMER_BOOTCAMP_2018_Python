import sys

class Employe:

    def __init__(self, nombcomp):
        first,last = nombcomp.lower().split(' ')
        self.__first, self._last = first,last
        self.email = first + "." + last + "@email.com"

    def getEmail(self):
        return self.email


author = "PBN"
# python lesson11/interactive_mode.py "Patricia Bautista"

if __name__ == "__main__":
    nomc = sys.argv[1]
    emp = Employe(nomc)
    print(emp.getEmail())