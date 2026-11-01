"""Esqueletos del modelo conceptual de HelpDesk EDU, sin persistencia."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    name: str
    email: str
    role: str

    def describe(self) -> str:
        return f"{self.name} ({self.role})"


@dataclass
class Comment:
    body: str

    def describe(self) -> str:
        return self.body


@dataclass
class History:
    description: str

    def describe(self) -> str:
        return self.description


@dataclass
class Ticket:
    id: int
    title: str
    requester: User
    technician: User | None = None
    comments: list[Comment] = field(default_factory=list, init=False)
    history: list[History] = field(default_factory=list, init=False)

    def add_comment(self, body: str) -> Comment:
        comment = Comment(body)
        self.comments.append(comment)
        return comment

    def record_event(self, description: str) -> History:
        event = History(description)
        self.history.append(event)
        return event


@dataclass
class Article:
    id: int
    title: str
    author: User

    def describe(self) -> str:
        return self.title
