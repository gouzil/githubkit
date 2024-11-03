"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser
from .group_0384 import SimpleInstallation
from .group_0386 import RepositoryWebhooks
from .group_0385 import OrganizationSimpleWebhooks
from .group_0429 import SecretScanningAlertWebhook


class WebhookSecretScanningAlertLocationCreated(GitHubModel):
    """Secret Scanning Alert Location Created Event"""

    action: Literal["created"] = Field()
    alert: SecretScanningAlertWebhook = Field()
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    location: SecretScanningLocation = Field()
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class SecretScanningLocation(GitHubModel):
    """SecretScanningLocation"""

    type: Missing[
        Literal[
            "commit",
            "wiki_commit",
            "issue_title",
            "issue_body",
            "issue_comment",
            "discussion_title",
            "discussion_body",
            "discussion_comment",
            "pull_request_title",
            "pull_request_body",
            "pull_request_comment",
            "pull_request_review",
            "pull_request_review_comment",
        ]
    ] = Field(
        default=UNSET,
        description="The location type. Because secrets may be found in different types of resources (ie. code, comments, issues, pull requests, discussions), this field identifies the type of resource where the secret was found.",
    )
    details: Missing[
        Union[
            SecretScanningLocationCommit,
            SecretScanningLocationWikiCommit,
            SecretScanningLocationIssueTitle,
            SecretScanningLocationIssueBody,
            SecretScanningLocationIssueComment,
            SecretScanningLocationDiscussionTitle,
            SecretScanningLocationDiscussionBody,
            SecretScanningLocationDiscussionComment,
            SecretScanningLocationPullRequestTitle,
            SecretScanningLocationPullRequestBody,
            SecretScanningLocationPullRequestComment,
            SecretScanningLocationPullRequestReview,
            SecretScanningLocationPullRequestReviewComment,
        ]
    ] = Field(default=UNSET)


class SecretScanningLocationCommit(GitHubModel):
    """SecretScanningLocationCommit

    Represents a 'commit' secret scanning location type. This location type shows
    that a secret was detected inside a commit to a repository.
    """

    path: str = Field(description="The file path in the repository")
    start_line: float = Field(
        description="Line number at which the secret starts in the file"
    )
    end_line: float = Field(
        description="Line number at which the secret ends in the file"
    )
    start_column: float = Field(
        description="The column at which the secret starts within the start line when the file is interpreted as 8BIT ASCII"
    )
    end_column: float = Field(
        description="The column at which the secret ends within the end line when the file is interpreted as 8BIT ASCII"
    )
    blob_sha: str = Field(description="SHA-1 hash ID of the associated blob")
    blob_url: str = Field(description="The API URL to get the associated blob resource")
    commit_sha: str = Field(description="SHA-1 hash ID of the associated commit")
    commit_url: str = Field(
        description="The API URL to get the associated commit resource"
    )


class SecretScanningLocationWikiCommit(GitHubModel):
    """SecretScanningLocationWikiCommit

    Represents a 'wiki_commit' secret scanning location type. This location type
    shows that a secret was detected inside a commit to a repository wiki.
    """

    path: str = Field(description="The file path of the wiki page")
    start_line: float = Field(
        description="Line number at which the secret starts in the file"
    )
    end_line: float = Field(
        description="Line number at which the secret ends in the file"
    )
    start_column: float = Field(
        description="The column at which the secret starts within the start line when the file is interpreted as 8-bit ASCII."
    )
    end_column: float = Field(
        description="The column at which the secret ends within the end line when the file is interpreted as 8-bit ASCII."
    )
    blob_sha: str = Field(description="SHA-1 hash ID of the associated blob")
    page_url: str = Field(description="The GitHub URL to get the associated wiki page")
    commit_sha: str = Field(description="SHA-1 hash ID of the associated commit")
    commit_url: str = Field(
        description="The GitHub URL to get the associated wiki commit"
    )


class SecretScanningLocationIssueTitle(GitHubModel):
    """SecretScanningLocationIssueTitle

    Represents an 'issue_title' secret scanning location type. This location type
    shows that a secret was detected in the title of an issue.
    """

    issue_title_url: str = Field(
        description="The API URL to get the issue where the secret was detected."
    )


class SecretScanningLocationIssueBody(GitHubModel):
    """SecretScanningLocationIssueBody

    Represents an 'issue_body' secret scanning location type. This location type
    shows that a secret was detected in the body of an issue.
    """

    issue_body_url: str = Field(
        description="The API URL to get the issue where the secret was detected."
    )


