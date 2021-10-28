from .read_s_parameter_group              import read_s_parameter_group
from .save_measurement_locally            import save_measurement_locally
from rohdeschwarz.instruments.vna.channel import Channel


def monkeypatch():
    Channel.read_s_parameter_group   = read_s_parameter_group
    Channel.save_measurement_locally = save_measurement_locally
