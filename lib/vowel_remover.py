class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else:
                i += 1
        return self.text

    # def remove_vowels(self):
    #     i = 0
    #     str_len = len(self.text)
    #     while i < str_len:
    #         if self.text[0].lower() in self.vowels:
    #             self.text = self.text[1:]
    #         else:
    #             self.text = self.text[1:] + self.text[0]
    #         i += 1
    #     return self.text


remover = VowelRemover("aeiou")
print(remover.remove_vowels())
