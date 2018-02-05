# Generic implementation of the Submodel Execution Loop

from littlemuscle import Configuration, Message, Operator, SubmodelDescription, TimeDrivenSubmodel

from overrides import overrides
from typing import Any, Dict

class Micro(TimeDrivenSubmodel):
    @overrides
    def describe(self) -> SubmodelDescription:
        desc = SubmodelDescription(2)
        desc.add_endpoint(Operator.F_INIT, 'init')
        desc.add_endpoint(Operator.O_F, 'result')
        return desc


    def __init__(self) -> None:
        pass


    @overrides
    def initialise_state(self,
            configuration: Configuration,
            initial_time: float,
            input_messages: Dict[str, Message]
            ) -> None:
        print('Micro model f_init at {} with input {}'.format(
            initial_time, input_messages['init']))

    @overrides
    def solve(self,
            time: float,
            input_messages: Dict[str, Message]
            ) -> None:
        print('Micro model S at {} with input {}'.format(
            time, input_messages))

    @overrides
    def update_boundary_conditions(self,
            time: float,
            input_messages: Dict[str, Message]
            ) -> None:
        print('Micro model B at {} with input {}'.format(
            time, input_messages))

    @overrides
    def has_converged(self) -> bool:
        return False

    @overrides
    def observe_intermediate_state(self) -> Dict[str, Any]:
        print('Micro model O_i')
        return {}

    @overrides
    def observe_final_state(self) -> Dict[str, Any]:
        print('Micro model O_f')
        return { 'result': 'Micro model result' }
