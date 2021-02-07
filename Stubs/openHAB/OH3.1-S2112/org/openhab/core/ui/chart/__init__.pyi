import java.awt.image
import java.lang
import java.util
import org
import typing


class ChartProvider(java.lang.Object):
    """
    public interface ChartProvider
    
        Defines the interface for chart providers. A chart provider interfaces with the persistence store to get the data and
        receives parameters from the UI chart servlet and returns a chart image object (PNG).
    
    
    """
    def createChart(self, service: java.lang.String, theme: java.lang.String, startTime: java.util.Date, endTime: java.util.Date, height: int, width: int, items: java.lang.String, groups: java.lang.String, dpi: int, legend: bool) -> java.awt.image.BufferedImage: ...
    def getChartType(self) -> 'ChartProvider.ImageType': ...
    def getName(self) -> java.lang.String: ...
    class ImageType(java.lang.Enum[org.openhab.core.ui.chart.ChartProvider.ImageType]):
        """
        Java class 'org.openhab.core.ui.chart.ChartProvider$ImageType'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            png (org.openhab.core.ui.chart.ChartProvider$ImageType): final static enum constant
            jpg (org.openhab.core.ui.chart.ChartProvider$ImageType): final static enum constant
            gif (org.openhab.core.ui.chart.ChartProvider$ImageType): final static enum constant
        
        """
        png: typing.ClassVar['ChartProvider.ImageType'] = ...
        jpg: typing.ClassVar['ChartProvider.ImageType'] = ...
        gif: typing.ClassVar['ChartProvider.ImageType'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, name: java.lang.String) -> 'ChartProvider.ImageType': ...
        @classmethod
        def values(cls) -> typing.List['ChartProvider.ImageType']: ...
