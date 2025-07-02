import os
import json
from codetraverse.adapters.typescript_adapter import adapt_typescript_components

def test_typescript_adapter_from_extracted_json():
    fdep_dir = "output/fdep"
    extracted_components = []

    for file in ["index.ts.json", "models.ts.json", "types.ts.json", "utils.ts.json"]:
        path = os.path.join(fdep_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            extracted_components.extend(json.load(f))

    result = adapt_typescript_components(extracted_components)

    # ✅ Basic structure check
    assert "nodes" in result
    assert "edges" in result
    assert isinstance(result["nodes"], list)
    assert isinstance(result["edges"], list)

    # ✅ Confirm specific node exists
    node_ids = [n["id"] for n in result["nodes"]]
    assert "utils::greetUser" in node_ids
    assert "types::\"user\"" in node_ids

    # ✅ Confirm 'calls' edge exists
    has_call_edge = any(e["relation"] == "calls" and e["from"] == "utils::greetUser" for e in result["edges"])
    assert has_call_edge

    # ✅ Confirm 'type_dependency' edges exist
    has_type_dep = any(e["relation"] == "type_dependency" for e in result["edges"])
    assert has_type_dep
