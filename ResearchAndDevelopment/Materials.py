import persistent

class Material(persistent.Persistent):

    def __init__(self):
        self.MatName = None
        self.Color = None
        self.Reflectivity = None
        self.BaseType = None

class Wood(Material):

    def __init__(self):
        self.MatName = 'Wood'
        self.Color = 'Brown'
        self.Reflectivity = 'Dull'
        self.BaseType = None
