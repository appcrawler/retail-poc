#---------------------------------------------------------------------------------
# Stop anything currently running on this host and delete for fresh start
# change PATH to confluent executable below to wherever you have the platform installed
confluent local stop
rm -rf /tmp/confluent.*
rm -rf /var/lib/kafka
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
# sleep five seconds to ensure everything to eliminate startup errors
sleep 5
confluent local start
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
kafka-topics --bootstrap-server localhost:9092 --delete --topic inventory
kafka-topics --bootstrap-server localhost:9092 --delete --topic sales
kafka-topics --bootstrap-server localhost:9092 --delete --topic receipts
kafka-topics --bootstrap-server localhost:9092 --delete --topic SOH

kafka-topics --bootstrap-server localhost:9092 --create --topic sales --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic receipts --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --create --topic inventory --partitions 1 --replication-factor 1

cat retail.ksql | ksql
