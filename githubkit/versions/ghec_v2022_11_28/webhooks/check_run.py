"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Annotated, Union
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookCheckRunCompleted,
    WebhookCheckRunCreated,
    WebhookCheckRunRequestedAction,
    WebhookCheckRunRerequested,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookCheckRunCompleted,
        WebhookCheckRunCreated,
        WebhookCheckRunRequestedAction,
        WebhookCheckRunRerequested,
    ],
    Field(discriminator="action"),
]

CheckRunEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "completed": WebhookCheckRunCompleted,
    "created": WebhookCheckRunCreated,
    "requested_action": WebhookCheckRunRequestedAction,
    "rerequested": WebhookCheckRunRerequested,
}

check_run_action_types = action_types

__all__ = ("CheckRunEvent", "Event", "action_types", "check_run_action_types")
