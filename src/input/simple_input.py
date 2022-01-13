from nptyping import Array

from .base_input import BaseInput


class SimpleInput(BaseInput):
    """
    inputを受け取り、成形したデータを返す
    """
    def __init__(self, input_path: str) -> None:
        """
        inputを受け取り、成形したデータを返す
        :params input_path: 入力ファイルのpath
        """
        self.input_path = input_path

    def process(self, **kwargs) -> Array:
        """
        成形した結果を返す
        :return: データ
        """
        return NotImplementedError
