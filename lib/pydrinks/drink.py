class Drink(object):
    def __init__(self, name, recipe, timebase=2, description=""):
        self.name = name
        self.timebase = timebase
        self.description = description
        self.recipe = []
        if isinstance(recipe, list):
            for step in recipe:
                if isinstance(step, tuple):
                    if len(step) is not 2:
                        raise TypeError('The recipe argument should be a list of tuples of length 2')
                    else:
                        self.recipe.append(step)
                else:
                    raise TypeError('The recipe argument should be a list of tuples of length 2')
        else:
            raise TypeError('The recipe argument should be a list of tuples of length 2')

    def __str__(self):
        string = "{0}:".format(self.name)
        for step in self.recipe:
            string += ( "\n\t- {0} parts {1}".format(step[1], step[0]))
        return string

