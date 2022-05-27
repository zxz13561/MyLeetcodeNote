from datetime import datetime as dt


def reverse_words(s):
    first_word = True
    word_list = s.split(" ")
    result_s = ""
    for word in word_list:
        if not first_word:
            result_s += " "
        result_s += word[::-1]
        first_word = False
    return result_s


if __name__ == '__main__':
    input_s = "Let's take LeetCode contest"
    print(reverse_words(input_s))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
