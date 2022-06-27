# Models

## `uberduck.Voice`

The `uberduck.Voice` class provides details on a text-to-speech voice. A list of this class can be received from the `get_voices` and `get_voices_async` functions.

*Attributes:*

* `architecture (str)`: The architecture of the voice i.e. the engine that was used to make the voice.

* `category (str)`: The category of the voice i.e. where it's from (WWE, SpongeBob etc).

* `contributors (list)`: The contributors' names of the voice.

* `controls (bool)`: Whether the voice has controls.

* `display_name (str)`: The display name of the voice i.e. a better formatted name to show to general users.

* `is_active (bool)`: Whether the voice is active or not.
  
* `model_id (str)`: The model ID of the voice. This is not a unique identification, the name is.

* `memberships (list)`: The memberships of the voice. If this list is not empty, it is a list of `uberduck.Membership` objects.

* `is_private (bool)`: Whether the voice is private.

* `name (str)`: The name of the voice i.e. the name you pass to the API in order for it to recognize which voice you want.

* `symbol_set (str)`: The symbol set of the voice.

* `voicemodel_uuid (str)`: The voice model's UUID.

*Magic methods:*

* `__str__`: Returns a string representation of the Voice object in the format `Voice: Architecture - {self.architecture}, Category - {self.category}, Contributors - {self.contributors}, Controls - {self.controls}, Display Name - {self.display_name}, Is Active - {self.is_active},  Model ID - {self.model_id}, Memberships - {self.memberships}, Is Private - {self.is_private}, Name - {self.name}, Symbol Set - {self.symbol_set}, Voice model UUID - {self.voicemodel_uuid}`.
    
* `__repr__`: Returns a string representation of the Voice object in the format `<Voice architecture='{self.architecture}' category='{self.category}' contributors='{self.contributors}' controls='{self.controls}' display_name='{self.display_name}' is_active='{self.is_active}' model_id='{self.model_id}' memberships='{self.memberships}' is_private='{self.is_private}' name='{self.name}' symbol_set='{self.symbol_set}' voicemodel_uuid='{self.voicemodel_uuid}'>`.

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