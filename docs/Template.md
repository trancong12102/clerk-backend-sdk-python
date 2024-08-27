# Template


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | [optional] 
**instance_id** | **str** | the id of the instance the template belongs to | [optional] 
**resource_type** | **str** | whether this is a system (default) or user overridden) template | [optional] 
**template_type** | **str** | whether this is an email or SMS template | [optional] 
**name** | **str** | user-friendly name of the template | [optional] 
**slug** | **str** | machine-friendly name of the template | [optional] 
**position** | **int** | position with the listing of templates | [optional] 
**can_revert** | **bool** | whether this template can be reverted to the corresponding system default | [optional] 
**can_delete** | **bool** | whether this template can be deleted | [optional] 
**can_toggle** | **bool** | whether this template can be enabled or disabled, true only for notification SMS templates | [optional] 
**subject** | **str** | email subject | [optional] 
**markup** | **str** | the editor markup used to generate the body of the template | [optional] 
**body** | **str** | the template body before variable interpolation | [optional] 
**available_variables** | **List[str]** | list of variables that are available for use in the template body | [optional] 
**required_variables** | **List[str]** | list of variables that must be contained in the template body | [optional] 
**from_email_name** | **str** |  | [optional] 
**reply_to_email_name** | **str** |  | [optional] 
**delivered_by_clerk** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**updated_at** | **int** | Unix timestamp of last update.  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | [optional] 

## Example

```python
from clerk_backend_sdk.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


