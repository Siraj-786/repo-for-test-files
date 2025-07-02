from codetraverse.main import create_fdep_data

create_fdep_data(
    root_dir="sample_code_repos/test_typescript_full",
    output_base="output/fdep1",
    graph_dir="output/graph",
    clear_existing=True
)