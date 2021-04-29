from scrapy.exporters import BaseItemExporter
from scrapy.exporters import JsonItemExporter
from scrapy.utils.serialize import ScrapyJSONEncoder
from scrapy.utils.python import to_bytes

# Extending JsonLinesItemExporter
# JsonLinesItemExporter provides the exact same
# implementation of export_item() method.
# Therefore only start_exporting() and finish_exporting() methods are overrided.
class FanItemExporter(JsonItemExporter):

    def __init__(self, file, **kwargs):
        # To initialize the object using JsonItemExporter's constructor
        super().__init__(file)

    def start_exporting(self):
        self.file.write(b'[\n')#b'{\'product\': ['

    def finish_exporting(self):
        self.file.write(b'\n]')

"""
#using FanItemExporter beeter than BaseItemExporter
# Extending BaseItemExporter
# Since BaseItemExporter is the parent class,
# start_exporting(), finish_exporting(), export_item()
# must be overrided to suit our needs.
class FanItemExporter(BaseItemExporter):

    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file = file
        self.encoder = ScrapyJSONEncoder(**kwargs)
        self.first_item = True

    def start_exporting(self):
        self.file.write(b'[\n')

    def finish_exporting(self):
        self.file.write(b'\n]')

    def export_item(self, item):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(b',\n')
        itemdict = dict(self._get_serialized_fields(item))
        self.file.write(to_bytes(self.encoder.encode(itemdict)))
"""
