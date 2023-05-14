#!/usr/bin/env python3


#  Title: priority-queue.py
#  Abstract: implement prioity queue. Must hace a front and back
#  Author: Seth Pickford
#  Email: spickfor@nd.edu
#  Estimate: 2 hrs
#  Date: 3/19/23


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enque(self, item):
        if not self.queue:
            self.queue.append(item)
        else:
            for i, element in enumerate(self.queue):
                if item < element:
                    self.queue.insert(i, item)
                    break
            else:
                self.queue.append(item)

    def deque(self):
        if not self.is_Empty():
            return self.queue.pop(0)
        else:
            return None

    def is_Empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Priority Queue:", self.queue)

def menu():
    pq = PriorityQueue()

    while True:
        print("\nMenu:")
        print("1. Enque")
        print("2. Deque")
        print("3. IsEmpty")
        print("4. Display")
        print("5. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = int(input("Enter the item to enque: "))
            pq.enque(item)
        elif choice == 2:
            item = pq.deque()
            if item is not None:
                print(f"Dequeued item: {item}")
            else:
                print("The queue is empty.")
        elif choice == 3:
            print("Is the queue empty?", pq.is_Empty())
        elif choice == 4:
            pq.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
