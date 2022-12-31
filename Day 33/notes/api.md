# API's:

---

An **API** (or **Application Programming Interface**) is a set of 
commands, functions, protocols, and objects that programmers can use 
to create software or _interact with an external system_.

For purposes of this course, we will use **API's** as a means to 
interact with various websites and pull live data from those websites.

Essentially, the **API** is an interface (or rather, sort of a 
barrier) between your program and an external system. Each **API** has 
rules that are prescribed to make a request to the external system 
for some piece of data. If we have structured our request according 
to all of the requirements that this external system has set out in 
the **API** documentation, then the **API** will respond appropriately 
and give us the data that we want.

A good metaphor for **API's** is that we (_the programmers_) are customers 
at a restaurant and all of the data that we want is held in the 
kitchen (_the external system_) and the data that we want specifically 
is outlined in the menu (_API documentation_).

---

### API Endpoints / API Requests:

The **API Endpoint** is typically a `url` where the user's request 
is made for some particular data. An **API Request** is the method 
or protocol for a user requesting data from the **API Endpoint**. 
The **API Documentation** is the document (or documents) that 
outline the construction of these requests. These requests are 
sometimes referred to a `get` requests. **API** data can come in 
many forms, but one of the most popular formats for this data is `.
json`, or, **JavaScript Object Notation**. Fortunately, `.json` data 
is easy to use in **Python** since it mimics `dictionaries`.

---

### HTTP Codes, Exceptions, & JSON Data:

When we use the `print()` function on an **API** request, that 
request will return a `response code` to our console. These codes 
are typically enumerated in the **API documentation** but they also 
tell the user whether or not the request was successful or if it 
failed for some reason.

Most `response codes` have general states depending on the first 
number present in the code:
```text
1XX: Hold On
(Request is ongoing & not finished or final)

2XX: Here You Go
(Request is completed, successful, and data has been transmitted)

3XX: Go Away
(Request doesn't have proper permissions)

4XX: You Screwed Up
(Request isn't formed correctly or seeks non-existent data)

5XX: I Screwed Up
(The external service is experiencing issues)
```

In **Python**, one of the more popular libraries for handling **API** 
requests is the `requests` library. Within the library, there is a method 
called `.raise_for_status()` that will raise `exceptions` without us having 
to program for them ourselves. Here is an example:
```python
response = requests.get(
		url="http://api.open-notify.org/iss-now.json"
)
response.raise_for_status()
```
```text
Process finished with exit code 0
```

---

### API Parameters:

**API Parameters** are a way to give an input during a `request` that allows 
us to retrieve specific data from the request. **_NOTE_**: Not all **API**'s 
have `parameters`. The documentation for the **API** will stipulate what, if any, `parameters` exist.