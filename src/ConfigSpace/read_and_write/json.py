from __future__ import annotations

from io import StringIO
from typing import TYPE_CHECKING, Mapping
from typing_extensions import deprecated

from ConfigSpace.configuration_space import ConfigurationSpace

if TYPE_CHECKING:
    from ConfigSpace.read_and_write.dictionary import _Decoder, _Encoder


@deprecated(
    "Please use `space.to_json(path)` directly instead. If you require the json string "
    " directly, pass a `StringIO` object to `space.to_json(buffer)`.",
)
def write(
    space: ConfigurationSpace,
    indent: int = 2,
    encoders: Mapping[type, tuple[str, _Encoder]] | None = None,
) -> str:
    """Create a string representation of a
    :class:`~ConfigSpace.configuration_space.ConfigurationSpace` in json format.
    This string can be written to file.

    .. code:: python

        from ConfigSpace import ConfigurationSpace
        from ConfigSpace.read_and_write import json as cs_json

        cs = ConfigurationSpace({"a": [1, 2, 3]})

        with open('configspace.json', 'w') as f:
            f.write(cs_json.write(cs))

    Parameters
    ----------
    configuration_space : :class:`~ConfigSpace.configuration_space.ConfigurationSpace`
        a configuration space, which should be written to file.
    indent : int
        number of whitespaces to use as indent
    encoders: dict[type, tuple[str, Callable[[Any, encoders], dict]]]
        Additional encoders to include where they key is a type to which the encoder
        applies to and the value is a tuple, where the first element is the type name
        to include in the dictionary and the second element is the encoder function
        which gives back a serializable dictionary.

    Returns
    -------
    str
        String representation of the configuration space,
        which can be written to file
    """
    buffer = StringIO()
    with buffer as f:
        space.to_json(f, indent=indent, encoders=encoders)
        return f.getvalue()


@deprecated(
    "Please use `space.from_json(path)` instead. If you already have the"
    " json string, pass it as `space.from_json(StringIO(jsn))`.",
)
def read(
    jason_string: str,
    decoders: Mapping[str, _Decoder] | None = None,
) -> ConfigurationSpace:
    """Create a configuration space definition from a json string.

    .. code:: python

        from ConfigSpace import ConfigurationSpace
        from ConfigSpace.read_and_write import json as cs_json

        cs = ConfigurationSpace({"a": [1, 2, 3]})

        cs_string = cs_json.write(cs)
        with open('configspace.json', 'w') as f:
             f.write(cs_string)

        with open('configspace.json', 'r') as f:
            json_string = f.read()
            config = cs_json.read(json_string)


    Parameters
    ----------
    jason_string : str
        A json string representing a configuration space definition

    Returns
    -------
    :class:`~ConfigSpace.configuration_space.ConfigurationSpace`
        The deserialized ConfigurationSpace object
    """
    return ConfigurationSpace.from_json(StringIO(jason_string), decoders=decoders)