"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0051 import CopilotSeatDetails


class OrgsOrgCopilotBillingSeatsGetResponse200(GitHubModel):
    """OrgsOrgCopilotBillingSeatsGetResponse200"""

    total_seats: Missing[int] = Field(
        default=UNSET,
        description="Total number of Copilot seats for the organization currently being billed.",
    )
    seats: Missing[List[CopilotSeatDetails]] = Field(default=UNSET)


model_rebuild(OrgsOrgCopilotBillingSeatsGetResponse200)

__all__ = ("OrgsOrgCopilotBillingSeatsGetResponse200",)
