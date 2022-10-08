from pydantic import BaseModel, HttpUrl, Field
import bugsnag
from app.v2.utils import s3


class Delete(BaseModel):
    url: HttpUrl = Field(example='https://DOC-EXAMPLE-BUCKET1.s3.us-west-2.amazonaws.com/puppy.png')

    def media_delete(self):
        try:
            return s3.Client().delete_object(self.url)
        except Exception as e:
            bugsnag.notify(e)
            raise SystemError('FileWasNotDeleted')
