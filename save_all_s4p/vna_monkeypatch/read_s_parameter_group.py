import numpy


def read_s_parameter_group(self):
    vna = self._vna
    vna.settings.binary_64_bit_data_format = True

    scpi = ':CALC{0}:DATA:SGR? SDAT'
    scpi = scpi.format(self.index)
    vna.write(scpi)

    # read flat data
    result = vna.read_64_bit_complex_vector_block_data()

    # reshape data according to VNA
    ports          = len(self.s_parameter_group)
    points         = self.points
    original_shape = (ports, ports, points)
    original_array =  numpy.reshape(result, original_shape)

    # switch axes to match scikit-rf [s] syntax
    desired_array = numpy.swapaxes(original_array, 1, 2)
    desired_array = numpy.swapaxes(desired_array,  0, 1)
    return desired_array
