# FormatDTO1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [default to 'number']
**fraction** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.format_dto1 import FormatDTO1

# TODO update the JSON string below
json = "{}"
# create an instance of FormatDTO1 from a JSON string
format_dto1_instance = FormatDTO1.from_json(json)
# print the JSON string representation of the object
print FormatDTO1.to_json()

# convert the object into a dict
format_dto1_dict = format_dto1_instance.to_dict()
# create an instance of FormatDTO1 from a dict
format_dto1_from_dict = FormatDTO1.from_dict(format_dto1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


