class Node:
    def __init__(self, data: dict):
        self.data = data
        self.next = None 

    def __repr__(self):
        return str(self.data) 

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data: dict):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node 

    def display(self):
        temp = self.head
        while temp:
            print("\n",temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def get_node(self, index):
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp
            temp = temp.next
            count += 1
        raise IndexError("Index out of range.")

    def update_key(self, node_index, key, value):
        node = self.get_node(node_index)
        node.data[key] = value
        print(f"\nUpdated node {node_index}: {node.data}")
    
    def clear_node_data(self, node_index):
        node = self.get_node(node_index)
        node.data.clear()
        print(f"Cleared data in node {node_index}.")

    def get_value(self, node_index, key):
        node = self.get_node(node_index)
        return node.data.get(key, "Key not found")


main = LinkedList()
main.append({"Name": "John", "Age": 25})
main.append({"Name": "Sean", "Age": 30})
main.append({"Name": "Charlie", "Age": 35})
main.append({"name": "Bob", "Age": 30})

main.display()

main.update_key(1, "age", 31) 

print("Charlie's age:", main.get_value(2, "Age"))

main.clear_node_data(3)

main.display()





  



    