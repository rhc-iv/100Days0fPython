# Type Hints:

---

**Type Hints** are ways that we can define particular `data types` within 
our **Python** code so that we have hints, or hover-over messages, that tell us 
the `data type` required, as in a `variable` or a `function`. The `data 
type` gets nested in a `function` as below. Also note that the `output` type 
can be specified as well using the `->` symbol:
```python
def greeting(name: str) -> str:
	return 'Hello' + name
```