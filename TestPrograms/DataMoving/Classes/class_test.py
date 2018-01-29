import super_test as super


class Class_test(super):
    this_is_a_class_method = "class method"

    def __init__(self, data):  # constructor method
        self.data = data  # instance data

    @classmethod  # method that mods class data instead of instance data
    def cls_method(cls, data):
        cls.data = data  # class data
        return cls.data

    @staticmethod  # method that doesnt use the class but is func related
    def stat_method(data):
        return data
