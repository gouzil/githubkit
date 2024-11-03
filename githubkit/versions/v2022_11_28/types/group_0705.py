"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0149 import RepositoryRulesetType
from .group_0383 import EnterpriseWebhooksType
from .group_0384 import SimpleInstallationType
from .group_0386 import RepositoryWebhooksType
from .group_0385 import OrganizationSimpleWebhooksType
from .group_0706 import WebhookRepositoryRulesetEditedPropChangesType


class WebhookRepositoryRulesetEditedType(TypedDict):
    """repository ruleset edited event"""

    action: Literal["edited"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    repository_ruleset: RepositoryRulesetType
    changes: NotRequired[WebhookRepositoryRulesetEditedPropChangesType]
    sender: SimpleUserType


__all__ = ("WebhookRepositoryRulesetEditedType",)
