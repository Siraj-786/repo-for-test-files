import os
from codetraverse.extractors.typescript_extractor import TypeScriptComponentExtractor

def test_typescript_extractor_on_sample_repo():
    sample_path = "sample_code_repos/test_typescript_full"
    os.environ["ROOT_DIR"] = sample_path

    extractor = TypeScriptComponentExtractor()
    for filename in ["index.ts", "models.ts", "types.ts", "utils.ts"]:
        extractor.process_file(os.path.join(sample_path, filename))

    components = extractor.extract_all_components()

    # ✅ Basic checks: ensure components for function, class, variable, type_alias are found
    kinds = [comp["kind"] for comp in components]
    assert "function" in kinds
    assert "class" in kinds
    assert "variable" in kinds
    assert "type_alias" in kinds

    # ✅ Specific function check
    greet_user = [c for c in components if c["kind"] == "function" and c["name"] == "greetUser"]
    assert greet_user != []

    # ✅ Check for keyof and string literal-based type_alias
    literal = [c for c in components if c["kind"] == "literal_type" and c["value"] == '"user"']
    assert literal != []

    # ✅ Check that type dependencies (edges) are extracted
    edges = [c for c in components if c["kind"] == "edge"]
    assert any(e["relation"] == "type_dependency" for e in edges)
