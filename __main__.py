# replace Channel.save_measurement_locally:
from save_all_s4p.vna_monkeypatch import monkeypatch
monkeypatch()


# imports
from pathlib      import Path
from save_all_s4p import get_timestamp
from rohdeschwarz.instruments.vna import Vna


# constants
PORTS = [1, 2, 3, 4]


# data path
data_path = Path.cwd() / 'data' / get_timestamp()
data_path.mkdir(parents=True)

# connect
vna = Vna()
vna.open_tcp()
vna.open_log('vna.log')


for set_name in vna.sets:
    # select set
    vna.active_set = set_name

    # save touchstone files
    for index in vna.channels:
        file_path = data_path / f'set-{set_name}-channel-{index}.s4p'

        channel = vna.channel(index)
        channel.save_measurement_locally(str(file_path), PORTS)

    # save trace data
    for trace_name in vna.traces:
        if trace_name.startswith(f'Ch') and '_SG_' in trace_name:
            # skip s parameter group traces
            continue

        file_path = data_path / f'set-{set_name}-trace-{trace_name}.csv'
        trace = vna.trace(trace_name)
        trace.save_complex_data_locally(str(file_path))

    # save screenshots
    for index in vna.diagrams:
        file_path = data_path / f'set-{set_name}-diagram-{index}.png'
        diagram = vna.diagram(index)
        diagram.save_screenshot_locally(str(file_path), image_format='PNG')
