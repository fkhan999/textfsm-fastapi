from fastapi import APIRouter, HTTPException
from app.schemas.textfsm_schema import TextFSMRequest
from app.services.textfsm_service import parse_textfsm

router = APIRouter()

@router.post("/textfsm_parser")
def textfsm_parser(request: TextFSMRequest):
    try:
        return parse_textfsm(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
