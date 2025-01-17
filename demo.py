from config import Config
from metadata_wrapper import MetadataWrapper
from generated_client.openapi_client.models.center_dto import CenterDTO
from generated_client.openapi_client.models.map_options_dto import MapOptionsDTO
from generated_client.openapi_client.models.view_content_dto import ViewContentDTO
from generated_client.openapi_client.models.view_dto import ViewDTO

config = Config(
    base_url="https://staging.dev.clevermaps.io/rest",
    refresh_token="<REFRESH_TOKEN>"
)

metadata_wrapper = MetadataWrapper(config)

project_id = "<PROJECT_ID>"

def demo_print_all_views() -> None:
    views = metadata_wrapper.get_all_views(project_id)
    ids = [view.id for view in views.content]
    print("views:", ", ".join(ids))
    print()

def demo_create_view() -> ViewDTO:
    center = CenterDTO(
        lat=51.5078988895,
        lng=-0.13758659362
    )

    map_options = MapOptionsDTO(
        zoom=15,
        tile_layer="mapbox",
        center=center
    )

    view_content = ViewContentDTO(
        icon="location_mark",
        dashboard=f"/rest/projects/{project_id}/md/dashboards?name=points_overview_dashboard",
        default_visualized=f"/rest/projects/{project_id}/md/indicators?name=points_value_sum_indicator",
        map_options=map_options
    )

    view = ViewDTO(
        name="test_view",
        type="view",
        title="Test View",
        description="Test View Description",
        content=view_content
    )

    created_view = metadata_wrapper.create_view(project_id, view)
    print(f"view created: {created_view.id}")
    return created_view

def demo_update_view(view: ViewDTO) -> ViewDTO:
    view.name = "updated_view"
    view.title = "Updated View"
    view.content.map_options.zoom = 10

    updated_view = metadata_wrapper.update_view(project_id, view.id, view)
    print(f"view updated: {updated_view.id}")
    return updated_view

def demo_get_view(view_id: str) -> ViewDTO:
    return metadata_wrapper.get_view_by_id(project_id, view_id)

def demo_delete_view(view_id: str) -> None:
    metadata_wrapper.delete_view(project_id, view_id)
    print(f"view deleted: {view_id}")

if __name__ == "__main__":
    demo_print_all_views()

    # create new view
    created_view = demo_create_view()
    demo_print_all_views()

    # update existing view
    existing_view = demo_update_view(created_view)

    # get updated view
    view = demo_get_view(existing_view.id)
    print(view)
    print()

    # delete view
    demo_delete_view(created_view.id)
    demo_print_all_views()