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

## Requirements
- requests


