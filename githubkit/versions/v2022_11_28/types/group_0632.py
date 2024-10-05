"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0414 import ProjectsV2ItemType
from .group_0379 import SimpleInstallationType
from .group_0380 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ItemCreatedType(TypedDict):
    """Projects v2 Item Created Event"""

    action: Literal["created"]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserType


__all__ = ("WebhookProjectsV2ItemCreatedType",)
