הרצת דוקר kafka

docker run -d -p 9092:9092 --name broker apache/kafka:latest


הרצת דוקר alastic


docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.10.2
