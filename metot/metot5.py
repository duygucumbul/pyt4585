

def decorator_metot(metot):
    def sarmalmetot():
        print("sarmal metot : {}'dan önce tetiklendi".format(metot.__name__))
        return metot()
    return sarmalmetot

@decorator_metot
def print_metot():
    print("print_metot tetiklendi")

print_metot() 

