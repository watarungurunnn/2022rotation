import abc
from typing import Any

class BaseValidator(metaclass=abc.ABCMeta):
    """
    入力データに不整合がないかチェックする
    """
    input_data: Any

    @abc.abstractmethod
    def validate(**kwargs):
        """
        不整合があればエラーを返す
        """
        raise NotImplementedError
