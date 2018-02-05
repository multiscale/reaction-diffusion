from littlemuscle import Configuration, Message, Operator, SubmodelDescription, TimeDrivenSubmodel

from overrides import overrides
from typing import Any, Dict

class Macro(TimeDrivenSubmodel):
    @overrides
    def describe(self) -> SubmodelDescription:
        desc = SubmodelDescription(2)
        desc.add_endpoint(Operator.O_I, 'state_out')
        desc.add_endpoint(Operator.S, 'step_in')
        return desc


    def __init__(self) -> None:
        pass


    @overrides
    def initialise_state(self,
            configuration: Configuration,
            initial_time: float,
            input_messages: Dict[str, Message]
            ) -> None:
        print('Macro model f_init at {} with input {}'.format(
                initial_time, input_messages))

    @overrides
    def solve(self,
            time: float,
            input_messages: Dict[str, Message]
            )-> None:
        print('Macro model S at {} with input {}'.format(
                time, input_messages))

    @overrides
    def update_boundary_conditions(self,
            time: float,
            input_messages: Dict[str, Message]
            ) -> None:
        print('Macro model B at {} with input {}'.format(
                time, input_messages))

    @overrides
    def has_converged(self) -> bool:
        return False

    @overrides
    def observe_intermediate_state(self) -> Dict[str, Any]:
        print('Macro model O_i')
        return { 'state_out': 'Macro model state' }

    @overrides
    def observe_final_state(self) -> Dict[str, Any]:
        print('Macro model O_f')
        return {}
