from os import system

class Menu():
    pass
    def __init__(self, elenemts=[]) :
        self.elements = elenemts

    def print(self):
        for (mark, text, _) in self.elements:
            print('{} - {}'.format (mark, text))


    def run(self, prompt=">: "):
        # def clrscr():
        #     return system('cls')
        while True:
            # clrscr()
            self.print()
            user_choice = input(prompt)
            for (mark, _, rummethod) in self.elements:
                if user_choice == mark:
                    if rummethod == -1:
                        return True
                    # clrscr()
                    rummethod()
                    break
