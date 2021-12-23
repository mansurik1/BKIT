from behave import given, then
from main import get_mod


@given('I put values {values} into the function')
def step_impl(context, values: str):
    values = list(map(int, values.replace("[", "").replace("]", "").split(", ")))
    context.result = get_mod(values[0], values[1])


@then('I get {result}')
def step_impl(context, result: str):
    assert str(context.result) == result
