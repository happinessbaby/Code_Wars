import numpy

def snail(snail_map):
    if len(snail_map) <= 1:
        return list(snail_map[0])
    new_map = numpy.flipud(numpy.transpose(snail_map[1:]))
    return list(numpy.append(snail_map[0], snail(new_map)))

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array))
