'''
    # [Text] = <h1>[Text]</h1>
'''
import sys

class Markdown:
    def __init__(self, fileName):
        self.fileName = fileName

    def toString(self):
        return self.fileName

if __name__ == '__main__':
    try:
       m = Markdown(sys.argv[1])
       print(m.toString())
    except:
        print(f'usage: python3 {sys.argv[0]} <file.md>')