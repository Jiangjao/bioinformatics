import pandas as pd
import io
# Example data (replace this with your actual data reading logic)
data_str = """
root	Tissue	Cell	Gene	Tags
a	Breast	Epithelial cell	CD117	4,614
a	Breast	Epithelial cell	SOX2	20,859
a	Breast	Epithelial cell	SSEA-4	10,530
a	Eye	Stem cell	ABCG2	14,593
a	Eye	Stem cell	CD133	6,703
a	Eye	Stem cell	CK14	700
a	Eye	Stem cell	P63	700
a	Intestine	Endocrine cell	CD144	1,200
a	Intestine	Endocrine cell	CD146	1,880
a	Intestine	Endocrine cell	CD44	2,313
a	Kidney	T cell	c-Kit	2,832
a	Kidney	T cell	CXCR3	8,435
a	Kidney	T cell	Dectin-1	7,862
a	Kidney	T cell	deltaNp63	2,138
a	Kidney	T cell	epsilon	5,222
a	Kidney	T cell	FLT3	3,842
a	Kidney	T cell	MARCO	2,649
a	Kidney	T cell	MHC	1,353
a	Kidney	T cell	SIGLEC8	876
a	Kidney	T cell	TGF	4,665
a	Kidney	T cell	Vimentin	4,896
a	Liver	Myeloid cell	ST2	16,540
a	Lung	Macrophage	CD192	2,023
a	Lung	Fibroblast	CD25	12,870
a	Lung	Fibroblast	CD282	12,348
a	Lung	Fibroblast	CD284	4,864
a	Lung	Fibroblast	CD289	4,853
a	Lung	Fibroblast	CD294	8,411
a	Lung	Fibroblast	CD3	12,003
a	Lung	Fibroblast	iNOS	3,165
a	Lung	Basal cell	TCR	4,190
a	Lung	Fibroblast	VEGF	5,219
a	Lung	Fibroblast	ZAP70	3,509
a	Pancreas	Beta cell	CD90	3,301
a	Pancreas	Beta cell	CK15	10,349
a	Pancreas	Beta cell	CK3	11,275
a	Pancreas	Beta cell	CXCR4	9,930
a	Pancreas	Beta cell	Integrin	10,544
a	Pancreas	Beta cell	LGR5	19,788
a	Pancreas	Beta cell	NANOG	7,147
a	Pancreas	Beta cell	NOTCH1	19,382
a	Pancreas	Beta cell	OCT3-4	2,247
a	Pancreas	Beta cell	P75	5,569
a	Pancreas	Beta cell	SOD2	376
a	Pancreas	Beta cell	STRO-1	654
"""

# Read data into pandas DataFrame
df = pd.read_csv(io.StringIO(data_str), sep='\t')

# Initialize the nested structure
data = {"name": "root", "children": []}

# Group by the hierarchy and build the nested structure
for root, tissue, cell, gene, tags in df.values:
    root_node = next((child for child in data["children"] if child["name"] == root), None)
    if not root_node:
        root_node = {"name": root, "children": []}
        data["children"].append(root_node)

    tissue_node = next((child for child in root_node["children"] if child["name"] == tissue), None)
    if not tissue_node:
        tissue_node = {"name": tissue, "children": []}
        root_node["children"].append(tissue_node)

    cell_node = next((child for child in tissue_node["children"] if child["name"] == cell), None)
    if not cell_node:
        cell_node = {"name": cell, "children": []}
        tissue_node["children"].append(cell_node)

    cell_node["children"].append({"name": gene, "value": int(tags.replace(",", ""))})

# Convert to JSON
import json
json_data = json.dumps(data, indent=2)

print(json_data)
