from .base_optimize import BaseOptimize


class OptimizeSakaguchi(BaseOptimize):
    """
    順位情報を受け取り、最適化したデータを返す
    """
    def __init__(self, input_data, **kwargs) -> None:
        """
        kwargsは必要な引数に置き換えてください(あれば)
        :param input_data: インプットデータ
        :param kwargs:
        """
        self.input_data = input_data

    def fit(**kwargs):
        """
        最適化した結果を返す
        :return: 結果
        """
        return NotImplementedError
