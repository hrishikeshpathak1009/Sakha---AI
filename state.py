from typing import TypedDict, Annotated
import operator


class SaakhaaState(TypedDict):

    messages: Annotated[
        list,
        operator.add
    ]