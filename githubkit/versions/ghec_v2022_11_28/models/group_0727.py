"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0728 import (
    WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersion,
)


class WebhookRegistryPackageUpdatedPropRegistryPackage(GitHubModel):
    """WebhookRegistryPackageUpdatedPropRegistryPackage"""

    created_at: str = Field()
    description: None = Field()
    ecosystem: str = Field()
    html_url: str = Field()
    id: int = Field()
    name: str = Field()
    namespace: str = Field()
    owner: WebhookRegistryPackageUpdatedPropRegistryPackagePropOwner = Field()
    package_type: str = Field()
    package_version: WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersion = Field()
    registry: Union[
        WebhookRegistryPackageUpdatedPropRegistryPackagePropRegistry, None
    ] = Field()
    updated_at: str = Field()


class WebhookRegistryPackageUpdatedPropRegistryPackagePropOwner(GitHubModel):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropOwner"""

    avatar_url: str = Field()
    events_url: str = Field()
    followers_url: str = Field()
    following_url: str = Field()
    gists_url: str = Field()
    gravatar_id: str = Field()
    html_url: str = Field()
    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organizations_url: str = Field()
    received_events_url: str = Field()
    repos_url: str = Field()
    site_admin: bool = Field()
    starred_url: str = Field()
    subscriptions_url: str = Field()
    type: str = Field()
    url: str = Field()
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookRegistryPackageUpdatedPropRegistryPackagePropRegistry(GitHubModel):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropRegistry"""


model_rebuild(WebhookRegistryPackageUpdatedPropRegistryPackage)
model_rebuild(WebhookRegistryPackageUpdatedPropRegistryPackagePropOwner)
model_rebuild(WebhookRegistryPackageUpdatedPropRegistryPackagePropRegistry)

__all__ = (
    "WebhookRegistryPackageUpdatedPropRegistryPackage",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropOwner",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropRegistry",
)
