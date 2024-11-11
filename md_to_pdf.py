from spire.doc import *
from spire.doc.common import *

doc = Document()
doc.LoadFromFile('./python_01综合作业.md',FileFormat.Markdown)
doc.SaveToFile('./python_01综合作业.pdf',FileFormat.PDF)
doc.Dispose()
