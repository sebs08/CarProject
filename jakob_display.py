import os


class display_emulator():
    top_line = "*" * 24 + "\n" + "*" + " " * 22 + "*\n"
    bottom_line = "*" + " " * 22 + "*\n" + "*" * 24

    line1 = "*" + " " * 22 + "*\n"
    line2 = "*" + " " * 22 + "*\n"

    def update(self, input_text, line):
        if line == 1:
            self.line1 = "*   " + input_text + "   *\n"
        elif line == 2:
            self.line2 = "*   " + input_text + "   *\n"

    def display_text(self):
        print("\n"*5)  # a little hack
        print(self.top_line + self.line1 + self.line2 + self.bottom_line)
        print("\n")



emulator = display_emulator()

def display_line(input_text, line):
    display_sting = str(input_text)
    if not (line == 1 or line == 2):
        print("there is no such line as: %s" % (line))
        raise IndexError
    if len(input_text) != 16:
        print("Der text ist zu lang: %s Zeichen" % (len(display_sting)))
        raise IOError

    emulator.update(display_sting, line)
    emulator.display_text()


if __name__ == "__main__":
    display_line(" " * 3 + "guten Tag" + " " * 4, 1)
    display_line(" " * 3 + "und tschuess ", 2)
    display_line(" " * 3 + "und tschuess ", 1)