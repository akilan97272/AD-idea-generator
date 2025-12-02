from pydantic import BaseModel

class ScriptResponse(BaseModel):
    script: str
    visual_hook: str
