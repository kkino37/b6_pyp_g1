import unittest
from unittest import mock


class Observer(object):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        # self.observers = []
        if not hasattr(self, 'observers'):
            self.observers = []
        self.observers.append(observer)
    
    def notifyAll(self, change):
        for observer in self.observers:
            observer(change)


class Collection(object):
    def __init__(self):
        self.data = []

    def add_element(self, element):
        raise NotImplementedError()

    def get_element(self):
        raise NotImplementedError()


class Queue(Observer, Collection):

    def add_element(self, element):
        self.data.insert(0, element)

    def get_element(self):
        return self.data.pop()


class Stack(Observer, Collection):

    def add_element(self, element):
        self.data.append(element)
        self.notifyAll("Element added to Stack: %s" % element)

    def get_element(self):
        elem = self.data.pop()
        self.notifyAll("Element removed to Stack: %s" % elem)
        return elem


class Vehicle(Observer):
    def __init__(self, model):
        self.model = model
        self.gas = 0

    def put_gas(self, gas_amount):
        self.gas += gas_amount
        self.notifyAll("Gas tank filled: %s" % gas_amount)


class Car(Vehicle):
    def move(self):
        print("I'm moving")


class Airplane(Vehicle):
    def move(self):
        print("I'm flying")


def on_element_added_in_stack(change):
    if 'added' in change:
        print("Element added")


def on_element_removed_on_stack(change):
    if 'removed' in change:
        print("Element removed")


s = Stack()

s.add_element(5)
s.get_element()


"""
c = Car('Ford')
c.add_observer(on_element_added_in_stack)
c.put_gas(10)

"""
# class QueueTestCase(unittest.TestCase):
#     def test_queue(self):
#         q = Queue()

#         q.add_element(1)
#         q.add_element(2)
#         q.add_element(3)

#         self.assertEqual(q.get_element(), 1)
#         self.assertEqual(q.get_element(), 2)

#     def test_stack(self):
#         s = Stack()

#         s.add_element(1)
#         s.add_element(2)
#         s.add_element(3)

#         self.assertEqual(s.get_element(), 3)
#         self.assertEqual(s.get_element(), 2)


# class VehicleObserverTestCase(unittest.TestCase):
#     def test_car_gas_observer(self):
#         c = Car('ford')
#         m = mock.MagicMock()

#         c.add_observer(m)
#         c.put_gas(5)

#         m.assert_called_once_with("Car tank gas filled with 5 gallons")

#     def test_airplane_gas_observer(self):
#         a = Airplane('boeing')
#         m = mock.MagicMock()

#         a.add_observer(m)
#         a.put_gas(1000)

#         m.assert_called_once_with("Airplane tank gas filled with 1000 gallons")


# class CollectionObserverTestCase(unittest.TestCase):
#     def test_queue_observer(self):
#         q = Queue()
#         m = mock.MagicMock()

#         q.add_observer(m)
#         q.add_element(5)

#         m.assert_called_once_with("Element added to Queue: 5")

#     def test_stack_observer(self):
#         s = Stack()
#         m = mock.MagicMock()

#         s.add_observer(m)
#         s.add_element("hello")

#         m.assert_called_once_with("Element added to Stack: hello")


# if __name__ == '__main__':
#     unittest.main()
