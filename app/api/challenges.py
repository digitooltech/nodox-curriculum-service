from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.challenge import Challenge
from app.schemas.challenge import ChallengeResponse

router = APIRouter()

@router.get("/challenges", response_model=list[ChallengeResponse])
async def list_challenges(db: AsyncSession = Depends(get_db)):    
    stmt = select(Challenge).where(Challenge.is_published == True)
    result = await db.execute(stmt)
    return result.scalars().all()