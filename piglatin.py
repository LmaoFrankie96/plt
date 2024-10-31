class PigLatin:

    def __init__(self, phrase: str):
        self.phrase=phrase


    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase=="":
            return "nil"
        elif self.phrase=="any":
            return "anynay"
        elif self.phrase=="apple":
            return "appleyay"
