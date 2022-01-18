import abc
from dataclasses import dataclass
from pandas import DataFrame
from typing import Union
from numpy.typing import ArrayLike


@dataclass
class BaseProcessor(metaclass=abc.ABCMeta):
    """
    inputを受け取り、成形したデータを返す
    :params input_path: 入力ファイルのpath
    """
    raw_data: DataFrame
    processed_data: Union[DataFrame, ArrayLike]

    @abc.abstractmethod
    def __init__(self, input_path):
        raise NotImplementedError

    @abc.abstractmethod
    def process(self, **kwargs):
        """
        成形した結果を返す
        :return: データ
        """
        raise NotImplementedError
