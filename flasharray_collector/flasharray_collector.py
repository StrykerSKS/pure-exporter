from .flasharray_metrics.flasharray import FlashArray
from .flasharray_metrics.array_info_metrics import ArrayInfoMetrics
from .flasharray_metrics.array_hardware_metrics import ArrayHardwareMetrics
from .flasharray_metrics.array_events_metrics import ArrayEventsMetrics
from .flasharray_metrics.array_space_metrics import ArraySpaceMetrics
from .flasharray_metrics.array_performance_metrics import ArrayPerformanceMetrics
from .flasharray_metrics.volume_space_metrics import VolumeSpaceMetrics
from .flasharray_metrics.volume_performance_metrics import VolumePerformanceMetrics
from .flasharray_metrics.host_space_metrics import HostSpaceMetrics
from .flasharray_metrics.host_performance_metrics import HostPerformanceMetrics
from .flasharray_metrics.pod_status_metrics import PodStatusMetrics
from .flasharray_metrics.pod_space_metrics import PodSpaceMetrics
from .flasharray_metrics.pod_performance_metrics import PodPerformanceMetrics


class FlasharrayCollector():
    """
    Instantiates the collector's methods and properties to retrieve status,
    space occupancy and performance metrics from Puretorage FlasBlade.
    Provides also a 'collect' method to allow Prometheus client registry
    to work properly.
    :param target: IP address or domain name of the target array's management
                   interface.
    :type target: str
    :param api_token: API token of the user with which to log in.
    :type api_token: str
    """
    def __init__(self, endpoint, api_token, request = 'all'):
        # self.fb = PurityFb(endpoint, conn_timeo=ctimeo, read_timeo=rtimeo, retries=retries)
        self.fa = FlashArray(endpoint, api_token)
        self.request = request

    def collect(self):
        """Global collector method for all the collected array metrics."""
        if self.request in ['all', 'array']:
            yield from ArrayInfoMetrics(self.fa).get_metrics()
            yield from ArrayHardwareMetrics(self.fa).get_metrics()
            yield from ArrayEventsMetrics(self.fa).get_metrics()
            yield from ArraySpaceMetrics(self.fa).get_metrics()
            yield from ArrayPerformanceMetrics(self.fa).get_metrics()
        if self.request in ['all', 'volumes']:
            yield from VolumeSpaceMetrics(self.fa).get_metrics()
            yield from VolumePerformanceMetrics(self.fa).get_metrics()
        if self.request in ['all', 'hosts']:
            yield from HostSpaceMetrics(self.fa).get_metrics()
            yield from HostPerformanceMetrics(self.fa).get_metrics()
        if self.request in ['all', 'pods']:
            yield from PodStatusMetrics(self.fa).get_metrics()
            yield from PodSpaceMetrics(self.fa).get_metrics()
            yield from PodPerformanceMetrics(self.fa).get_metrics()