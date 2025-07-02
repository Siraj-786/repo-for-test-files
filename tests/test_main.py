# import os
# import shutil
# import tempfile
# from pathlib import Path
# from unittest.mock import patch, MagicMock
# import networkx as nx

# from codetraverse.main import create_fdep_data

# @patch("codetraverse.main.get_extractor")
# @patch("codetraverse.main.load_components_without_hash")
# @patch("codetraverse.main.build_graph_from_schema")
# @patch("codetraverse.main.adapter_map", {"python": lambda x: {"nodes": [], "edges": []}})
# def test_create_fdep_data_creates_expected_files(
#     mock_build_graph, mock_load_components, mock_get_extractor
# ):
#     # Setup mock extractor
#     mock_extractor = MagicMock()
#     mock_extractor.process_file.return_value = None
#     mock_extractor.write_to_file.return_value = None
#     mock_get_extractor.return_value = mock_extractor

#     # Mock load_components to return dummy functions
#     mock_load_components.return_value = [
#         {"file_path": "some_file.py", "name": "dummy_func"}
#     ]

#     # Use a real graph instead of mock
#     G = nx.Graph()
#     G.add_node("a")
#     G.add_node("b")
#     G.add_edge("a", "b")
#     mock_build_graph.return_value = G

#     # Create a temporary test repo
#     with tempfile.TemporaryDirectory() as tmpdir:
#         # Add a dummy Python file
#         file_path = Path(tmpdir) / "example.py"
#         file_path.write_text("def foo(): pass")

#         output_dir = Path(tmpdir) / "output"
#         graph_dir = Path(tmpdir) / "graph"

#         # Run the function
#         create_fdep_data(
#             root_dir=str(tmpdir),
#             output_base=str(output_dir),
#             graph_dir=str(graph_dir),
#             clear_existing=True,
#         )

#         # Check that output files were created
#         graphml_file = graph_dir / "repo_function_calls.graphml"
#         gpickle_file = graph_dir / "repo_function_calls.gpickle"

#         assert graphml_file.exists()
#         assert gpickle_file.exists()
