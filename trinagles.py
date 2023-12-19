
def xesNos (count):
    limit = int(count/2)
    print("")
    for i in range(1, limit):
        line = "x" * i + " " * (count+1-2*i) + "o" * i
        print(line)
    for i in range(limit, 0, -1):
        line = "x" * i + " " * (count+1-2*i) + "o" * i
        print(line)
    print("")

def getCount():
    number = input("Geben Sie eine GERADE Zahl ein (max 120): ")
    count = int(number)
    if count % 2 != 0 or count > 120:
        print("Sie haben eine ungerade Zahl eingegeben...")
        getCount()
    return count


if __name__ == "__main__":
    xesNos(getCount())