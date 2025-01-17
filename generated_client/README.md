# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthenticationApi(api_client)
    token_request_dto = openapi_client.TokenRequestDTO() # TokenRequestDTO |  (optional)

    try:
        # Get bearer token
        api_response = api_instance.get_token(token_request_dto=token_request_dto)
        print("The response of AuthenticationApi->get_token:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**get_token**](docs/AuthenticationApi.md#get_token) | **POST** /oauth/token | Get bearer token
*DashboardsApi* | [**create_dashboard**](docs/DashboardsApi.md#create_dashboard) | **POST** /projects/{projectId}/md/dashboards | Creates new dashboard
*DashboardsApi* | [**get_all_dashboards**](docs/DashboardsApi.md#get_all_dashboards) | **GET** /projects/{projectId}/md/dashboards | Returns paged collection of all Dashboards in a project
*DashboardsApi* | [**get_dashboard_by_id**](docs/DashboardsApi.md#get_dashboard_by_id) | **GET** /projects/{projectId}/md/dashboards/{id} | Gets dashboard by id
*DashboardsApi* | [**update_dashboard_by_id**](docs/DashboardsApi.md#update_dashboard_by_id) | **PUT** /projects/{projectId}/md/dashboards/{id} | Updates dashboard by id
*ViewsApi* | [**create_view**](docs/ViewsApi.md#create_view) | **POST** /projects/{projectId}/md/views | Creates new view
*ViewsApi* | [**delete_dashboard_by_id**](docs/ViewsApi.md#delete_dashboard_by_id) | **DELETE** /projects/{projectId}/md/dashboards/{id} | Deletes dashboard by id
*ViewsApi* | [**delete_view_by_id**](docs/ViewsApi.md#delete_view_by_id) | **DELETE** /projects/{projectId}/md/views/{id} | Deletes view by id
*ViewsApi* | [**get_all_views**](docs/ViewsApi.md#get_all_views) | **GET** /projects/{projectId}/md/views | Returns collection of all views in a project
*ViewsApi* | [**get_view_by_id**](docs/ViewsApi.md#get_view_by_id) | **GET** /projects/{projectId}/md/views/{id} | Gets view by id
*ViewsApi* | [**update_view_by_id**](docs/ViewsApi.md#update_view_by_id) | **PUT** /projects/{projectId}/md/views/{id} | Updates view by id


## Documentation For Models

 - [ActiveDateFilterDTO](docs/ActiveDateFilterDTO.md)
 - [ActiveFeatureFilterDTO](docs/ActiveFeatureFilterDTO.md)
 - [ActiveFilterAbstractType](docs/ActiveFilterAbstractType.md)
 - [ActiveGlobalDateFilterDTO](docs/ActiveGlobalDateFilterDTO.md)
 - [ActiveHistogramFilterDTO](docs/ActiveHistogramFilterDTO.md)
 - [ActiveIndicatorFilterDTO](docs/ActiveIndicatorFilterDTO.md)
 - [ActiveMultiSelectFilterDTO](docs/ActiveMultiSelectFilterDTO.md)
 - [ActiveSingleSelectFilterDTO](docs/ActiveSingleSelectFilterDTO.md)
 - [AdditionalSeriesLinkDTO](docs/AdditionalSeriesLinkDTO.md)
 - [AnnotationLinkDTO](docs/AnnotationLinkDTO.md)
 - [AttributeFormatDTO](docs/AttributeFormatDTO.md)
 - [BlockRowAbstractType](docs/BlockRowAbstractType.md)
 - [BlockRowDTO](docs/BlockRowDTO.md)
 - [CategoriesDTO](docs/CategoriesDTO.md)
 - [CenterDTO](docs/CenterDTO.md)
 - [CuzkParcelInfoDTO](docs/CuzkParcelInfoDTO.md)
 - [DashboardContentDTO](docs/DashboardContentDTO.md)
 - [DashboardDTO](docs/DashboardDTO.md)
 - [DashboardDatasetPropertiesDTO](docs/DashboardDatasetPropertiesDTO.md)
 - [DashboardPagedModelDTO](docs/DashboardPagedModelDTO.md)
 - [DateFilterDTO](docs/DateFilterDTO.md)
 - [DateFilterDefaultValueType](docs/DateFilterDefaultValueType.md)
 - [DateRangeFunction](docs/DateRangeFunction.md)
 - [DateRangeValue](docs/DateRangeValue.md)
 - [DefaultSelectedDTO](docs/DefaultSelectedDTO.md)
 - [DefaultValuesDateDTO](docs/DefaultValuesDateDTO.md)
 - [DefaultValuesFeatureDTO](docs/DefaultValuesFeatureDTO.md)
 - [DefaultValuesHistogramDTO](docs/DefaultValuesHistogramDTO.md)
 - [DefaultValuesIndicatorDTO](docs/DefaultValuesIndicatorDTO.md)
 - [DefaultValuesMultiSelectDTO](docs/DefaultValuesMultiSelectDTO.md)
 - [DefaultValuesSingleSelectDTO](docs/DefaultValuesSingleSelectDTO.md)
 - [DistributionDTO](docs/DistributionDTO.md)
 - [ExportLinkDTO](docs/ExportLinkDTO.md)
 - [FeatureAttributeDTO](docs/FeatureAttributeDTO.md)
 - [FeatureFilterDTO](docs/FeatureFilterDTO.md)
 - [FilterAbstractType](docs/FilterAbstractType.md)
 - [FormatDTO](docs/FormatDTO.md)
 - [FormatDTO1](docs/FormatDTO1.md)
 - [GlobalDateFilterDTO](docs/GlobalDateFilterDTO.md)
 - [GoogleEarthDTO](docs/GoogleEarthDTO.md)
 - [GoogleSatelliteDTO](docs/GoogleSatelliteDTO.md)
 - [GoogleStreetViewDTO](docs/GoogleStreetViewDTO.md)
 - [HistogramFilterDTO](docs/HistogramFilterDTO.md)
 - [IndicatorFilterDTO](docs/IndicatorFilterDTO.md)
 - [IndicatorGroupDTO](docs/IndicatorGroupDTO.md)
 - [IndicatorLinkDTO](docs/IndicatorLinkDTO.md)
 - [IndicatorLinkDTOBlockRowsInner](docs/IndicatorLinkDTOBlockRowsInner.md)
 - [IsochroneDTO](docs/IsochroneDTO.md)
 - [MandatoryKeysForPagableResponse](docs/MandatoryKeysForPagableResponse.md)
 - [MapContextMenuDTO](docs/MapContextMenuDTO.md)
 - [MapContextMenuItemAbstractType](docs/MapContextMenuItemAbstractType.md)
 - [MapOptionsDTO](docs/MapOptionsDTO.md)
 - [MapOptionsDTOCustomTileLayer](docs/MapOptionsDTOCustomTileLayer.md)
 - [MapyczOrtophotoDTO](docs/MapyczOrtophotoDTO.md)
 - [MapyczPanoramaDTO](docs/MapyczPanoramaDTO.md)
 - [MeasureDTO](docs/MeasureDTO.md)
 - [MultiSelectFilterDTO](docs/MultiSelectFilterDTO.md)
 - [OrderByDTO](docs/OrderByDTO.md)
 - [RankingDTO](docs/RankingDTO.md)
 - [SingleSelectFilterDTO](docs/SingleSelectFilterDTO.md)
 - [TimeSeriesDTO](docs/TimeSeriesDTO.md)
 - [TokenRequestDTO](docs/TokenRequestDTO.md)
 - [TokenResponseDTO](docs/TokenResponseDTO.md)
 - [VariableDTO](docs/VariableDTO.md)
 - [VariablesDTO](docs/VariablesDTO.md)
 - [ViewContentDTO](docs/ViewContentDTO.md)
 - [ViewDTO](docs/ViewDTO.md)
 - [ViewPagedModelDTO](docs/ViewPagedModelDTO.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication


## Author



