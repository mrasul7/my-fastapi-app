from datetime import datetime
import time
from typing import Annotated
from sqlalchemy import DateTime, text
from sqlalchemy.orm import mapped_column


create_at = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('Europe/Moscow', NOW())")
    )
]
