from abc import ABC, abstractmethod
from copy import deepcopy
class Prototype(ABC):
    def clone(self):
        pass

class PythonObject(Prototype):
    def __init__(self, *args):
        self.value_one = args[0]
        self.value_two = args[1]

    def value_sum(self):
        return self.value_one + self.value_two

    def clone(self):
        return deepcopy(self)
        # copying the instance of the class with its properties and methods

obj = PythonObject(1,2)
assert(obj.value_sum() == obj.clone().value_sum())
# lets have this scenario where you have a object that has student record with
# properties like id, name, age, class and course, he/she wants to view these
# details, asks for this details, the provider creates a respective student
# object loaded with details, serves him/her the object with students details of
# him/her, now the student after viewing the details wants to download it, now
# two choices either you construct the student class in your download page
# again with student details or just clone the object that is in view page.
