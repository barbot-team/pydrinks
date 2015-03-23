class Dispenser(object):
    def __init__(self, name, on_cmd, off_cmd, description=""):
        self.name = name
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd
        self.description = description
        
    def __str__(self):
        return "{0}: '{1}' on. '{2}' off".format(self.name, self.on_cmd, self.off_cmd)

