# openapi_client.DashboardsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardsApi.md#create_dashboard) | **POST** /projects/{projectId}/md/dashboards | Creates new dashboard
[**get_all_dashboards**](DashboardsApi.md#get_all_dashboards) | **GET** /projects/{projectId}/md/dashboards | Returns paged collection of all Dashboards in a project
[**get_dashboard_by_id**](DashboardsApi.md#get_dashboard_by_id) | **GET** /projects/{projectId}/md/dashboards/{id} | Gets dashboard by id
[**update_dashboard_by_id**](DashboardsApi.md#update_dashboard_by_id) | **PUT** /projects/{projectId}/md/dashboards/{id} | Updates dashboard by id


# **create_dashboard**
> DashboardDTO create_dashboard(project_id, dashboard_dto)

Creates new dashboard

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_dto import DashboardDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DashboardsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dashboard_dto = openapi_client.DashboardDTO() # DashboardDTO | 

    try:
        # Creates new dashboard
        api_response = api_instance.create_dashboard(project_id, dashboard_dto)
        print("The response of DashboardsApi->create_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->create_dashboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dashboard_dto** | [**DashboardDTO**](DashboardDTO.md)|  | 

### Return type

[**DashboardDTO**](DashboardDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard was successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_dashboards**
> DashboardPagedModelDTO get_all_dashboards(project_id)

Returns paged collection of all Dashboards in a project

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_paged_model_dto import DashboardPagedModelDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DashboardsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project

    try:
        # Returns paged collection of all Dashboards in a project
        api_response = api_instance.get_all_dashboards(project_id)
        print("The response of DashboardsApi->get_all_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_all_dashboards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 

### Return type

[**DashboardPagedModelDTO**](DashboardPagedModelDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_by_id**
> DashboardDTO get_dashboard_by_id(project_id, id)

Gets dashboard by id

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_dto import DashboardDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DashboardsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the dashboard

    try:
        # Gets dashboard by id
        api_response = api_instance.get_dashboard_by_id(project_id, id)
        print("The response of DashboardsApi->get_dashboard_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_dashboard_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the dashboard | 

### Return type

[**DashboardDTO**](DashboardDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Dashboard not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_by_id**
> DashboardDTO update_dashboard_by_id(project_id, id, if_match, dashboard_dto)

Updates dashboard by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_dto import DashboardDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DashboardsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the dashboard
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    dashboard_dto = openapi_client.DashboardDTO() # DashboardDTO | 

    try:
        # Updates dashboard by id
        api_response = api_instance.update_dashboard_by_id(project_id, id, if_match, dashboard_dto)
        print("The response of DashboardsApi->update_dashboard_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->update_dashboard_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the dashboard | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **dashboard_dto** | [**DashboardDTO**](DashboardDTO.md)|  | 

### Return type

[**DashboardDTO**](DashboardDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Dashboard not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

