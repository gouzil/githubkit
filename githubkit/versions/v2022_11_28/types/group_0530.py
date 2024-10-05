"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0397 import WebhooksChangesType
from .group_0378 import EnterpriseWebhooksType
from .group_0379 import SimpleInstallationType
from .group_0381 import RepositoryWebhooksType
from .group_0396 import WebhooksIssueCommentType
from .group_0380 import OrganizationSimpleWebhooksType
from .group_0531 import WebhookIssueCommentEditedPropIssueType


class WebhookIssueCommentEditedType(TypedDict):
    """issue_comment edited event"""

    action: Literal["edited"]
    changes: WebhooksChangesType
    comment: WebhooksIssueCommentType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssueCommentEditedPropIssueType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookIssueCommentEditedType",)
