"""Word Finder: finds random words from a dictionary."""


class WordFinder:

    def __init__(self, filename):
        self.filename = open(filename)
        self.word_list = []
        self.read()

    def read(self):
        self.word_counter = 0
        # with open(self.filename) as self.f:
        self.lines = self.filename.readlines()
        for self.line in self.lines:
            self.word_counter = self.word_counter + 1
            self.word_list.append(self.line.strip())
        print(f"{self.word_counter} words read")

    def random(self):
        import random
        return self.word_list[random.randrange(len(self.word_list))]

class SpecialWordFinder(WordFinder):

    def __init__(self,filename):
        super().__init__(filename)

    def read(self):
        self.word_counter = 0
        # with open(self.filename) as self.f:
        self.lines = self.filename.readlines()
        for self.line in self.lines:
            if not self.line.startswith('#') and self.line != "\n":
                self.word_counter = self.word_counter + 1
                self.word_list.append(self.line.strip())
        print(f"{self.word_counter} words read")
    
    


        


    

