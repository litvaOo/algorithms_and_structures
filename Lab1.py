class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        """
        Checking state of a list
        """
        return self.first is None

    def size(self):
        current = self.first
        count = 1
        while current.next_node != self.first:
            count = count + 1
            current = current.next_node

        return count

    def add(self, value):
        """
        Method, adding new nodes to list
        """
        if not self.isEmpty():
            new_node = Node(value, self.first)
            self.last.next_node = new_node
            self.last = new_node
        else:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
    
    def get(self, index):
        """
        Get node by index
        """
        current_node = self.first
        for _ in range(index-1):
            current_node = current_node.next_node
        return current_node

    def average(self):
        current = self.first
        summ = current.data
        for _ in range(self.size()):
            summ += current.data
            current = current.next_node
        return summ/self.size()

    def min_and_max(self):
        minimum = self.first
        maximum = self.first
        current_node = self.first
        for _ in range(self.size()):
            if minimum.data > current_node.data:
                minimum = current_node
            if maximum.data < current_node.data:
                maximum = current_node
            current_node = current_node.next_node
        return minimum, maximum

    def pre_minimum(self, minimum):
        current_node = self.first        
        for _ in range(self.size()):
            if current_node.next_node == minimum:
                return current_node
            current_node = current_node.next_node


class Node:
    """
    Class, representing particular node in a list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    starting_number = int(input())
    my_list = LinkedList()
    for _ in range(starting_number):
        my_list.add(int(input()))
    print(my_list.size())
    minimum, maximum = my_list.min_and_max()
    print(str(minimum) + " " + str(maximum))
    print(my_list.pre_minimum(minimum).data)
    print(my_list.average())
    print(my_list.get(4).data)