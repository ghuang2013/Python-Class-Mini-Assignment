# Course: COP 4930  - Python Programming
# Term:   Fall 2015 - Dr. Clovis Tondo
# Author: Guan Huang
# Assignment #6


class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)

    def __gt__(self, other_node):
        return self.data > other_node.get_data()

    def __lt__(self, other_node):
        return self.data < other_node.get_data()

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data

    def set_next(self, new_next):
        self.next_node = new_next


class List(object):
    def __init__(self, head = None):
        self.head = head

    def remove(self, data):
        print("\nremove('{}')".format(data))
        cur = self.head
        if data == cur.get_data():
            self.head = cur.get_next()
            cur = None
        else:
            while cur.get_next() and data != cur.get_next().get_data():
                cur = cur.get_next()
            if cur.get_next():
                to_del = cur.get_next()
                after = to_del.get_next()
                cur.set_next(after)
                to_del = None
            else:
                return False  # NO SUCH ELEMENT
        return True

    def insert(self, data):
        print("\ninsert('{}')".format(data))
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        if new_node < cur:
            new_node.set_next(cur)
            self.head = new_node
        else:
            while cur.get_next() and new_node > cur.get_next():
                cur = cur.get_next()
            after = cur.get_next()
            cur.set_next(new_node)
            new_node.set_next(after)

    def print(self):
        print("\nprint()")
        cur = self.head
        while cur:
            print("{0}\t{1}\t{2}".format(id(cur), cur, id(cur.get_next())))
            cur = cur.get_next()


class LinkedListOperation(object):
    INSERT = 'i'
    REMOVE = 'r'
    PRINT = 'p'


def read_file(filename):
    try:
        file = open(filename)
    except FileNotFoundError as e:
        print("Error: ", e.strerror)
        quit()
    return file


def main():
    my_list = List()
    file = read_file("llist.txt")
    for line in file:
        token = line.rstrip().split()
        if len(token) > 1:
            if token[0] == LinkedListOperation.INSERT:
                my_list.insert(token[1])
            elif token[0] == LinkedListOperation.REMOVE:
                my_list.remove(token[1])
        else:
            if token[0] == LinkedListOperation.PRINT:
                my_list.print()
    file.close()


if __name__ == '__main__':
    main()
