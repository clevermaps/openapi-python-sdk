class Config:
    def __init__(
            self,
            base_url: str,
            refresh_token: str = None
    ):
        self.base_url = base_url
        self.refresh_token = refresh_token
