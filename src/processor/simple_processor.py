from numpy.typing import ArrayLike
from .validator.simple_validator import SimpleValidator
import pandas as pd
from pandas import DataFrame
from typing import Union

from .base_processor import BaseProcessor


class SimpleProcessor(BaseProcessor):
    """
    inputを受け取り、成形したデータを返す
    """
    def __init__(self, input_path: str, input_format: str='excel', **kwargs) -> None:
        """
        inputを受け取り、成形したデータを返す
        :params input_path: 入力ファイルのpath
        :params kwargs: pandasへのoptional引数
        """
        if input_format == 'excel':
            self.raw_data = pd.read_excel(input_path, kwargs)
        elif input_format == 'csv':
            self.raw_data = pd.read_csv(input_path, kwargs)
        else:
            raise ValueError

    def process(self, column: str='order', format: str='ndarray', **kwargs) -> Union[ArrayLike, DataFrame]:
        """
        成形した結果を返す
        :param column: 列の形式。デフォルトは'order'。'course'を選択可能(README参照)
        :param format: デフォルトは'ndarray'。'dataframe'を選択可能
        :return: データ
        """
        SimpleValidator(self.raw_data).validate()
        if column == 'order':
            pass
        elif column == 'course':
            pass
        else:
            raise ValueError

        if format == 'ndarray':
            self._to_array()
            pass
        elif format == 'dataframe':
            pass
        else:
            raise ValueError
        raise NotImplementedError

    def _to_array(self) -> None:
        """
        処理済みデータをndarrayに直す
        """
        pass
