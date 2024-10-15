class Introspection:
    def __init__(self, obj):
        self.obj = obj

    def get_info(self):
        obj_type = type(self.obj)
        attributes = [attr for attr in dir(self.obj)
                      if not callable(getattr(self.obj, attr))]
        methods = [attr for attr in dir(self.obj)
                   if callable(getattr(self.obj, attr))]
        module = getattr(self.obj, '__module__', 'builtins')

        a = {
            "type": obj_type,
            "attributes": attributes,
            "methods": methods,
            "module": module,
        }
        return a

    def __str__(self):
        return str(self.get_info())


number_info = Introspection(42)
print(number_info)
string_info = Introspection("Hello")
print(string_info)
list_info = Introspection([1, 2, 3])
print(list_info)