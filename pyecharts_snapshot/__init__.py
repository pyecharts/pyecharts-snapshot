from lml.plugin import PluginInfo, PluginInfoChain


PluginInfoChain(__name__).add_a_plugin_instance(
    PluginInfo(
        'pyecharts_environment',
        '%s.jupyter.SnapshotEnvironment' % __name__,
        tags=['snapshot']
    )
)
