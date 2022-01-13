from numpy.typing import Arraylike
from .validator.simple_validator import SimpleValidator
from pathlib import Path
import pandas as pd

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
        self.input_path = Path(input_path)
        self.input_data = pd.read_excel(input_path, header=None)
        SimpleValidator(self.input_data).validate()

    def process(self, **kwargs) -> Array:
        """
        成形した結果を返す
        :return: データ
        """
        return NotImplementedError
