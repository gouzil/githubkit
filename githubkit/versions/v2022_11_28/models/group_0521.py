"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookIssueCommentCreatedPropIssueAllof1(GitHubModel):
    """WebhookIssueCommentCreatedPropIssueAllof1"""

    active_lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    assignee: Union[WebhookIssueCommentCreatedPropIssueAllof1PropAssignee, None] = (
        Field(title="User")
    )
    assignees: Missing[
        List[Union[WebhookIssueCommentCreatedPropIssueAllof1PropAssigneesItems, None]]
    ] = Field(default=UNSET)
    author_association: Missing[str] = Field(default=UNSET)
    body: Missing[Union[str, None]] = Field(default=UNSET)
    closed_at: Missing[Union[str, None]] = Field(default=UNSET)
    comments: Missing[int] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    labels: List[WebhookIssueCommentCreatedPropIssueAllof1PropLabelsItems] = Field()
    labels_url: Missing[str] = Field(default=UNSET)
    locked: bool = Field()
    milestone: Missing[
        Union[WebhookIssueCommentCreatedPropIssueAllof1PropMilestone, None]
    ] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    number: Missing[int] = Field(default=UNSET)
    performed_via_github_app: Missing[
        Union[WebhookIssueCommentCreatedPropIssueAllof1PropPerformedViaGithubApp, None]
    ] = Field(default=UNSET)
    reactions: Missing[WebhookIssueCommentCreatedPropIssueAllof1PropReactions] = Field(
        default=UNSET
    )
    repository_url: Missing[str] = Field(default=UNSET)
    state: Literal["open", "closed"] = Field(
        description="State of the issue; either 'open' or 'closed'"
    )
    timeline_url: Missing[str] = Field(default=UNSET)
    title: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user: Missing[WebhookIssueCommentCreatedPropIssueAllof1PropUser] = Field(
        default=UNSET
    )


class WebhookIssueCommentCreatedPropIssueAllof1PropAssignee(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookIssueCommentCreatedPropIssueAllof1PropAssigneesItems(GitHubModel):
    """WebhookIssueCommentCreatedPropIssueAllof1PropAssigneesItems"""


class WebhookIssueCommentCreatedPropIssueAllof1PropLabelsItems(GitHubModel):
    """Label"""

    color: str = Field(
        description="6-character hex code, without the leading #, identifying the color"
    )
    default: bool = Field()
    description: Union[str, None] = Field()
    id: int = Field()
    name: str = Field(description="The name of the label.")
    node_id: str = Field()
    url: str = Field(description="URL for the label")


class WebhookIssueCommentCreatedPropIssueAllof1PropMilestone(GitHubModel):
    """WebhookIssueCommentCreatedPropIssueAllof1PropMilestone"""


class WebhookIssueCommentCreatedPropIssueAllof1PropPerformedViaGithubApp(GitHubModel):
    """WebhookIssueCommentCreatedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssueCommentCreatedPropIssueAllof1PropReactions(GitHubModel):
    """WebhookIssueCommentCreatedPropIssueAllof1PropReactions"""

    plus_one: Missing[int] = Field(default=UNSET, alias="+1")
    minus_one: Missing[int] = Field(default=UNSET, alias="-1")
    confused: Missing[int] = Field(default=UNSET)
    eyes: Missing[int] = Field(default=UNSET)
    heart: Missing[int] = Field(default=UNSET)
    hooray: Missing[int] = Field(default=UNSET)
    laugh: Missing[int] = Field(default=UNSET)
    rocket: Missing[int] = Field(default=UNSET)
    total_count: Missing[int] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookIssueCommentCreatedPropIssueAllof1PropUser(GitHubModel):
    """WebhookIssueCommentCreatedPropIssueAllof1PropUser"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssueCommentCreatedPropIssueAllof1)
model_rebuild(WebhookIssueCommentCreatedPropIssueAllof1PropAssignee)
model_rebuild(WebhookIssueCommentCreatedPropIssueAllof1PropAssigneesItems)
model_rebuild(WebhookIssueCommentCreatedPropIssueAllof1PropLabelsItems)
model_rebuild(WebhookIssueCommentCreatedPropIssueAllof1PropMilestone)
model_rebuild(WebhookIssueCommentCreatedPropIssueAllof1PropPerformedViaGithubApp)
model_rebuild(WebhookIssueCommentCreatedPropIssueAllof1PropReactions)
model_rebuild(WebhookIssueCommentCreatedPropIssueAllof1PropUser)

__all__ = (
    "WebhookIssueCommentCreatedPropIssueAllof1",
    "WebhookIssueCommentCreatedPropIssueAllof1PropAssignee",
    "WebhookIssueCommentCreatedPropIssueAllof1PropAssigneesItems",
    "WebhookIssueCommentCreatedPropIssueAllof1PropLabelsItems",
    "WebhookIssueCommentCreatedPropIssueAllof1PropMilestone",
    "WebhookIssueCommentCreatedPropIssueAllof1PropPerformedViaGithubApp",
    "WebhookIssueCommentCreatedPropIssueAllof1PropReactions",
    "WebhookIssueCommentCreatedPropIssueAllof1PropUser",
)
