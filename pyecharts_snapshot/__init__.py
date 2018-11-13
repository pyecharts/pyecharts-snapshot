from lml.plugin import PluginInfo, PluginInfoChain


EXTENSION_TYPE = "pyecharts_environment"


PluginInfoChain(__name__).add_a_plugin_instance(
    PluginInfo(
        EXTENSION_TYPE,
        "%s.environment.SnapshotEnvironment" % __name__,
        tags=["png", "svg", "jpeg", "gif", "pdf", "eps"],
    )
)
