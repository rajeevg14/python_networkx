import matplotlib.pyplot as plt
import networkx as nx
from networkx.readwrite import node_link_graph

G = node_link_graph({'directed': True, 'multigraph': False, 'graph': {}, 'nodes': [{'id': 'build'}, {'id': 'root'}, {'id': 'utils'}, {'id': 'codegen'}, {'id': 'codegen.templates'}, {'id': 'nodes.shapes'}, {'id': 'codegen.c_types'}, {'id': 'nodes'}, {'id': 'containers'}, {'id': 'distutils'}, {'id': 'wheel'}, {'id': 'tools.testing'}, {'id': 'finalizations'}, {'id': 'importing'}, {'id': 'plugins'}, {'id': 'freezer'}, {'id': 'tree'}, {'id': 'specs'}, {'id': 'optimizations'}, {'id': 'plugins.standard'}, {'id': 'tools.general.dll_report'}, {'id': 'tools.specialize'}, {'id': 'tools.testing.compare_with_cpython'}, {'id': 'tools.testing.find_sxs_modules'}, {'id': 'tools.testing.measure_construct_performance'}, {'id': 'tools.testing.run_root_tests'}, {'id': 'tools'}], 'links': [{'source': 'build', 'target': 'root'}, {'source': 'build', 'target': 'utils'}, {'source': 'root', 'target': 'root'}, {'source': 'root', 'target': 'containers'}, {'source': 'root', 'target': 'utils'}, {'source': 'root', 'target': 'finalizations'}, {'source': 'root', 'target': 'freezer'}, {'source': 'root', 'target': 'plugins'}, {'source': 'root', 'target': 'nodes.shapes'}, {'source': 'utils', 'target': 'root'}, {'source': 'utils', 'target': 'utils'}, {'source': 'codegen', 'target': 'codegen'}, {'source': 'codegen', 'target': 'codegen.templates'}, {'source': 'codegen', 'target': 'root'}, {'source': 'codegen', 'target': 'codegen.c_types'}, {'source': 'codegen', 'target': 'utils'}, {'source': 'codegen', 'target': 'nodes.shapes'}, {'source': 'codegen', 'target': 'nodes'}, {'source': 'codegen', 'target': 'containers'}, {'source': 'codegen.templates', 'target': 'root'}, {'source': 'nodes.shapes', 'target': 'codegen.c_types'}, {'source': 'nodes.shapes', 'target': 'codegen'}, {'source': 'nodes.shapes', 'target': 'root'}, {'source': 'nodes.shapes', 'target': 'nodes.shapes'}, {'source': 'codegen.c_types', 'target': 'codegen.templates'}, {'source': 'codegen.c_types', 'target': 'codegen.c_types'}, {'source': 'codegen.c_types', 'target': 'codegen'}, {'source': 'nodes', 'target': 'containers'}, {'source': 'nodes', 'target': 'utils'}, {'source': 'nodes', 'target': 'nodes.shapes'}, {'source': 'nodes', 'target': 'importing'}, {'source': 'nodes', 'target': 'root'}, {'source': 'nodes', 'target': 'optimizations'}, {'source': 'nodes', 'target': 'tree'}, {'source': 'nodes', 'target': 'nodes'}, {'source': 'nodes', 'target': 'specs'}, {'source': 'containers', 'target': 'root'}, {'source': 'distutils', 'target': 'wheel'}, {'source': 'distutils', 'target': 'tools.testing'}, {'source': 'tools.testing', 'target': 'root'}, {'source': 'tools.testing', 'target': 'utils'}, {'source': 'tools.testing', 'target': 'tools.testing'}, {'source': 'finalizations', 'target': 'finalizations'}, {'source': 'finalizations', 'target': 'root'}, {'source': 'finalizations', 'target': 'importing'}, {'source': 'finalizations', 'target': 'plugins'}, {
                    'source': 'importing', 'target': 'containers'}, {'source': 'importing', 'target': 'plugins'}, {'source': 'importing', 'target': 'root'}, {'source': 'importing', 'target': 'utils'}, {'source': 'importing', 'target': 'importing'}, {'source': 'importing', 'target': 'tree'}, {'source': 'plugins', 'target': 'root'}, {'source': 'plugins', 'target': 'containers'}, {'source': 'plugins', 'target': 'utils'}, {'source': 'plugins', 'target': 'plugins'}, {'source': 'freezer', 'target': 'codegen'}, {'source': 'freezer', 'target': 'codegen.templates'}, {'source': 'freezer', 'target': 'root'}, {'source': 'freezer', 'target': 'utils'}, {'source': 'freezer', 'target': 'containers'}, {'source': 'freezer', 'target': 'importing'}, {'source': 'freezer', 'target': 'nodes'}, {'source': 'freezer', 'target': 'plugins'}, {'source': 'freezer', 'target': 'tree'}, {'source': 'freezer', 'target': 'freezer'}, {'source': 'tree', 'target': 'root'}, {'source': 'tree', 'target': 'plugins'}, {'source': 'tree', 'target': 'utils'}, {'source': 'tree', 'target': 'tree'}, {'source': 'tree', 'target': 'nodes'}, {'source': 'tree', 'target': 'optimizations'}, {'source': 'tree', 'target': 'freezer'}, {'source': 'tree', 'target': 'importing'}, {'source': 'tree', 'target': 'specs'}, {'source': 'specs', 'target': 'root'}, {'source': 'specs', 'target': 'specs'}, {'source': 'specs', 'target': 'utils'}, {'source': 'optimizations', 'target': 'root'}, {'source': 'optimizations', 'target': 'importing'}, {'source': 'optimizations', 'target': 'nodes'}, {'source': 'optimizations', 'target': 'nodes.shapes'}, {'source': 'optimizations', 'target': 'tree'}, {'source': 'optimizations', 'target': 'utils'}, {'source': 'optimizations', 'target': 'optimizations'}, {'source': 'optimizations', 'target': 'plugins'}, {'source': 'plugins.standard', 'target': 'root'}, {'source': 'plugins.standard', 'target': 'plugins'}, {'source': 'plugins.standard', 'target': 'containers'}, {'source': 'plugins.standard', 'target': 'utils'}, {'source': 'tools.general.dll_report', 'target': 'freezer'}, {'source': 'tools.general.dll_report', 'target': 'utils'}, {'source': 'tools.specialize', 'target': 'codegen'}, {'source': 'tools.specialize', 'target': 'root'}, {'source': 'tools.testing.compare_with_cpython', 'target': 'root'}, {'source': 'tools.testing.compare_with_cpython', 'target': 'tools.testing'}, {'source': 'tools.testing.compare_with_cpython', 'target': 'utils'}, {'source': 'tools.testing.find_sxs_modules', 'target': 'tools.testing'}, {'source': 'tools.testing.find_sxs_modules', 'target': 'root'}, {'source': 'tools.testing.find_sxs_modules', 'target': 'utils'}, {'source': 'tools.testing.measure_construct_performance', 'target': 'tools.testing'}, {'source': 'tools.testing.run_root_tests', 'target': 'tools'}, {'source': 'tools.testing.run_root_tests', 'target': 'tools.testing'}, {'source': 'tools.testing.run_root_tests', 'target': 'utils'}]})
nx.draw(G, with_labels=True)
plt.show()