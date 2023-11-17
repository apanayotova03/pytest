import pprint
import reprlib
from typing import Any
from typing import Dict
from typing import IO
from typing import Optional

from .pprint import PrettyPrinter  # type: ignore


def _try_repr_or_str(obj: object) -> str:
    try:
        return repr(obj)
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:
        return f'{type(obj).__name__}("{obj}")'


def _format_repr_exception(exc: BaseException, obj: object) -> str:
    try:
        exc_info = _try_repr_or_str(exc)
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException as exc:
        exc_info = f"unpresentable exception ({_try_repr_or_str(exc)})"
    return "<[{} raised in repr()] {} object at 0x{:x}>".format(
        exc_info, type(obj).__name__, id(obj)
    )


def _ellipsize(s: str, maxsize: int) -> str:
    if len(s) > maxsize:
        i = max(0, (maxsize - 3) // 2)
        j = max(0, maxsize - 3 - i)
        return s[:i] + "..." + s[len(s) - j :]
    return s


class SafeRepr(reprlib.Repr):
    """
    repr.Repr that limits the resulting size of repr() and includes
    information on exceptions raised during the call.
    """

    def __init__(self, maxsize: Optional[int], use_ascii: bool = False) -> None:
        """
        :param maxsize:
            If not None, will truncate the resulting repr to that specific size, using ellipsis
            somewhere in the middle to hide the extra text.
            If None, will not impose any size limits on the returning repr.
        """
        super().__init__()
        # ``maxstring`` is used by the superclass, and needs to be an int; using a
        # very large number in case maxsize is None, meaning we want to disable
        # truncation.
        self.maxstring = maxsize if maxsize is not None else 1_000_000_000
        self.maxsize = maxsize
        self.use_ascii = use_ascii

    def repr(self, x: object) -> str:
        try:
            if self.use_ascii:
                s = ascii(x)
            else:
                s = super().repr(x)

        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as exc:
            s = _format_repr_exception(exc, x)
        if self.maxsize is not None:
            s = _ellipsize(s, self.maxsize)
        return s

    def repr_instance(self, x: object, level: int) -> str:
        try:
            s = repr(x)
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as exc:
            s = _format_repr_exception(exc, x)
        if self.maxsize is not None:
            s = _ellipsize(s, self.maxsize)
        return s


def safeformat(obj: object) -> str:
    """Return a pretty printed string for the given object.

    Failing __repr__ functions of user instances will be represented
    with a short exception info.
    """
    try:
        return pprint.pformat(obj)
    except Exception as exc:
        return _format_repr_exception(exc, obj)


# Maximum size of overall repr of objects to display during assertion errors.
DEFAULT_REPR_MAX_SIZE = 240


def saferepr(
    obj: object, maxsize: Optional[int] = DEFAULT_REPR_MAX_SIZE, use_ascii: bool = False
) -> str:
    """Return a size-limited safe repr-string for the given object.

    Failing __repr__ functions of user instances will be represented
    with a short exception info and 'saferepr' generally takes
    care to never raise exceptions itself.

    This function is a wrapper around the Repr/reprlib functionality of the
    stdlib.
    """

    return SafeRepr(maxsize, use_ascii).repr(obj)


def saferepr_unlimited(obj: object, use_ascii: bool = True) -> str:
    """Return an unlimited-size safe repr-string for the given object.

    As with saferepr, failing __repr__ functions of user instances
    will be represented with a short exception info.

    This function is a wrapper around simple repr.

    Note: a cleaner solution would be to alter ``saferepr``this way
    when maxsize=None, but that might affect some other code.
    """
    try:
        if use_ascii:
            return ascii(obj)
        return repr(obj)
    except Exception as exc:
        return _format_repr_exception(exc, obj)


class AlwaysDispatchingPrettyPrinter(PrettyPrinter):
    """PrettyPrinter that always dispatches (regardless of width)."""

    def _format(
        self,
        object: object,
        stream: IO[str],
        indent: int,
        allowance: int,
        context: Dict[int, Any],
        level: int,
    ) -> None:
        # Type ignored because _dispatch is private.
        p = self._dispatch.get(type(object).__repr__, None)  # type: ignore[attr-defined]

        objid = id(object)
        if objid in context or p is None:
            # Type ignored because _format is private.
            super()._format(  # type: ignore[misc]
                object,
                stream,
                indent,
                allowance,
                context,
                level,
            )
            return

        context[objid] = 1
        p(self, object, stream, indent, allowance, context, level + 1)
        del context[objid]


def _pformat_dispatch(
    object: object,
    indent: int = 1,
    width: int = 80,
    depth: Optional[int] = None,
    *,
    compact: bool = False,
) -> str:
    return AlwaysDispatchingPrettyPrinter(  # type: ignore
        indent=indent, width=width, depth=depth, compact=compact
    ).pformat(object)
