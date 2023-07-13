
def test_update_col():
    col = "prefix_test"
    dict = {"target": {}}
    list = {
        "code": "test_code"
    }

    update_col(col, dict, list)
    
    expected = {"target": {"test": [list]}}
    assert dict == expected

def update_col(target_col: str, result_dict: dict, list: list):
    prefix = "prefix_"
    if target_col.startswith(prefix):
        col_without_prefix = target_col.replace(prefix, "")
        if col_without_prefix not in result_dict["target"]:
            result_dict["target"][col_without_prefix] = []
        result_dict["target"][col_without_prefix].append(list)