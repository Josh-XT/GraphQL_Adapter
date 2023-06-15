from python_graphql_client import GraphqlClient
import os


async def graphql_request(
    query, variables, graphql_server, headers={}, query_path="./gql"
):
    headers.append({"Content-Type": "application/json"})
    graphql_client = GraphqlClient(
        endpoint=graphql_server,
        headers=headers,
    )
    query_file = os.path.join(os.getcwd(), query_path, f"{query}.gql")
    with open(query_file, "r") as f:
        query_data = f.read()
    data = await graphql_client.execute_async(query=query_data, variables=variables)
    if data != None:
        while not isinstance(data, list):
            data = data.popitem()[1]
    if "mutation" in query_data:
        if "returning" in data:
            data = data["returning"]
            if isinstance(data, list):
                data = data[0]
        else:
            if isinstance(data, list):
                data = data[0]
    if len(data) == 1:
        if isinstance(data, list):
            data = data[0]
    return data
