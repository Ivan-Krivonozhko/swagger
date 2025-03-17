from contextlib import contextmanager
from typing import TypeVar, Callable, ContextManager

from assertions.assertion_types import AssertionTypes

T = TypeVar('T')
StepProvider = Callable[[str], ContextManager]


@contextmanager
def default_step_provider(step: str):
    yield


class AssertModel:
    def __init__(self, expected: T) -> None:
        self.expected = expected
        self._description: str | None = None
        self._step_provider: StepProvider = default_step_provider


    def _error_template(self, actual: T, method: AssertionTypes):
        return f"""
               Checking: {self._description}
               Expected: {self.expected} {type(self.expected)}
               Actual: {actual} {type(actual)}
    
               Expression: assert {self.expected} {method} {actual}
               """


    def set_description(self, description: str):
        self._description = description
        return self


    @property
    def step_provider(self) -> StepProvider:
        return self._step_provider


    @step_provider.setter
    def step_provider(self, provider: StepProvider):
        self._step_provider = provider
