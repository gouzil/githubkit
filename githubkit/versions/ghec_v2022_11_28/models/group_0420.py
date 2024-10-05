"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ExemptionResponse(GitHubModel):
    """Exemption response

    A response to an exemption request by a delegated bypasser.
    """

    id: Missing[int] = Field(
        default=UNSET, description="The ID of the exemption response."
    )
    reviewer_id: Missing[int] = Field(
        default=UNSET,
        description="The ID of the user who reviewed the exemption request.",
    )
    reviewer_login: Missing[str] = Field(
        default=UNSET,
        description="The login of the user who reviewed the exemption request.",
    )
    status: Missing[Literal["approved", "rejected", "dismissed"]] = Field(
        default=UNSET, description="The status of the exemption response."
    )
    created_at: Missing[datetime] = Field(
        default=UNSET,
        description="The date and time the exemption request was created.",
    )


model_rebuild(ExemptionResponse)

__all__ = ("ExemptionResponse",)
