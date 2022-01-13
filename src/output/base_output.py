import abc
from typing import Any


class BaseOutput(metaclass=abc.ABCMeta):
    """
    結果をエクセルにして出力
    """
    opt_data: Any

    @abc.abstractmethod
    def save(**kwargs):
        """
        結果を出力する
        :return: 結果
        """
        return NotImplementedError
