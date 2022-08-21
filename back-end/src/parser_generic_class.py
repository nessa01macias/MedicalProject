import abc

# abc metaclass makes the class an abstractClass so we cannot create instances of it
# and the child class have a cumpulsion of having those methods inside them
class MedicalDocParser(metaclass= abc.ABCMeta):
    def __init__(self, text):
        self.text = text

    @abc.abstractmethod
    # it is an abstract method because we are leaving it in blank
    def parse(self):
        # it will return a dictionary or a JSON object at some point in the child class
        pass