import littlemuscle as lm

from .micro import Micro
from .macro import Macro


if __name__ == '__main__':
    simulation = lm.Simulation()
    macro = Macro()
    micro = Micro()

    simulation.add_submodel('micro', micro)
    simulation.add_submodel('macro', macro)

    simulation.add_conduit('macro', 'state_out', 'micro', 'init')
    simulation.add_conduit('micro', 'result', 'macro', 'step_in')

    micro_configuration = lm.Configuration()
    micro_configuration.time_scale = lm.Scale(1, 10)

    macro_configuration = lm.Configuration()
    macro_configuration.time_scale = lm.Scale(20, 100)

    simulation.set_configuration('micro', micro_configuration)
    simulation.set_configuration('macro', macro_configuration)

    simulation.run()
