# !/usr/python3
# encoding = utf-8
from Bio import SeqIO
records = (r for r in SeqIO.parse("opuntia.fasta", "fasta") if len(r) < 900)
from StringIO import StringIO
handle = StringIO()
SeqIO.write(records, handle, "fasta")
data = handle.getvalue()
stdout, stderr = muscle_cline(stdin=data)
from Bio import AlignIO
align = AlignIO.read(StringIO(stdout), "clustal")
print(align)
