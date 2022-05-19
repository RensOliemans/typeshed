from typing import Callable, Pattern
from typing_extensions import Literal

_DEFAULT_DELIMITER: str

def emojize(
    string: str,
    use_aliases: bool = ...,
    delimiters: tuple[str, str] = ...,
    variant: Literal["text_type", "emoji_type", None] = ...,
    language: str = ...,
    version: float | int = ...,
    handle_version: str | Callable = ...,
) -> str: ...
def demojize(
    string: str,
    use_aliases: bool = ...,
    delimiters: tuple[str, str] = ...,
    language: str = ...,
    version: float | int = ...,
    handle_version: str | Callable = ...,
) -> str: ...
def replace_emoji(string: str, replace: str | Callable = ..., language: str = ..., version: float | int = ...) -> str: ...
def get_emoji_regexp(language: str = ...) -> Pattern[str]: ...
def emoji_lis(string: str, language: str = ...) -> list[dict[str, int | str]]: ...
def emoji_list(string: str) -> list[dict[str, int | str]]: ...
def distinct_emoji_lis(string: str) -> list[str]: ...
def distinct_emoji_list(string: str) -> list[str]: ...
def emoji_count(string: str) -> int: ...
def version(string: str) -> float | int: ...
