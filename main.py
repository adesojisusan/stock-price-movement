import sys, json
struct = {}
try:
  try: #try parsing to dict
    dataform = str(response_json).strip("'<>() ").replace('\'', '\"')
    struct = json.loads(dataform)
