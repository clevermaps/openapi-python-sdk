# openapi_client.ViewsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_view**](ViewsApi.md#create_view) | **POST** /projects/{projectId}/md/views | Creates new view
[**delete_dashboard_by_id**](ViewsApi.md#delete_dashboard_by_id) | **DELETE** /projects/{projectId}/md/dashboards/{id} | Deletes dashboard by id
[**delete_view_by_id**](ViewsApi.md#delete_view_by_id) | **DELETE** /projects/{projectId}/md/views/{id} | Deletes view by id
[**get_all_views**](ViewsApi.md#get_all_views) | **GET** /projects/{projectId}/md/views | Returns collection of all views in a project
[**get_view_by_id**](ViewsApi.md#get_view_by_id) | **GET** /projects/{projectId}/md/views/{id} | Gets view by id
[**update_view_by_id**](ViewsApi.md#update_view_by_id) | **PUT** /projects/{projectId}/md/views/{id} | Updates view by id


# **create_view**
> ViewDTO create_view(project_id, view_dto)

Creates new view

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.view_dto import ViewDTO
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
    api_instance = openapi_client.ViewsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    view_dto = openapi_client.ViewDTO() # ViewDTO | 

    try:
        # Creates new view
        api_response = api_instance.create_view(project_id, view_dto)
        print("The response of ViewsApi->create_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->create_view: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **view_dto** | [**ViewDTO**](ViewDTO.md)|  | 

### Return type

[**ViewDTO**](ViewDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | View was successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_by_id**
> delete_dashboard_by_id(project_id, id)

Deletes dashboard by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ViewsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the dashboard

    try:
        # Deletes dashboard by id
        api_instance.delete_dashboard_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling ViewsApi->delete_dashboard_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the dashboard | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Dashboard was successfully deleted |  -  |
**404** | Dashboard not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_view_by_id**
> delete_view_by_id(project_id, id)

Deletes view by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ViewsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the view

    try:
        # Deletes view by id
        api_instance.delete_view_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling ViewsApi->delete_view_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the view | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | View was successfully deleted |  -  |
**404** | View not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_views**
> ViewPagedModelDTO get_all_views(project_id)

Returns collection of all views in a project

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.view_paged_model_dto import ViewPagedModelDTO
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
    api_instance = openapi_client.ViewsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project

    try:
        # Returns collection of all views in a project
        api_response = api_instance.get_all_views(project_id)
        print("The response of ViewsApi->get_all_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->get_all_views: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 

### Return type

[**ViewPagedModelDTO**](ViewPagedModelDTO.md)

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

# **get_view_by_id**
> ViewDTO get_view_by_id(project_id, id)

Gets view by id

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.view_dto import ViewDTO
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
    api_instance = openapi_client.ViewsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the view

    try:
        # Gets view by id
        api_response = api_instance.get_view_by_id(project_id, id)
        print("The response of ViewsApi->get_view_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->get_view_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the view | 

### Return type

[**ViewDTO**](ViewDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | View not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_view_by_id**
> ViewDTO update_view_by_id(project_id, id, if_match, view_dto)

Updates view by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.view_dto import ViewDTO
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
    api_instance = openapi_client.ViewsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the view
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    view_dto = openapi_client.ViewDTO() # ViewDTO | 

    try:
        # Updates view by id
        api_response = api_instance.update_view_by_id(project_id, id, if_match, view_dto)
        print("The response of ViewsApi->update_view_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->update_view_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the view | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **view_dto** | [**ViewDTO**](ViewDTO.md)|  | 

### Return type

[**ViewDTO**](ViewDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | View was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | View not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

