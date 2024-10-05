"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookWorkflowJobCompletedPropWorkflowJobAllof1Type(TypedDict):
    """WebhookWorkflowJobCompletedPropWorkflowJobAllof1"""

    check_run_url: NotRequired[str]
    completed_at: NotRequired[str]
    conclusion: Literal[
        "success",
        "failure",
        "skipped",
        "cancelled",
        "action_required",
        "neutral",
        "timed_out",
    ]
    created_at: NotRequired[str]
    head_sha: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    labels: NotRequired[List[Union[str, None]]]
    name: NotRequired[str]
    node_id: NotRequired[str]
    run_attempt: NotRequired[int]
    run_id: NotRequired[int]
    run_url: NotRequired[str]
    runner_group_id: NotRequired[Union[int, None]]
    runner_group_name: NotRequired[Union[str, None]]
    runner_id: NotRequired[Union[int, None]]
    runner_name: NotRequired[Union[str, None]]
    started_at: NotRequired[str]
    status: NotRequired[str]
    head_branch: NotRequired[Union[str, None]]
    workflow_name: NotRequired[Union[str, None]]
    steps: NotRequired[
        List[
            Union[
                WebhookWorkflowJobCompletedPropWorkflowJobAllof1PropStepsItemsType, None
            ]
        ]
    ]
    url: NotRequired[str]


class WebhookWorkflowJobCompletedPropWorkflowJobAllof1PropStepsItemsType(TypedDict):
    """WebhookWorkflowJobCompletedPropWorkflowJobAllof1PropStepsItems"""


__all__ = (
    "WebhookWorkflowJobCompletedPropWorkflowJobAllof1Type",
    "WebhookWorkflowJobCompletedPropWorkflowJobAllof1PropStepsItemsType",
)
