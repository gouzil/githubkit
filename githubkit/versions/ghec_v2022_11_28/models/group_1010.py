"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoBranchesBranchProtectionRestrictionsUsersPutBody(GitHubModel):
    """ReposOwnerRepoBranchesBranchProtectionRestrictionsUsersPutBody

    Examples:
        {'users': ['mona']}
    """

    users: List[str] = Field(description="The username for users")


model_rebuild(ReposOwnerRepoBranchesBranchProtectionRestrictionsUsersPutBody)

__all__ = ("ReposOwnerRepoBranchesBranchProtectionRestrictionsUsersPutBody",)
