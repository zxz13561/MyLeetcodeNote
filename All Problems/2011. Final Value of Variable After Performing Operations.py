class Solution(object):
    def finalValueAfterOperations(self, operations):
        listVals = {
            '--X': -1,
            'X--': -1,
            '++X': +1,
            'X++': +1
        }
        val = 0
        i = 0
        for i in operations:
            val += listVals[i]
        return val


if __name__ == '__main__':
    input_operations = ["--X", "X++", "X++"]
    run = Solution()
    print(run.finalValueAfterOperations(input_operations))
