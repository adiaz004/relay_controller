# Relay Controller

## Usage

ALL responses will have the form:

```json
{
    "data" "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

### List all relays

**Definition**

`GET /relays`

**Response**

- `200 OK` on success

```json
[
    {
        "id": "0",
        "name": "Useful Name",
        "gpio": "gpio pin"
    },
    {
        "id": "1",
        "name": "Another useful name",
        "gpio": "gpio pin"
    }
]
```

### List one relay

**Definition**

`GET /relays/<identifier>`

**Response**

- `200 OK` on success

```json
[
    {
        "id": "0",
        "name": "Useful Name",
        "gpio": "gpio pin"
    }
]
```

### Register a new relay

**Definition**

`POST /relays`

**Arguments**

- `"id":"string"` a globally unique id for this relay
- `"name":"string"` a friendly name for this relay
- `"gpio":"gpio pin"` gpio pin attached to relay

**Response**

- `201 Created` on success

```json
{
    "id": "0",
    "name": "Useful Name",
    "gpio": "gpio pin"
}
```

### Delete a relay

**Definition**

`DELETE /relays/<identifier>`

**Response**

- `404 Not Found` if device doesn't exist
- `204 No Content` on delete

```json
{
    "id": "0",
    "name": "Useful Name",
    "gpio": "gpio pin"
}
```