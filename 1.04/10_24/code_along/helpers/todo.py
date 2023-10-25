
def get_todo():
    with open(r"C:\Users\XTAGH\Documents\GitHub\10-02_TKH\1.04\10_24\code_along\data\todo.txt") as f:
        lines = f.readlines()

        for row in lines:
            print(row)


print("youve ran todo.py")


