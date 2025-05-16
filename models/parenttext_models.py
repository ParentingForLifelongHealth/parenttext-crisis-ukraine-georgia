from rpft.parsers.creation.datarowmodel import DataRowModel
from rpft.parsers.common.rowparser import ParserModel
from parenttext_pipeline.models.parenttext_models import *
from typing import List


class JoiningTriggerModel(DataRowModel):
    triggers: str = ""
    groups: list[str] = []
    cap: str = ""
    location: str = ""
    set_location: str = "no"
