import os

class Jaqi:
    uid = 'jaqi'
    pw = os.getenv('PASSWORD')

    @staticmethod
    def is_authenticated() -> bool:
        return True

    @staticmethod
    def is_active() -> bool:
        return True

    @staticmethod
    def is_anonymous() -> bool:
        return False

    @staticmethod
    def get_id() -> str:
        return Jaqi.uid
