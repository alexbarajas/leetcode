class CropRatio:

    def __init__(self):
        self._crops = {}
        self._total_weight = 0

    def add(self, name, crop_weight):

        if not name in self._crops:
            self._crops[name] = crop_weight
        else:
            self._crops[name] += crop_weight

        self._total_weight += crop_weight

    def proportion(self, name):
        try:
            return self._crops[name]/self._total_weight
        except KeyError:
            return name + " is not in the harvest."

#To see the output, uncomment the lines below:
crop_ratio = CropRatio()
crop_ratio.add('Wheat', 4)
crop_ratio.add('Wheat', 5)
crop_ratio.add('Rice', 1)

print(crop_ratio.proportion('Wheat'))
print(crop_ratio.proportion('Rice'))
print(crop_ratio.proportion('Corn'))

# THIS DID NOT WORK FOR ALL CASES