# Ticket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**strategy** | **str** |  | 
**attempts** | **int** |  | [optional] 
**expire_at** | **int** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.ticket import Ticket

# TODO update the JSON string below
json = "{}"
# create an instance of Ticket from a JSON string
ticket_instance = Ticket.from_json(json)
# print the JSON string representation of the object
print(Ticket.to_json())

# convert the object into a dict
ticket_dict = ticket_instance.to_dict()
# create an instance of Ticket from a dict
ticket_from_dict = Ticket.from_dict(ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


