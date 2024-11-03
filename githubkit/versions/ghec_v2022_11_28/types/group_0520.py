"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0433 import WebhooksUserType
from .group_0420 import EnterpriseWebhooksType
from .group_0421 import SimpleInstallationType
from .group_0423 import RepositoryWebhooksType
from .group_0422 import OrganizationSimpleWebhooksType


class WebhookDeploymentReviewRequestedType(TypedDict):
    """WebhookDeploymentReviewRequested"""

    action: Literal["requested"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    environment: str
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    repository: RepositoryWebhooksType
    requestor: Union[WebhooksUserType, None]
    reviewers: List[WebhookDeploymentReviewRequestedPropReviewersItemsType]
    sender: SimpleUserType
    since: str
    workflow_job_run: WebhookDeploymentReviewRequestedPropWorkflowJobRunType
    workflow_run: Union[WebhookDeploymentReviewRequestedPropWorkflowRunType, None]


class WebhookDeploymentReviewRequestedPropWorkflowJobRunType(TypedDict):
    """WebhookDeploymentReviewRequestedPropWorkflowJobRun"""

    conclusion: None
    created_at: str
    environment: str
    html_url: str
    id: int
    name: Union[str, None]
    status: str
    updated_at: str


class WebhookDeploymentReviewRequestedPropReviewersItemsType(TypedDict):
    """WebhookDeploymentReviewRequestedPropReviewersItems"""

    reviewer: NotRequired[
        Union[WebhookDeploymentReviewRequestedPropReviewersItemsPropReviewerType, None]
    ]
    type: NotRequired[Literal["User", "Team"]]


class WebhookDeploymentReviewRequestedPropReviewersItemsPropReviewerType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: NotRequired[str]
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookDeploymentReviewRequestedPropWorkflowRunType(TypedDict):
    """Deployment Workflow Run"""

    actor: Union[WebhookDeploymentReviewRequestedPropWorkflowRunPropActorType, None]
    artifacts_url: NotRequired[str]
    cancel_url: NotRequired[str]
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: NotRequired[str]
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
        ],
    ]
    created_at: datetime
    event: str
    head_branch: str
    head_commit: NotRequired[
        Union[WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadCommitType, None]
    ]
    head_repository: NotRequired[
        WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadRepositoryType
    ]
    head_sha: str
    html_url: str
    id: int
    jobs_url: NotRequired[str]
    logs_url: NotRequired[str]
    name: str
    node_id: str
    path: str
    previous_attempt_url: NotRequired[Union[str, None]]
    pull_requests: List[
        WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsType
    ]
    referenced_workflows: NotRequired[
        Union[
            List[
                WebhookDeploymentReviewRequestedPropWorkflowRunPropReferencedWorkflowsItemsType
            ],
            None,
        ]
    ]
    repository: NotRequired[
        WebhookDeploymentReviewRequestedPropWorkflowRunPropRepositoryType
    ]
    rerun_url: NotRequired[str]
    run_attempt: int
    run_number: int
    run_started_at: datetime
    status: Literal[
        "requested", "in_progress", "completed", "queued", "waiting", "pending"
    ]
    triggering_actor: Union[
        WebhookDeploymentReviewRequestedPropWorkflowRunPropTriggeringActorType, None
    ]
    updated_at: datetime
    url: str
    workflow_id: int
    workflow_url: NotRequired[str]
    display_title: str


class WebhookDeploymentReviewRequestedPropWorkflowRunPropActorType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadCommitType(TypedDict):
    """WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadCommit"""


