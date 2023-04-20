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

* `added_at (datetime)`: The date the model was added at.

* `is_primary: (bool)`: Whether the voice is added to the Uberduck.ai site.

* `hifi_gan_vocoder: (str)`: The HIFI-gan vocoder used to improve the voice.

* `ml_model_id: (int)`: The ID of the machine learning model.

* `speaker_id: (Optional[int])`: The ID of the person doing the voice.

* `language: (str)`: The language the voice was trained for.

*Magic methods:*

* `__str__`: Returns a string representation of the Voice object in the format `Voice: Architecture - {architecture}, Category - {category}, Contributors - {contributors}, Controls - {controls}, Display Name - {display_name}, Is Active - {is_active},  Model ID - {model_id}, Memberships - {memberships}, Is Private - {is_private}, Name - {name}, Symbol Set - {symbol_set}, Voice model UUID - {voicemodel_uuid}, Added At - {added_at time in "%a, %B %d %Y, %I:%M:%S %p UTC" strftime format}, Is Primary - {is_primary}, Hifi Gan Vocoder - {hifi_gan_vocoder}, ML Model ID - {ml_model_id}, Speaker ID - {speaker_id}, Language {language}`.
    
* `__repr__`: Returns a string representation of the Voice object in the format `<Voice architecture='{architecture}' category='{category}' contributors='{contributors}' controls='{controls}' display_name='{display_name}' is_active='{is_active}' model_id='{model_id}' memberships='{memberships}' is_private='{is_private}' name='{name}' symbol_set='{symbol_set}' voicemodel_uuid='{voicemodel_uuid}' added_at='{added_at as float timestamp}' is_primary='{is_primary}' hifi_gan_vocoder='{hifi_gan_vocoder}' ml_model_id='{ml_model_id}' speaker_id='{speaker_id}' language='{language}'>`.

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