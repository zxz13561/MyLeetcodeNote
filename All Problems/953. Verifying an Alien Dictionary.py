class Solution(object):
    def isAlienSorted(self, words, order):
        if len(words) == 1:
            return True

        order_dic = {a: i for i, a in enumerate(order)}

        for i, w in enumerate(words):
            if i + 1 > len(words) - 1:
                break

            next_w, next_len = words[i + 1], len(words[i + 1])

            if order_dic[w[0]] > order_dic[next_w[0]]:
                return False
            elif order_dic[w[0]] == order_dic[next_w[0]]:
                for w_i, a in enumerate(w[1:]):
                    if w_i + 1 > next_len - 1:
                        return False
                    elif order_dic[a] > order_dic[next_w[w_i + 1]]:
                        return False
                    elif order_dic[a] < order_dic[next_w[w_i + 1]]:
                        break

        return True


if __name__ == '__main__':
    i_words = ["apple","app"]
    i_order = "abcdefghijklmnopqrstuvwxyz"

    run = Solution()
    print(run.isAlienSorted(i_words, i_order))
