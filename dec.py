def dec1(func1):
    def dec2():
        print("now")
        func1()
        print("than")
        return dec2


@dec1

def who():
    print("lad")
who()
