# Actions

Thing Actions are a bit harder to type in Python as the stub files cannot be generated automatically.
All of the stubs for Thing Actions must be created by hand by users.

## Typing Thing Actions

Thing Actions are dynamic so they must be typed manually because there is no way in your IDE to know what `actions.get()` will return.
If there is a stub file available for the Thing Action in question you can use it like this:

```python
if t.TYPE_CHECKING:
    from core.jsr223.scope import actions
    from actions.telegram import TelegramAction  # pylint: disable=import-error

telegram = actions.get("telegram", "telegram:telegramBot:BOT_ID")  # type: TelegramAction
```

## Creating and Submitting Thing Actions

Thing Actions should be put in a file with the same name as the binding in `Stubs/openHAB/{VERSION}/actions/`.
In this file should be a class for each type of Thing that has Actions available in the binding.
This class should have a name like `TelegramAction` such as to be clear about what it is and avoid naming conflicts.
If the stub applies to multiple versions of openHAB the file should be duplicated in each version folder that it works for.
