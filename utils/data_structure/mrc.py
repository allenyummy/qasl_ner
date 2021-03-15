# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Data Structure of Machine Reading Comprehension

import logging
from typing import List, NamedTuple

logger = logging.getLogger(__name__)


class AnswerStruct(NamedTuple):
    """
    An internal data structure of AN answer in given passage.

    Args:
        `text`: The text of answer.
        `type`: The entity type of answer.
        `start_pos`: The start position of `text` in given passage.
        `end_pos`: The end position of `text` in given passage. (Notice: exact_end or exact_end+1)
    Type:
        `text`: string
        `type`: string
        `start_pos`: integer
        `end_pos`: integer
    """

    text: str
    type: str
    start_pos: int
    end_pos: int

    def __eq__(self, other):
        return (
            self.type == other.type
            and self.text == other.text
            and self.start_pos == other.start_pos
            and self.end_pos == other.end_pos
        )

    def __repr__(self):
        return f"({self.type}, {self.text}, {self.start_pos}, {self.end_pos})"


class DataStruct(NamedTuple):
    """
    An internal data structure of A data/sample/example in the entire dataset.

    Args:
        `pid`: The identification number of sample.
        `passage`: The passage text of sample.
        `answers`: The answers list of sample.
    Type:
        `pid`: integer
        `passage`: string
        `answers`: list of `AnswerStruct`
    """

    pid: int
    passage: str
    answers: List[AnswerStruct]

    def __len__(self):
        return len(self.answers)

    def __repr__(self):
        message = (
            f"[  PID  ]: {self.pid},\n" f"[PASSAGE]: {self.passage},\n" f"[ANSWERS]: \n"
        )
        for ans in self.answers:
            message += f"{ans}\n"
        return message


class MRCStruct(NamedTuple):
    """
    A data structure of the entire dataset.

    Args:
        `built_time`: The time when the dataset is built.
        `version`: The version of datasest.
        `data`: The entire samples.
    Type:
        `built_time`: string
        `version`: string
        `data`: list of `DataStruct`
    """

    built_time: str
    version: str
    data: List[DataStruct]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"[BUILT_TIME]: {self.built_time}\n" f"[ VERSION ] : {self.version}"


if __name__ == "__main__":

    a_e = AnswerStruct(text="gg", type="ff", start_pos=2, end_pos=4)
    a_s = AnswerStruct(text="gg", type="ff", start_pos=2, end_pos=4)
    a = DataStruct(pid="1", passage="Hello World", answers=[a_e, a_s, a_e])
    print(a)

    print(AnswerStruct.__doc__)

    print(a_e == a_s)
    print(a)
