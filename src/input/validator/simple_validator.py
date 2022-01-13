from .base_validator import BaseValidator

class SimpleValidator(BaseValidator):
    """
    入力データに不整合がないかチェックする
    """
    def __init__(self, input_data):
        """
        kwargsは必要な引数に置き換えてください(あれば)
        :param input_data: インプットデータ
        :param kwargs:
        """
        self.input_data = input_data

    def validate(**kwargs):
        """
        不整合があればエラーを返す
        """
        raise NotImplementedError
