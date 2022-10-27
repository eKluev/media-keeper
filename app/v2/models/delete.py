import bugsnag
import logging
import os
from pydantic import BaseModel, HttpUrl, Field
from app.v2.utils import s3


class Delete(BaseModel):
    url: HttpUrl = Field(example='https://DOC-EXAMPLE-BUCKET1.s3.us-west-2.amazonaws.com/puppy.png')

    def media_delete(self):
        try:
            return s3.Client().delete_object(self.url)
        except Exception as e:
            if os.environ.get('BUGSNAG'):
                bugsnag.notify(e)
            else:
                logging.exception(e)
            raise SystemError('FileWasNotDeleted')
