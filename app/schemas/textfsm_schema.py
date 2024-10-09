from pydantic import BaseModel

class TextFSMRequest(BaseModel):
    fsmtxt: str
    inputtext: str
    fsmmode: str