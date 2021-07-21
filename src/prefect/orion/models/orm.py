import sqlalchemy as sa
from sqlalchemy import JSON, Column, String

from prefect.orion.utilities.database import UUID, Base, UUIDDefault


class Flow(Base):
    name = Column(String, nullable=False, unique=True)
    tags = Column(JSON, server_default="[]", default=list, nullable=False)
    parameters = Column(JSON, server_default="{}", default=dict, nullable=False)


class FlowRun(Base):
    flow_id = Column(UUID(), nullable=False, index=True)
    flow_version = Column(String, server_default=UUIDDefault())
    parameters = Column(JSON, server_default="{}", default=dict, nullable=False)
    parent_task_run_id = Column(UUID(), nullable=True)
    context = Column(JSON, server_default="{}", default=dict, nullable=False)
    tags = Column(JSON, server_default="[]", default=list, nullable=False)
    flow_run_metadata = Column(JSON, server_default="{}", default=dict, nullable=False)


class TaskRun(Base):
    flow_run_id = Column(UUID(), nullable=False, index=True)
    task_key = Column(String)
    dynamic_key = Column(String)
    cache_key = Column(String)
    cache_expiration = Column(sa.TIMESTAMP(timezone=True))
    task_version = Column(String, server_default=UUIDDefault())
    empirical_policy = Column(JSON, server_default="{}", default=dict, nullable=False)
    tags = Column(JSON, server_default="[]", default=list, nullable=False)
    upstream_task_run_ids = Column(
        JSON, server_default="{}", default=dict, nullable=False
    )
    task_run_metadata = Column(JSON, server_default="{}", default=dict, nullable=False)


# TODO: add indexes
