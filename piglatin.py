class PigLatin:

    def __init__(self, phrase: str):
        self.phrase=phrase


    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        elif self.phrase[0]=="a" or self.phrase[0]=="e" or self.phrase[0]=="i" or self.phrase[0]=="o" or self.phrase[-1]=="u":
            if self.phrase[-1]=="y":
                return self.phrase+"nay"
            elif self.phrase[-1]=="a" or self.phrase[-1]=="e" or self.phrase[-1]=="i" or self.phrase[-1]=="o" or self.phrase[-1]=="u" :
                return self.phrase+"yay"
            elif self.phrase[-1]!="a" or self.phrase[-1]!="e" or self.phrase[-1]!="i" or self.phrase[-1]!="o" or self.phrase[-1]!="u":
                return self.phrase+"ay"
        else:
            return "Not starting with a vowel"