class WebhookDeploymentReviewRequestedPropWorkflowRunPropReferencedWorkflowsItemsType(
    TypedDict
):
    """WebhookDeploymentReviewRequestedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str
    ref: NotRequired[str]
    sha: str


class WebhookDeploymentReviewRequestedPropWorkflowRunPropTriggeringActorType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadRepositoryType(TypedDict):
    """WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadRepository"""

    archive_url: NotRequired[str]
    assignees_url: NotRequired[str]
    blobs_url: NotRequired[str]
    branches_url: NotRequired[str]
    collaborators_url: NotRequired[str]
    comments_url: NotRequired[str]
    commits_url: NotRequired[str]
    compare_url: NotRequired[str]
    contents_url: NotRequired[str]
    contributors_url: NotRequired[str]
    deployments_url: NotRequired[str]
    description: NotRequired[Union[str, None]]
    downloads_url: NotRequired[str]
    events_url: NotRequired[str]
    fork: NotRequired[bool]
    forks_url: NotRequired[str]
    full_name: NotRequired[str]
    git_commits_url: NotRequired[str]
    git_refs_url: NotRequired[str]
    git_tags_url: NotRequired[str]
    hooks_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    issue_comment_url: NotRequired[str]
    issue_events_url: NotRequired[str]
    issues_url: NotRequired[str]
    keys_url: NotRequired[str]
    labels_url: NotRequired[str]
    languages_url: NotRequired[str]
    merges_url: NotRequired[str]
    milestones_url: NotRequired[str]
    name: NotRequired[str]
    node_id: NotRequired[str]
    notifications_url: NotRequired[str]
    owner: NotRequired[
        WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadRepositoryPropOwnerType
    ]
    private: NotRequired[bool]
    pulls_url: NotRequired[str]
    releases_url: NotRequired[str]
    stargazers_url: NotRequired[str]
    statuses_url: NotRequired[str]
    subscribers_url: NotRequired[str]
    subscription_url: NotRequired[str]
    tags_url: NotRequired[str]
    teams_url: NotRequired[str]
    trees_url: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadRepositoryPropOwnerType(
    TypedDict
):
    """WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadRepositoryPropOwner"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookDeploymentReviewRequestedPropWorkflowRunPropRepositoryType(TypedDict):
    """WebhookDeploymentReviewRequestedPropWorkflowRunPropRepository"""

    archive_url: NotRequired[str]
    assignees_url: NotRequired[str]
    blobs_url: NotRequired[str]
    branches_url: NotRequired[str]
    collaborators_url: NotRequired[str]
    comments_url: NotRequired[str]
    commits_url: NotRequired[str]
    compare_url: NotRequired[str]
    contents_url: NotRequired[str]
    contributors_url: NotRequired[str]
    deployments_url: NotRequired[str]
    description: NotRequired[Union[str, None]]
    downloads_url: NotRequired[str]
    events_url: NotRequired[str]
    fork: NotRequired[bool]
    forks_url: NotRequired[str]
    full_name: NotRequired[str]
    git_commits_url: NotRequired[str]
    git_refs_url: NotRequired[str]
    git_tags_url: NotRequired[str]
    hooks_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    issue_comment_url: NotRequired[str]
    issue_events_url: NotRequired[str]
    issues_url: NotRequired[str]
    keys_url: NotRequired[str]
    labels_url: NotRequired[str]
    languages_url: NotRequired[str]
    merges_url: NotRequired[str]
    milestones_url: NotRequired[str]
    name: NotRequired[str]
    node_id: NotRequired[str]
    notifications_url: NotRequired[str]
    owner: NotRequired[
        WebhookDeploymentReviewRequestedPropWorkflowRunPropRepositoryPropOwnerType
    ]
    private: NotRequired[bool]
    pulls_url: NotRequired[str]
    releases_url: NotRequired[str]
    stargazers_url: NotRequired[str]
    statuses_url: NotRequired[str]
    subscribers_url: NotRequired[str]
    subscription_url: NotRequired[str]
    tags_url: NotRequired[str]
    teams_url: NotRequired[str]
    trees_url: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentReviewRequestedPropWorkflowRunPropRepositoryPropOwnerType(
    TypedDict
):
    """WebhookDeploymentReviewRequestedPropWorkflowRunPropRepositoryPropOwner"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsType(
    TypedDict
):
    """Check Run Pull Request"""

    base: (
        WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropBaseType
    )
    head: (
        WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropHeadType
    )
    id: int
    number: int
    url: str


class WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookDeploymentReviewRequestedType",
    "WebhookDeploymentReviewRequestedPropWorkflowJobRunType",
    "WebhookDeploymentReviewRequestedPropReviewersItemsType",
    "WebhookDeploymentReviewRequestedPropReviewersItemsPropReviewerType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropActorType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadCommitType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropReferencedWorkflowsItemsType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropTriggeringActorType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadRepositoryType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropHeadRepositoryPropOwnerType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropRepositoryType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropRepositoryPropOwnerType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropBaseType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropHeadType",
    "WebhookDeploymentReviewRequestedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType",
)
