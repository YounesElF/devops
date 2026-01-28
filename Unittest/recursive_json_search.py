def json_search(key, input_object):
    ret_val = []

    def _search(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    ret_val.append({k: v})
                if isinstance(v, (dict, list)):
                    _search(v)

        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, (dict, list)):
                    _search(item)

    _search(input_object)
    return ret_val


# Alleen voor manuele test (wordt NIET uitgevoerd bij unittest import)
if __name__ == "__main__":
    from test_data import data
    print(json_search("issueSummary", data))

