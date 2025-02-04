"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Annotated, Union
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookWorkflowJobCompleted,
    WebhookWorkflowJobInProgress,
    WebhookWorkflowJobQueued,
    WebhookWorkflowJobWaiting,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookWorkflowJobCompleted,
        WebhookWorkflowJobInProgress,
        WebhookWorkflowJobQueued,
        WebhookWorkflowJobWaiting,
    ],
    Field(discriminator="action"),
]

WorkflowJobEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "completed": WebhookWorkflowJobCompleted,
    "in_progress": WebhookWorkflowJobInProgress,
    "queued": WebhookWorkflowJobQueued,
    "waiting": WebhookWorkflowJobWaiting,
}

workflow_job_action_types = action_types

__all__ = ("Event", "WorkflowJobEvent", "action_types", "workflow_job_action_types")
