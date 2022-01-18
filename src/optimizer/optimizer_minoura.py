from .base_optimizer import BaseOptimizer


class OptimizerMinoura(BaseOptimizer):
    """
    順位情報を受け取り、最適化したデータを返す
    """
    def __init__(self, processed_data, **kwargs) -> None:
        """
        kwargsは必要な引数に置き換えてください(あれば)
        :param input_data: インプットデータ
        :param kwargs:
        """
        self.processed_data = processed_data

    def fit(**kwargs):
        """
        最適化した結果を返す
        :return: 結果
        """
        raise NotImplementedError
