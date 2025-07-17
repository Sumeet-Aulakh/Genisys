#Here we define the Pydantic models and Data Classes for the project

from pydantic import BaseModel

class ScriptType(BaseModel):
    command: str
    flags: str
    file: str

class FileType(BaseModel):
    name: str
    extension: str
    content: str

class ResponseType(BaseModel):
    title: str
    description: str
    repoName: str
    files: list[FileType]
    scriptToRun: ScriptType
    libraries: list[str]
