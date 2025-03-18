from deepdiff import DeepDiff

def compare_dicts(actual: dict, expected: dict):
    if isinstance(actual, dict) and isinstance(expected, dict):
        diff = DeepDiff(actual, expected, ignore_order=True)
        assert {} == diff, str(diff)
