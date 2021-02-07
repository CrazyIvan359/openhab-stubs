# Reference

Here you will find information on commonly used things in openHAB.

## Item Types

Item types are found in `org.openhab.core.library.items` and are subclassed from `org.openhab.core.items.GenericItem`.

* `CallItem`
* `ContactItem`
* `DateTimeItem`
* `ImageItem`
* `LocationItem`
* `NumberItem`
* `PlayerItem`
* `RollershutterItem`
* `StringItem`
* `SwitchItem`
* `DimmerItem`
* `ColorItem`

The Group Item type `GroupItem` is special and is found in `org.openhab.core.items`.

## State and Command Types

Item State and Command types are found in `org.openhab.core.library.types` and are subclassed from `org.openhab.core.types.State` or `org.openhab.core.types.Command` or both.
These are mostly provided in the `DefaultScope` for scripts and can be imported from `core.jsr223.scope` for typing purposes in scripts or for runtime use in libraries.

|          Type           | State | Command |
| :---------------------- | :---: | :-----: |
| `DateTimeType`          |   ✔   |    ✔    |
| `DecimalType`           |   ✔   |    ✔    |
| `IncreaseDecreaseType`  |       |    ✔    |
| `NextPreviousType`      |       |    ✔    |
| `OnOffType`             |   ✔   |    ✔    |
| `OpenClosedType`        |   ✔   |    ✔    |
| `PlayPauseType`         |   ✔   |    ✔    |
| `PointType`             |   ✔   |    ✔    |
| `QuantityType`          |   ✔   |    ✔    |
| `RawType`               |   ✔   |         |
| `RewindFastforwardType` |   ✔   |    ✔    |
| `StopMoveType`          |       |    ✔    |
| `StringListType`        |   ✔   |    ✔    |
| `StringType`            |   ✔   |    ✔    |
| `UpDownType`            |   ✔   |    ✔    |
| `PercentType`           |   ✔   |    ✔    |
| `HSBType`               |   ✔   |    ✔    |

There are also some core types in `org.openhab.core.types`.

|     Type      | State | Command |
| :------------ | :---: | :-----: |
| `RefreshType` |       |    ✔    |
| `UnDefType`   |   ✔   |         |

## Rule Event Types

The `event` parameter in rule functions will always be a subclass of `org.openhab.core.events.AbstractEvent` (except if the rule was run from the UI, in which case `event` will be `null`/`None`).
The tables below list most of the possible event classes and the rule triggers that generate them.

### Item Events

These events are all found in `org.openhab.core.items.events`.

|          Event Type          |        Parent Class         |              Triggers              |
| :--------------------------- | :-------------------------- | :--------------------------------- |
| `ItemStateChangedEvent`      | `ItemEvent`                 | `"Item myItem changed"`            |
| `ItemStateEvent`             | `ItemEvent`                 | `"Item myItem received udpate"`    |
| `ItemCommandEvent`           | `ItemEvent`                 | `"Item myItem received command"`   |
| `GroupItemStateChangedEvent` | `ItemStateChangedEvent`     | openHAB native *Member of* trigger |
| `ItemAddedEvent`             | `AbstractItemRegistryEvent` | `"Item added"`                     |
| `ItemRemovedEvent`           | `AbstractItemRegistryEvent` | `"Item removed"`                   |
| `ItemUpdatedEvent`           | `AbstractItemRegistryEvent` | `"Item updated"`                   |

### Thing Events

These events are all found in `org.openhab.core.thing.events`.

|          Event Type           |         Parent Class         |                     Triggers                     |
| :---------------------------- | :--------------------------- | :----------------------------------------------- |
| `ChannelTriggeredEvent`       | `AbstractEvent`              | `"Channel binding:thing:myChannel triggered"`    |
| `ThingStatusInfoChangedEvent` | `AbstractEvent`              | `"Thing binding:thing:myThing changed"`          |
| `ThingStatusInfoEvent`        | `AbstractEvent`              | `"Thing binding:thing:myThing received updated"` |
| `ThingAddedEvent`             | `AbstractThingRegistryEvent` | `"Thing added"`                                  |
| `ThingRemovedEvent`           | `AbstractThingRegistryEvent` | `"Thing removed"`                                |
| `ThingUpdatedEvent`           | `AbstractThingRegistryEvent` | `"Thing updated"`                                |

### Other Events

|                    Event Type                    | Triggers |
| :----------------------------------------------- | :------- |
| `org.openhab.core.events.system.StartlevelEvent` |          |
