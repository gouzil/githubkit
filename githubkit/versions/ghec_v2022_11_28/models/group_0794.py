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

from .group_0002 import SimpleUser
from .group_0202 import Deployment
from .group_0415 import EnterpriseWebhooks
from .group_0416 import SimpleInstallation
from .group_0418 import RepositoryWebhooks
from .group_0417 import OrganizationSimpleWebhooks


class WebhookWorkflowJobCompleted(GitHubModel):
    """workflow_job completed event"""

    action: Literal["completed"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
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
    workflow_job: WebhookWorkflowJobCompletedPropWorkflowJob = Field()
    deployment: Missing[Deployment] = Field(
        default=UNSET,
        title="Deployment",
        description="A request for a specific ref(branch,sha,tag) to be deployed",
    )


class WebhookWorkflowJobCompletedPropWorkflowJob(GitHubModel):
    """WebhookWorkflowJobCompletedPropWorkflowJob"""

    check_run_url: str = Field()
    completed_at: str = Field()
    conclusion: Literal[
        "success",
        "failure",
        "skipped",
        "cancelled",
        "action_required",
        "neutral",
        "timed_out",
    ] = Field()
    created_at: str = Field(description="The time that the job created.")
    head_sha: str = Field()
    html_url: str = Field()
    id: int = Field()
    labels: List[str] = Field(
        description='Custom labels for the job. Specified by the [`"runs-on"` attribute](https://docs.github.com/enterprise-cloud@latest//actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on) in the workflow YAML.'
    )
    name: str = Field()
    node_id: str = Field()
    run_attempt: int = Field()
    run_id: int = Field()
    run_url: str = Field()
    runner_group_id: Union[Union[int, None], None] = Field(
        description="The ID of the runner group that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`."
    )
    runner_group_name: Union[Union[str, None], None] = Field(
        description="The name of the runner group that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`."
    )
    runner_id: Union[Union[int, None], None] = Field(
        description="The ID of the runner that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`."
    )
    runner_name: Union[Union[str, None], None] = Field(
        description="The name of the runner that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`."
    )
    started_at: str = Field()
    status: Literal["queued", "in_progress", "completed", "waiting"] = Field(
        description="The current status of the job. Can be `queued`, `in_progress`, `waiting`, or `completed`."
    )
    head_branch: Union[Union[str, None], None] = Field(
        description="The name of the current branch."
    )
    workflow_name: Union[Union[str, None], None] = Field(
        description="The name of the workflow."
    )
    steps: List[WebhookWorkflowJobCompletedPropWorkflowJobMergedSteps] = Field()
    url: str = Field()


class WebhookWorkflowJobCompletedPropWorkflowJobMergedSteps(GitHubModel):
    """WebhookWorkflowJobCompletedPropWorkflowJobMergedSteps"""

    completed_at: Union[str, None] = Field()
    conclusion: Union[None, Literal["failure", "skipped", "success", "cancelled"]] = (
        Field()
    )
    name: str = Field()
    number: int = Field()
    started_at: Union[str, None] = Field()
    status: Literal["in_progress", "completed", "queued"] = Field()


model_rebuild(WebhookWorkflowJobCompleted)
model_rebuild(WebhookWorkflowJobCompletedPropWorkflowJob)
model_rebuild(WebhookWorkflowJobCompletedPropWorkflowJobMergedSteps)

__all__ = (
    "WebhookWorkflowJobCompleted",
    "WebhookWorkflowJobCompletedPropWorkflowJob",
    "WebhookWorkflowJobCompletedPropWorkflowJobMergedSteps",
)
