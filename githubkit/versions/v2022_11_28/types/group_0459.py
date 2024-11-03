"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0383 import EnterpriseWebhooksType
from .group_0384 import SimpleInstallationType
from .group_0385 import OrganizationSimpleWebhooksType


class WebhookCustomPropertyDeletedType(TypedDict):
    """custom property deleted event"""

    action: Literal["deleted"]
    definition: WebhookCustomPropertyDeletedPropDefinitionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    sender: NotRequired[SimpleUserType]


class WebhookCustomPropertyDeletedPropDefinitionType(TypedDict):
    """WebhookCustomPropertyDeletedPropDefinition"""

    property_name: str


__all__ = (
    "WebhookCustomPropertyDeletedType",
    "WebhookCustomPropertyDeletedPropDefinitionType",
)
