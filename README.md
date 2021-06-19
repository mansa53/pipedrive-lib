# pipedrive-python

pipedrive-python is an API wrapper for [Pipedrive](https://www.pipedrive.com/) written in Python.

## steps to run

Run setup.py

```
python setup.py bdist_wheel
```
A dist file would be generated 
## Installing
```
pip install {path to dist file}
```

## Usage



### Using this library with API Token

#### Client instantiation
```
from pipedrive.client import Client

client = Client(domain='https://companydomain.pipedrive.com/')
```

#### Set API token in the library
```
client.set_api_token('API_TOKEN')
```



### Notes

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Notes

#### Get a note
```
response = client.notes.get_note('NOTE_ID')
```

#### Get all notes
```
response = client.notes.get_all_notes()
```

#### Add a note
```
data = {
    'content': ''
}
response = client.notes.create_note(data)
```

#### Update a note
```
data = {
    'content': ''
}
response = client.notes.update_note('NOTE_ID', data)
```

#### Delete a note
```
response = client.notes.delete_note('NOTE_ID')
```



### Persons 

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Persons

#### Get a person
```
response = client.persons.get_person('PERSON_ID')
```

#### Get all persons
```
response = client.persons.get_all_persons()
```

#### Get persons by name
```
params = {
    'term': ''
}
response = client.persons.get_persons_by_name(params=params)
```

#### Create person
```
data = {
    'name': ''
}
response = client.persons.create_person(data)
```

#### Update person
```
data = {
    'name': ''
}
response = client.persons.update_person('PERSON_ID', data)
```

#### Delete person
```
response = client.persons.delete_person('PERSON_ID')
```

#### Get deals associated with a person
```
response = client.persons.get_person_deals('PERSON_ID')
```

#### Get person fields
```
response = client.persons.get_person_fields()
```


### Webhook 

API docs: https://developers.pipedrive.com/docs/api/v1/#!/Webhooks

#### Get webhooks
```
response = client.webhooks.get_hooks_subscription()
```

#### Add webhook
```
data = {
    'subscription_url': '',
    'event_action': '',
    'event_object': ''
}
response = client.webhooks.create_hook_subscription(data)
```

#### Delete webhook
```
response = client.webhooks.delete_hook_subscription('HOOK_ID')
```

### Webhook Hit details

```
 request_string = '''
    {"v":1,"matches_filters":{"current":[]},"meta":{"action":"added","change_source":"api","company_id":7966119,"host":"demo.pipedrive.com","id":9,"is_bulk_update":false,"matches_filters":{"current":[]},"object":"person","permitted_user_ids":[12256380],"pipedrive_service_name":false,"timestamp":1624079482,"timestamp_micro":1624079482440272,"trans_pending":false,"user_id":12256380,"v":1,"webhook_id":"781914"},"current":{"related_closed_deals_count":0,"email_messages_count":0,"cc_email":"student-sandbox@pipedrivemail.com","owner_id":12256380,"open_deals_count":0,"last_outgoing_mail_time":null,"active_flag":true,"picture_id":null,"last_activity_id":null,"1d49338625a9066d827b531176c589959de0a595":"13","next_activity_date":null,"update_time":"2021-06-19 05:11:22","participant_open_deals_count":0,"activities_count":0,"id":9,"org_name":null,"first_name":"Jack","email":[{"value":"","primary":true}],"won_deals_count":0,"owner_name":"Manasa Hegde","files_count":0,"company_id":7966119,"related_won_deals_count":0,"last_incoming_mail_time":null,"first_char":"j","undone_activities_count":0,"closed_deals_count":0,"last_name":null,"last_activity_date":null,"label":null,"next_activity_id":null,"related_lost_deals_count":0,"related_open_deals_count":0,"phone":[{"value":"","primary":true}],"visible_to":"3","org_id":null,"notes_count":0,"followers_count":0,"name":"Jack","participant_closed_deals_count":0,"lost_deals_count":0,"next_activity_time":null,"add_time":"2021-06-19 05:11:22","done_activities_count":0},"previous":null,"event":"added.person","retry":0}
    '''


    data = json.loads(request_string)

    latestResponse = client.utils.getPersonDetails(data)
```


## Requirements
- requests


