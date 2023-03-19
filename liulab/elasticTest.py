# !/usr/bin/python3
from elasticsearch import Elasticsearch
import pprint
# 连接ES,注意version
es = Elasticsearch([{'host':'116.205.232.152','port':9200}], timeout=3600)
# 查询
query = {
  "query": {
    # "match_all": {}
        "match": {
            "Metabolite ID" : "sucrose"
        }
  }
}

result = es.search(index="metabolitekegg", body=query)

pprint.pprint(result)
# print(result.keys())
# pprint.pprint(result['hits']['hits'][0]["_source"]["KEGG api"])
print()
# result['hits']
# print(result)