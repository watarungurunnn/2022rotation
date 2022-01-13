from .base_output import BaseOutput


class SimpleOutput(BaseOutput):
    """
    結果をエクセルにして出力
    """
    def __init__(self, opt_data, **kwargs) -> None:
        """
        kwargsには共通して使用するパラメータ(あれば)
        :param opt_data: 最適化されたデータ
        :param kwargs:
        """
        self.opt_data = opt_data

    def save(**kwargs) -> None:
        """
        結果を出力する
        :return: 結果
        """
        return NotImplementedError
