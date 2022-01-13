import abc


class BaseInput(metaclass=abc.ABCMeta):
    """
    inputを受け取り、成形したデータを返す
    :params input_path: 入力ファイルのpath
    """
    input_path: str

    @abc.abstractmethod
    def process(self, **kwargs):
        """
        成形した結果を返す
        :return: データ
        """
        pass
