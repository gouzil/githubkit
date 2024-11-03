"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0404 import WebhooksMilestoneType
from .group_0383 import EnterpriseWebhooksType
from .group_0384 import SimpleInstallationType
from .group_0386 import RepositoryWebhooksType
from .group_0385 import OrganizationSimpleWebhooksType


class WebhookMilestoneEditedType(TypedDict):
    """milestone edited event"""

    action: Literal["edited"]
    changes: WebhookMilestoneEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    milestone: WebhooksMilestoneType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookMilestoneEditedPropChangesType(TypedDict):
    """WebhookMilestoneEditedPropChanges

    The changes to the milestone if the action was `edited`.
    """

    description: NotRequired[WebhookMilestoneEditedPropChangesPropDescriptionType]
    due_on: NotRequired[WebhookMilestoneEditedPropChangesPropDueOnType]
    title: NotRequired[WebhookMilestoneEditedPropChangesPropTitleType]


class WebhookMilestoneEditedPropChangesPropDescriptionType(TypedDict):
    """WebhookMilestoneEditedPropChangesPropDescription"""

    from_: str


class WebhookMilestoneEditedPropChangesPropDueOnType(TypedDict):
    """WebhookMilestoneEditedPropChangesPropDueOn"""

    from_: str


class WebhookMilestoneEditedPropChangesPropTitleType(TypedDict):
    """WebhookMilestoneEditedPropChangesPropTitle"""

    from_: str


__all__ = (
    "WebhookMilestoneEditedType",
    "WebhookMilestoneEditedPropChangesType",
    "WebhookMilestoneEditedPropChangesPropDescriptionType",
    "WebhookMilestoneEditedPropChangesPropDueOnType",
    "WebhookMilestoneEditedPropChangesPropTitleType",
)
