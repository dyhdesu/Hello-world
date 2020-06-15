class person:
    def __init__(self, N: int, name: str):
        self.N =N
        self.name = name
class student(person):
    def  __init__(self, N: int, mzi: str):
        super().__init__(N,mzi)
        self.mzi = mzi

x= student(10,"abb")
print(x.N)
print(x.mzi)
print(x.name)