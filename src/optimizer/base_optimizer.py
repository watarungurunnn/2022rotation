import abc
from typing import Any


class BaseOptimizer(metaclass=abc.ABCMeta):
    """
    順位情報を受け取り、最適化したデータを返す
    """
    processed_data: Any

    @abc.abstractmethod
    def fit(**kwargs) -> Any:
        """
        最適化した結果を返す
        :return: 結果
        """
        raise NotImplementedError
