"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0002 import SimpleUser
from .group_0420 import EnterpriseWebhooks
from .group_0421 import SimpleInstallation
from .group_0423 import RepositoryWebhooks
from .group_0422 import OrganizationSimpleWebhooks


class WebhookWorkflowDispatch(GitHubModel):
    """workflow_dispatch event"""

    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    inputs: Union[WebhookWorkflowDispatchPropInputs, None] = Field()
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
    ref: str = Field()
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    workflow: str = Field()


class WebhookWorkflowDispatchPropInputs(ExtraGitHubModel):
    """WebhookWorkflowDispatchPropInputs"""


model_rebuild(WebhookWorkflowDispatch)
model_rebuild(WebhookWorkflowDispatchPropInputs)

__all__ = (
    "WebhookWorkflowDispatch",
    "WebhookWorkflowDispatchPropInputs",
)
