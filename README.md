# Graphql Adapter Module

The `graphql_adapter` module is a Python package that simplifies interactions with GraphQL servers. It abstracts away some of the pain points of using Python with GraphQL by providing a streamlined, asynchronous interface for sending GraphQL queries and mutations.

## Installation

```
pip install graphql-adapter
```

## Usage

The `graphql_adapter` module exports a single async function `graphql_request`.

Here's an example of how to use it:

```python
from graphql_adapter import graphql_request

# A simple example query
query = """
query {
  test {
    field1
    field2
  }
}
"""

variables = {"key1": "value1", "key2": "value2"}

response = await graphql_request(
    query=query,
    variables=variables,
    graphql_server="http://localhost:4000/graphql"
)

print(response)
```

### Function Parameters

- `query`: The name of the GraphQL query or mutation. This should match the name of a `.gql` file in your `query_path` directory.
- `variables`: A dictionary of variables to pass to the GraphQL query or mutation.
- `graphql_server`: The URL of your GraphQL server.
- `headers` (optional): A dictionary of headers to include in the request. Default is an empty dictionary.
- `query_path` (optional): The relative path to the directory containing your `.gql` files. Default is `./gql`.

### Return Values

The function will return the data from the GraphQL server's response. This data is processed as follows:

1. If the server returns an error, the function will raise an exception.
2. If the query was a mutation and the data contains a `returning` field, the function will return the value of the `returning` field.
3. If the data is a list, the function will return the first item in the list.
4. If the data is a dictionary with only one item, the function will return that item.

Please note that due to the async nature of the function, you should `await` the function call to get the response.