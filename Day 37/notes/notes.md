# Day 37 Notes:

---

### HTTP Requests:

#### GET

The `get` method is used to request data through an **API**.
```python
requests.get("")
```
The parameters for the `get` method are passed within the parentheses of the 
request.

#### POST

The `post` method is used to add data to an external system; the only 
response we're interested in is if the data was added successfully.
```python
requests.post("")
```

#### PUT

The `put` method updates data already on an external system.  Like a `post` 
request, the programmer is typically interested in a response that indicates 
success.
```python
requests.put("")
```

#### DELETE

The `delete` method is simply that: the user wants to delete some portion of 
data off of an external system.
```python
requests.delete("")
```

#### HEADERS

A `header` is a part of a request that exists as an individual parameter 
that is typically required by **API Requests**. The **API** documentation 
will typically explain what headers are required & how they need to be 
formatted:
```python
headers = {
		"X_USER_TOKEN": TOKEN,
}
```

