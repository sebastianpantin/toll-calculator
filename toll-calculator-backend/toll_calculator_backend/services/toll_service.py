from repository.toll_repository import TollRepository


class TollService:
    def __init__(self):
        """
        Init the service
        """
        self.repository = TollRepository()
