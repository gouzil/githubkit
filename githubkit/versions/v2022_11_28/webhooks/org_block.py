"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Annotated, Union
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import WebhookOrgBlockBlocked, WebhookOrgBlockUnblocked

Event: TypeAlias = Annotated[
    Union[
        WebhookOrgBlockBlocked,
        WebhookOrgBlockUnblocked,
    ],
    Field(discriminator="action"),
]

OrgBlockEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "blocked": WebhookOrgBlockBlocked,
    "unblocked": WebhookOrgBlockUnblocked,
}

org_block_action_types = action_types

__all__ = ("Event", "OrgBlockEvent", "action_types", "org_block_action_types")
