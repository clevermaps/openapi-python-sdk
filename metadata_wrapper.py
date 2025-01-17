from auth import Auth
from config import Config
from generated_client import openapi_client
from generated_client.openapi_client.api_client import ApiClient
from generated_client.openapi_client.models.dashboard_dto import DashboardDTO
from generated_client.openapi_client.models.dashboard_paged_model_dto import DashboardPagedModelDTO
from generated_client.openapi_client.models.view_dto import ViewDTO
from generated_client.openapi_client.models.view_paged_model_dto import ViewPagedModelDTO


class MetadataWrapper:

    def __init__(self, config: Config):
        self.auth = Auth(config)
        self.config = config
        self.api_client = self._create_api_client()

        self.dashboards_api = openapi_client.DashboardsApi(self.api_client)
        self.views_api = openapi_client.ViewsApi(self.api_client)

    def get_all_dashboards(self, project_id: str) -> DashboardPagedModelDTO:
        self._handle_token()
        return self.dashboards_api.get_all_dashboards(project_id)

    def get_dashboard_by_id(self, project_id: str, dashboard_id: str) -> DashboardDTO:
        self._handle_token()
        return self.dashboards_api.get_dashboard_by_id(project_id, dashboard_id)

    def create_dashboard(self, project_id: str, dashboard: DashboardDTO) -> DashboardDTO:
        self._handle_token()
        return self.dashboards_api.create_dashboard(project_id, dashboard)

    def update_dashboard(self, project_id: str, dashboard_id: str, dashboard: DashboardDTO) -> DashboardDTO:
        self._handle_token()
        etag = self.dashboards_api.get_dashboard_by_id_with_http_info(project_id, dashboard_id).headers["ETag"]
        return self.dashboards_api.update_dashboard_by_id(project_id, dashboard_id, etag, dashboard)

    def delete_dashboard(self, project_id: str, dashboard_id: str) -> None:
        self._handle_token()
        self.dashboards_api.delete_dashboard_by_id(project_id, dashboard_id)

    def get_all_views(self, project_id: str) -> ViewPagedModelDTO:
        self._handle_token()
        return self.views_api.get_all_views(project_id)

    def get_view_by_id(self, project_id: str, view_id: str) -> ViewDTO:
        self._handle_token()
        return self.views_api.get_view_by_id(project_id, view_id)

    def create_view(self, project_id: str, view: ViewDTO) -> ViewDTO:
        self._handle_token()
        return self.views_api.create_view(project_id, view)

    def update_view(self, project_id: str, view_id: str, view: ViewDTO) -> ViewDTO:
        self._handle_token()
        etag = self.views_api.get_view_by_id_with_http_info(project_id, view_id).headers["ETag"]
        return self.views_api.update_view_by_id(project_id, view_id, etag, view)

    def delete_view(self, project_id: str, view_id: str) -> None:
        self._handle_token()
        self.views_api.delete_view_by_id(project_id, view_id)

    def _create_api_client(self) -> ApiClient:
        configuration = openapi_client.Configuration(
            host=self.config.base_url,
            access_token=self.auth.get_token()
        )

        return openapi_client.ApiClient(configuration)

    def _handle_token(self) -> None:
        new_token = self.auth.get_token()
        if self.api_client.configuration.access_token != new_token:
            self.api_client.configuration.access_token = new_token