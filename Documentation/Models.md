# Models

## `uberduck.Voice`

The `uberduck.Voice` class provides details on a text-to-speech voice. A list of this class can be received from the `get_voices` and `get_voices_async` functions.

*Attributes:*

* `architecture (str)`: The architecture of the voice i.e. the engine that was used to make the voice.

* `category (str)`: The category of the voice i.e. where it's from (WWE, SpongeBob etc).

* `controls (bool)`: Whether the voice has controls.

* `display_name (str)`: The display name of the voice i.e. a better formatted name to show to general users.

* `name (str)`: The name of the voice i.e. the name you pass to the API in order for it to recognize which voice you want.

* `model_id (str)`: The model ID of the voice. This is not a unique identification, the name is.

* `memberships (list)`: The memberships of the voice. If this list is not empty, it is a list of `uberduck.Membership` objects.

* `is_private (bool)`: Whether the voice is private.

* `contributors (list)`: The contributors' names of the voice.

*Magic methods:*

* `__str__`: Returns a string representation of the Voice object in the format `Voice: Architecture - {architecture}, Category - {category}, Controls - {controls}, Display Name - {display_name}, Name - {name}, Model ID - {model_id}, Memberships - {memberships}, Is Private - {is_private}, Contributors - {contributors}`.
    
* `__repr__`: Returns a string representation of the Voice object in the format `<Voice architecture='{architecture}' category='{category}' controls='{controls}' display_name='{display_name}' name='{name}' model_id='{model_id}' memberships='{memberships}' is_private='{is_private}' contributors='{contributors}'>`.

This class is read-only.

## `uberduck.Membership`

This is a model class Membership that represents the membership attribute of a voice.
    
*Attributes:*

* `name (str)`: The name of the membership.

* `id (int)`: The ID of the membership.

*Magic methods:*

* `__str__`: Returns a string representation of the Membership object in the format `Membership: Name - {name}, ID - {id}`.

* `__repr__`: Returns a string representation of the Membership object in the format `<Membership name='{name}' id={id}>`.

This class is read-only.