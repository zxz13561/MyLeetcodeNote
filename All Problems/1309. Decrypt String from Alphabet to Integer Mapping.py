class Solution(object):
    def freqAlphabets(self, s):
        word_nums = []
        for w in s:
            if w != '#':
                word_nums.append(w)
            else:
                word_nums[-1] = word_nums.pop(-2) + word_nums[-1]

        return ''.join(chr(int(num) + 96) for num in word_nums)


if __name__ == '__main__':
    i_s = "1326#10#11#12"

    run = Solution()
    print(run.freqAlphabets(i_s))
