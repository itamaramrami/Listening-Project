הרצת דוקר kafka

docker run -d -p 9092:9092 --name broker apache/kafka:latest


הרצת דוקר alastic
docker run -d --name elasticsearch --net itamar -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.15.0


הרצת docker mongo
docker run -d --name mongomes -p 27017:27017 mongo:latest


הרצת docker kebana

docker run -d --name kibana --net itamar -p 5601:5601 kibana:8.15.0



R2Vub2NpZGUSV2FyIENyaW1lcyxBcGFydGhlaWQs TWFzc2FjcmUsTmFrYmEsRG1zcGxhY2 
VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUST2NjdXBhdGlvbixSZWZ1Z2V1 
cyxJQOMSQKRT


RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmN1LExpYmVyYXRpb24sRnJ1ZSBQYWx1c3Rpbm 
USR2F6YSXDZWFzZWZpcmUsUHJvdGVzdCxVT1JXQQ==