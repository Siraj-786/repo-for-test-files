from codetraverse.main import create_fdep_data
import os
def test_end_to_end_graph_creation():
    create_fdep_data(
        root_dir="sample_code_repos/test_typescript_full",
        output_base="output/fdep",
        graph_dir="output/graph",
        clear_existing=True
    )

    assert os.path.exists("output/graph/repo_function_calls.graphml")
    assert os.path.exists("output/graph/repo_function_calls.gpickle")
