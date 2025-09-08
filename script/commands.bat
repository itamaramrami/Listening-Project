הרצת דוקר kafka

docker run -d -p 9092:9092 --name broker apache/kafka:latest


הרצת דוקר alastic


docker run -d --name elasticsearch --network my_network -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.10.2



הרצת docker mongo
docker run -d --name mongomes -p 27017:27017 mongo:latest


docker run -d --name kibana --network my_network -p 5601:5601 kibana:tag


docker run -d --name kibana --network my_network -p 5601:5601 -e ELASTICSEARCH_HOSTS=http:elasticsearch:9200
docker.elastic.co/kibana/kibana:8.12.1