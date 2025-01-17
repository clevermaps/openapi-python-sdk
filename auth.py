from typing import Optional
from datetime import datetime, timedelta
from config import Config
from generated_client import openapi_client
from generated_client.openapi_client.models.token_request_dto import TokenRequestDTO
from generated_client.openapi_client.models.token_response_dto import TokenResponseDTO


class Auth:
    def __init__(self, config: Config):
        self.config = config
        self.access_token: Optional[str] = None
        self.token_expiry: Optional[datetime] = None
        self.client_configuration = openapi_client.Configuration(host=config.base_url)

    def get_token(self) -> str:
        if not self._is_token_valid():
            self._get_new_token()

        if self.access_token is None:
            raise Exception("Unable to get access token.")

        return self.access_token

    def _is_token_valid(self) -> bool:
        if not self.access_token or not self.token_expiry:
            return False

        return datetime.now() + timedelta(minutes=5) < self.token_expiry

    def _get_new_token(self) -> None:
        try:
            with openapi_client.ApiClient(self.client_configuration) as api_client:
                auth_api = openapi_client.AuthenticationApi(api_client)

                get_token_request = TokenRequestDTO(
                    refresh_token=self.config.refresh_token
                )

                response: TokenResponseDTO = auth_api.get_token(token_request_dto=get_token_request)

                if response.access_token is not None:
                    self.access_token = response.access_token

                if response.refresh_token is not None:
                    self.config.refresh_token = response.refresh_token

                if response.expires_in is not None:
                    self.token_expiry = datetime.now() + timedelta(seconds=float(response.expires_in))

        except Exception as e:
            raise Exception(f"Unable to fetch access token: {str(e)}")