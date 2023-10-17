from typing import Any, TypedDict
from uuid import uuid4
from asyncio import Event

class SocketResponseDict(TypedDict):
    id: str
    success: bool
    res: Any

class MethodCallResponse:
    def __init__(self, success: bool, result: Any) -> None:
        self.success = success
        self.result = result

class MethodCallRequest:
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.event = Event()
        self.response: MethodCallResponse
    
    def set_result(self, dc: SocketResponseDict):
        self.response = MethodCallResponse(dc["success"], dc["res"])
        self.event.set()
    
    async def wait_for_result(self):
        await self.event.wait()
        if not self.response.success:
            raise Exception(self.response.result)
        return self.response