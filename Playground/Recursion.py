class test(object):
    def test_fun(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.test_fun(n - 1) + self.test_fun(n - 2)


if __name__ == '__main__':
    call_def = test()
    print(call_def.test_fun(3))
