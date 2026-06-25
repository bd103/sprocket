from sprocket_bio.grammar import SyntaxKind, Span
import typing

class Event:
    @typing.final
    class NodeStarted(Event):
        kind: SyntaxKind
        forward_parent: int | None

        def __new__(
            cls, kind: SyntaxKind, forward_parent: int | None
        ) -> Event.NodeStarted: ...

    @typing.final
    class NodeFinished(Event):
        def __new__(cls) -> Event.NodeFinished: ...

    @typing.final
    class Token(Event):
        kind: SyntaxKind
        span: Span

        def __new__(cls, kind: SyntaxKind, span: Span) -> Event.Token: ...

    # `Event` cannot be constructed directly, you must construct one of its subclasses.
    def __new__(cls) -> typing.NoReturn: ...
    @classmethod
    def abandoned(cls) -> Event.NodeStarted: ...

__all__ = ["Event"]
