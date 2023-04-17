from mindee import Client, documents

# Init a new client and add your custom endpoint (document)
mindee_client = Client(api_key="b99503ae6741c730db66da45e7bb2767").add_endpoint(
    account_name="Utkarsh3012",
    endpoint_name="rc_front",
)

# Load a file from disk and parse it.
# The endpoint name must be specified since it cannot be determined from the class.
api_response = mindee_client.doc_from_path(
    "Bill and RC\RC1.1.jpg"
).parse(documents.TypeCustomV1, endpoint_name="rc_front")

# Print a brief summary of the parsed data
print(api_response.document)
