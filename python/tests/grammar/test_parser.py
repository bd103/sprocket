from sprocket_bio.grammar import SyntaxKind, Span
from sprocket_bio.grammar.parser import Event

import pytest


def test_event_new() -> None:
    with pytest.raises(TypeError, match="cannot create"):
        Event()


def test_event_abandoned() -> None:
    abandoned = Event.abandoned()

    assert isinstance(abandoned, Event.NodeStarted)
    # Note: `abandoned.kind is SyntaxKind.ABANDONED` fails here due to the nature of how
    # `abandoned.kind` is created.
    assert abandoned.kind == SyntaxKind.ABANDONED
    assert abandoned.forward_parent is None


def test_event_node_started_getters_setters() -> None:
    node_started = Event.NodeStarted(SyntaxKind.CALL_STATEMENT_NODE, 2)

    assert node_started.kind is SyntaxKind.CALL_STATEMENT_NODE
    assert node_started.forward_parent == 2

    node_started.kind = SyntaxKind.ACCESS_EXPR_NODE
    node_started.forward_parent = None

    assert node_started.kind is SyntaxKind.ACCESS_EXPR_NODE
    assert node_started.forward_parent is None


def test_event_node_started_eq() -> None:
    assert Event.NodeStarted(SyntaxKind.ROOT_NODE, 1) == Event.NodeStarted(
        SyntaxKind.ROOT_NODE, 1
    )
    assert Event.NodeStarted(SyntaxKind.ROOT_NODE, 1) != Event.NodeStarted(
        SyntaxKind.IF_EXPR_NODE, 1
    )
    assert Event.NodeStarted(SyntaxKind.ROOT_NODE, 1) != Event.NodeStarted(
        SyntaxKind.ROOT_NODE, None
    )
    assert Event.NodeStarted(SyntaxKind.ROOT_NODE, 1) != Event.NodeFinished()


def test_event_node_started_repr() -> None:
    assert "Event.NodeStarted" in repr(
        Event.NodeStarted(SyntaxKind.PRIMITIVE_TYPE_NODE, None)
    )


def test_event_node_finished_eq() -> None:
    assert Event.NodeFinished() == Event.NodeFinished()
    assert Event.NodeFinished() != Event.NodeStarted(SyntaxKind.ROOT_NODE, None)


def test_event_node_finished_repr() -> None:
    assert "Event.NodeFinished" in repr(Event.NodeFinished())


def test_event_token_getters_setters() -> None:
    token = Event.Token(SyntaxKind.AS_KEYWORD, Span(0, 10))

    assert token.kind is SyntaxKind.AS_KEYWORD
    assert token.span == Span(0, 10)

    token.kind = SyntaxKind.PERCENT
    token.span = Span(2, 3)

    assert token.kind is SyntaxKind.PERCENT
    assert token.span == Span(2, 3)


def test_event_token_eq() -> None:
    assert Event.Token(SyntaxKind.AS_KEYWORD, Span(0, 10)) == Event.Token(
        SyntaxKind.AS_KEYWORD, Span(0, 10)
    )
    assert Event.Token(SyntaxKind.AS_KEYWORD, Span(0, 10)) != Event.Token(
        SyntaxKind.AFTER_KEYWORD, Span(0, 10)
    )
    assert Event.Token(SyntaxKind.AS_KEYWORD, Span(0, 10)) != Event.Token(
        SyntaxKind.AS_KEYWORD, Span(0, 3)
    )
    assert Event.Token(SyntaxKind.AS_KEYWORD, Span(0, 10)) != Event.NodeFinished()


def test_event_token_repr() -> None:
    assert "Event.Token" in repr(Event.Token(SyntaxKind.IF_KEYWORD, Span(0, 0)))
