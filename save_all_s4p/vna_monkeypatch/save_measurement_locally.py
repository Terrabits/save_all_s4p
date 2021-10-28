from skrf import save_network


def save_measurement_locally(self, filename, test_ports):
    # get frequencies
    freq_Hz = self.frequencies_Hz

    # get s parameters
    logical_ports          = self.to_logical_ports(test_ports)
    self.s_parameter_group = logical_ports
    s_params = self.read_s_parameter_group()

    # save
    save_network(freq_Hz, s_params, filename)
