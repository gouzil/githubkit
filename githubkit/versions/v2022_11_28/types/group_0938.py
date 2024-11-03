"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


class ReposOwnerRepoBranchesBranchProtectionRestrictionsAppsPostBodyType(TypedDict):
    """ReposOwnerRepoBranchesBranchProtectionRestrictionsAppsPostBody

    Examples:
        {'apps': ['my-app']}
    """

    apps: List[str]


__all__ = ("ReposOwnerRepoBranchesBranchProtectionRestrictionsAppsPostBodyType",)
