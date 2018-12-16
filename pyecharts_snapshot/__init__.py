from lml.plugin import PluginInfo, PluginInfoChain
from pyecharts_snapshot.main import SUPPORTED_IMAGE_FORMATS

EXTENSION_TYPE = "pyecharts_environment"


PluginInfoChain(__name__).add_a_plugin_instance(
    PluginInfo(
        EXTENSION_TYPE,
        "%s.environment.SnapshotEnvironment" % __name__,
        tags=list(SUPPORTED_IMAGE_FORMATS),
    )
)
