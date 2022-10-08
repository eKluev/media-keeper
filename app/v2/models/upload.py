import base64
import bugsnag
import re

from pydantic import BaseModel, constr, Field, validator
from app.v2.utils import s3


class Upload(BaseModel):
    path: constr(max_length=50) = Field(example='project/owner_id')
    object_name: constr(max_length=64) = Field(example='event_34675')
    object_type: constr(max_length=5) = Field(example='jpg')
    base64_data: str

    @validator('path')
    def strip_path(cls, v):
        return v.strip('/')

    @validator('object_name', 'object_type')
    def spellchecking(cls, v):
        if v != re.sub("[^A-Za-z0-9_]", "", v):
            raise ValueError('object_name/object_type should contain latin symbols, digits, underscore only')
        return v

    def media_upload(self):
        try:
            media = base64.b64decode(self.base64_data.encode('ascii'))
            path = f"{self.path}/{self.object_name}.{self.object_type}"
            return s3.Client().put_object(media, path)

        except Exception as e:
            bugsnag.notify(e)
            raise SystemError('FileHasNotUploaded')
