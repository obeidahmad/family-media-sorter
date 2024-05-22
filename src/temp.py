def build_tree_from_paths(paths):
    output = []
    root = {"children": output}
    helper = {}

    for path in paths:
        current = root
        subpath = ""
        for segment in path.split("/"):
            if "children" not in current:
                current["children"] = []
            subpath += "/" + segment
            if subpath not in helper:
                helper[subpath] = {"label": segment}
            current["children"].append(helper[subpath])
            current = helper[subpath]

    return output

# Example usage:
paths = [
    "VP Accounting/iWay/Universidad de Especialidades del Espíritu Santo",
    "VP Accounting/iWay/Marmara University",
    "VP Accounting/iWay/Baghdad College of Pharmacy",
    "VP Accounting/KDB/Latvian University of Agriculture",
    "VP Accounting/KDB/Dublin Institute of Technology",
]

json_tree = build_tree_from_paths(paths)
print(json_tree)