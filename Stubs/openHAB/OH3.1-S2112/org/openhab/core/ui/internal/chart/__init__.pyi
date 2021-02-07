import java.lang
import java.util
import javax.servlet
import org.openhab.core.io.http.servlet
import org.openhab.core.ui.chart
import org.osgi.service.http
import typing


class ChartServlet(org.openhab.core.io.http.servlet.OpenHABServlet):
    """
    Java class 'org.openhab.core.ui.internal.chart.ChartServlet'
    
        Extends:
            org.openhab.core.io.http.servlet.OpenHABServlet
    
      Constructors:
        * ChartServlet(org.osgi.service.http.HttpService, org.osgi.service.http.HttpContext)
    
      Attributes:
        SERVLET_NAME (java.lang.String): final static field
    
    """
    SERVLET_NAME: typing.ClassVar[java.lang.String] = ...
    def __init__(self, httpService: org.osgi.service.http.HttpService, httpContext: org.osgi.service.http.HttpContext): ...
    def addChartProvider(self, provider: org.openhab.core.ui.chart.ChartProvider) -> None: ...
    def destroy(self) -> None: ...
    @classmethod
    def getChartProviders(cls) -> java.util.Map[java.lang.String, org.openhab.core.ui.chart.ChartProvider]: ...
    def getServletConfig(self) -> javax.servlet.ServletConfig: ...
    def getServletInfo(self) -> java.lang.String: ...
    @typing.overload
    def init(self) -> None: ...
    @typing.overload
    def init(self, config: javax.servlet.ServletConfig) -> None: ...
    def removeChartProvider(self, provider: org.openhab.core.ui.chart.ChartProvider) -> None: ...