class SecretScanningLocationIssueComment(GitHubModel):
    """SecretScanningLocationIssueComment

    Represents an 'issue_comment' secret scanning location type. This location type
    shows that a secret was detected in a comment on an issue.
    """

    issue_comment_url: str = Field(
        description="The API URL to get the issue comment where the secret was detected."
    )


class SecretScanningLocationDiscussionTitle(GitHubModel):
    """SecretScanningLocationDiscussionTitle

    Represents a 'discussion_title' secret scanning location type. This location
    type shows that a secret was detected in the title of a discussion.
    """

    discussion_title_url: str = Field(
        description="The URL to the discussion where the secret was detected."
    )


class SecretScanningLocationDiscussionBody(GitHubModel):
    """SecretScanningLocationDiscussionBody

    Represents a 'discussion_body' secret scanning location type. This location type
    shows that a secret was detected in the body of a discussion.
    """

    discussion_body_url: str = Field(
        description="The URL to the discussion where the secret was detected."
    )


class SecretScanningLocationDiscussionComment(GitHubModel):
    """SecretScanningLocationDiscussionComment

    Represents a 'discussion_comment' secret scanning location type. This location
    type shows that a secret was detected in a comment on a discussion.
    """

    discussion_comment_url: str = Field(
        description="The API URL to get the discussion comment where the secret was detected."
    )


class SecretScanningLocationPullRequestTitle(GitHubModel):
    """SecretScanningLocationPullRequestTitle

    Represents a 'pull_request_title' secret scanning location type. This location
    type shows that a secret was detected in the title of a pull request.
    """

    pull_request_title_url: str = Field(
        description="The API URL to get the pull request where the secret was detected."
    )


class SecretScanningLocationPullRequestBody(GitHubModel):
    """SecretScanningLocationPullRequestBody

    Represents a 'pull_request_body' secret scanning location type. This location
    type shows that a secret was detected in the body of a pull request.
    """

    pull_request_body_url: str = Field(
        description="The API URL to get the pull request where the secret was detected."
    )


class SecretScanningLocationPullRequestComment(GitHubModel):
    """SecretScanningLocationPullRequestComment

    Represents a 'pull_request_comment' secret scanning location type. This location
    type shows that a secret was detected in a comment on a pull request.
    """

    pull_request_comment_url: str = Field(
        description="The API URL to get the pull request comment where the secret was detected."
    )


class SecretScanningLocationPullRequestReview(GitHubModel):
    """SecretScanningLocationPullRequestReview

    Represents a 'pull_request_review' secret scanning location type. This location
    type shows that a secret was detected in a review on a pull request.
    """

    pull_request_review_url: str = Field(
        description="The API URL to get the pull request review where the secret was detected."
    )


class SecretScanningLocationPullRequestReviewComment(GitHubModel):
    """SecretScanningLocationPullRequestReviewComment

    Represents a 'pull_request_review_comment' secret scanning location type. This
    location type shows that a secret was detected in a review comment on a pull
    request.
    """

    pull_request_review_comment_url: str = Field(
        description="The API URL to get the pull request review comment where the secret was detected."
    )


model_rebuild(WebhookSecretScanningAlertLocationCreated)
model_rebuild(SecretScanningLocation)
model_rebuild(SecretScanningLocationCommit)
model_rebuild(SecretScanningLocationWikiCommit)
model_rebuild(SecretScanningLocationIssueTitle)
model_rebuild(SecretScanningLocationIssueBody)
model_rebuild(SecretScanningLocationIssueComment)
model_rebuild(SecretScanningLocationDiscussionTitle)
model_rebuild(SecretScanningLocationDiscussionBody)
model_rebuild(SecretScanningLocationDiscussionComment)
model_rebuild(SecretScanningLocationPullRequestTitle)
model_rebuild(SecretScanningLocationPullRequestBody)
model_rebuild(SecretScanningLocationPullRequestComment)
model_rebuild(SecretScanningLocationPullRequestReview)
model_rebuild(SecretScanningLocationPullRequestReviewComment)

__all__ = (
    "WebhookSecretScanningAlertLocationCreated",
    "SecretScanningLocation",
    "SecretScanningLocationCommit",
    "SecretScanningLocationWikiCommit",
    "SecretScanningLocationIssueTitle",
    "SecretScanningLocationIssueBody",
    "SecretScanningLocationIssueComment",
    "SecretScanningLocationDiscussionTitle",
    "SecretScanningLocationDiscussionBody",
    "SecretScanningLocationDiscussionComment",
    "SecretScanningLocationPullRequestTitle",
    "SecretScanningLocationPullRequestBody",
    "SecretScanningLocationPullRequestComment",
    "SecretScanningLocationPullRequestReview",
    "SecretScanningLocationPullRequestReviewComment",
)
