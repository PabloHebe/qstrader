"""
This is good error handling. Subclass created of Exception.
Gives if correctly applied a good error message.
"""

class AbstractEmptyDataRow(Exception):
    pass


class EmptyTickEvent(AbstractEmptyDataRow):
    pass


class EmptyBarEvent(AbstractEmptyDataRow):
    pass
