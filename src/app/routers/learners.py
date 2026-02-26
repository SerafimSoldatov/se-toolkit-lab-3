"""Router for learner endpoints."""

from fastapi import APIRouter

from datetime import datetime

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners, create_learner
from app.models.learner import Learner, LearnerCreate

router = APIRouter()

# ===
# PART A: GET endpoint
# ===

@router.get("/learners", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime = None,
    session: AsyncSession = Depends(get_session),
):
    """Get learners with optional filter by enrollment date"""
    return await read_learners(session, enrolled_after)

# ===
# PART B: POST endpoint
# ===

@router.post("/learners", response_model=Learner, status_code=201)
async def create_learner(
    learner_data: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    """Create a new learner"""
    return await create_learner_in_db(session, name=learner_data.name, email=learner_data.email)
