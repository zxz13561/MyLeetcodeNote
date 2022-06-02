import re

class Solution(object):
    def interpret(self, command: str) -> str:
        c = re.sub(r'[(][)]', 'o', command)
        return re.sub(r'[(]al[)]', 'al', c)


if __name__ == '__main__':
    c = "(al)G(al)()()G"

    run = Solution()
    print(run.interpret(c))
