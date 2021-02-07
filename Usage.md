# Usage

When using type hints in your scripts they must be in comments of the form `# type: str` because type hints were not part of the syntax for Python 2.7.
More information on Python 2.7 safe typing can be found in the [mypy documentation](https://mypy.readthedocs.io/en/stable/python2.html).

If you are writing a library module or package you have the option of using in-line type hints in comments, or creating separate stub files.
These stub files can be in the same folder as your library, or can be placed in the `automation/typings/` folder.

## Contents

* [Initial Setup](#Initial-Setup)
* [Examples](#Examples)
  * [In a Script](#In-a-Script)
  * [In a Library](#In-a-Library)
* [Tips and Tricks](#Tips-and-Tricks)
* [Actions](Actions.md)

## Reference

* [Rule Event Types](Reference.md#Rule-Event-Types)

## Initial Setup

In order to make your scripts and libraries a little cleaner, it is recommended to install the `typing` library using `pip`.
The examples on this page will assume you have `typing` installed.

```sh
pip install -t "{OH_CONF}/automation/lib/python" --python-version 2.7 --no-deps typing
```

Example with `typing` installed:

```python
import typing as t

if t.TYPE_CHECKING:  # put imports used only for type hints here
    from org.openhab.core.events import Event
```

Example *without* `typing` installed:

```python
try:
    import typing as t

    if t.TYPE_CHECKING:  # put imports used only for type hints here
        from org.openhab.core.events import Event
except:
    pass
```

## Examples

Most of these examples use the openHAB Scripters Helper Libraries.

### In a Script

```python
import typing as t
from core.rules import rule
from core.triggers import when

if t.TYPE_CHECKING:  # imports used only for type hints
    from core.jsr223.scope import ON
    from core.log import Slf4jLogger
    from org.openhab.core.items.events import ItemStateChangedEvent


@rule("Type hint example")
@when("Member of gMyGroup changed")
def rule_example(event):
    # type: (ItemStateChangedEvent) -> None
    log = rule_example.log  # type: Slf4jLogger
    if event.getItemState() == ON:
      log.info("%s changed to ON", event.getItemName())
```

That may seem like a lot so let's break it down:

#### Function Definition

```python
def rule_example(event):
    # type: (ItemStateChangedEvent) -> None
```

Here we are saying that the parameter `event` should be an instance of `ItemStateChangedEvent` (see [Reference](Reference.md#Rule-Event-Types) for a list) and that our function doesn't return anything (`-> None`).

#### Rule Log

```python
    log = rule_example.log  # type: Slf4jLogger
```

This line is not really necessary but it's something I use in all my rules to give me somewhere to put the type hint and make calls to `log` shorter.

#### Comparing a State

```python
    if event.getItemState() == ON:
```

In a script, `ON` will be available by default (no import needed) but your IDE doesn't know that, so we import it from `core.jsr223.scope`.  
`ItemStateChangedEvent.getItemState()` will return an instance of `org.openhab.core.types.State`.  
`ON` is a subclass of `State` so we can compare directly with the state from the event.

### In a Library

```python
import typing as t

if t.TYPE_CHECKING:
    pass
```

## Tips and Tricks

### Prevent Warnings for `basestring` and `unicode`

```python
if t.TYPE_CHECKING:
    basestring = str
    unicode = str
else:
    basestring = basestring  # type: ignore # pylint: disable=self-assigning-variable
    unicode = unicode  # type: ignore # pylint: disable=self-assigning-variable
```
