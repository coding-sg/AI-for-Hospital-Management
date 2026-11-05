from typing import List, Optional
from pydantic import BaseModel, Field

class WorkflowStep(BaseModel):
    title: str = Field(description="Short title for this workflow step")
    description: str = Field(description="What should happen during this step")
    responsible_role: Optional[str] = Field(default=None, description="Suggested responsible role")

class KPI(BaseModel):
    name: str = Field(description="Name of the operational or quality KPI")
    description: str = Field(description="What the KPI measures and why it matters")
    calculation: Optional[str] = Field(default=None, description="Simple calculation or definition, if appropriate")

class HospitalManagementResponse(BaseModel):
    overview: str
    key_concepts: List[str]
    workflow_steps: List[WorkflowStep]
    practical_example: Optional[str] = None
    relevant_kpis: List[KPI]
    action_checklist: List[str]
    risks_and_safeguards: List[str]
    assumptions_or_missing_information: List[str]
    further_considerations: List[str]
