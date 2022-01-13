import abc
from typing import Any


class BaseOptimize(metaclass=abc.ABCMeta):
    """
    順位情報を受け取り、最適化したデータを返す
    """
    input_data: Any

    @abc.abstractmethod
    def fit(**kwargs):
        """
        最適化した結果を返す
        :return: 結果
        """
        raise NotImplementedError
