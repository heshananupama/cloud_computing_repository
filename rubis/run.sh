echo Starting mysql
/usr/sbin/service mysql start

echo Starting apache
/usr/sbin/service apache2 start

echo Waiting for services to start
sleep 3

echo Initializing DB
mysql -uroot -e "CREATE DATABASE rubis;"
mysql -uroot rubis < database/rubis.sql
mysql -uroot rubis < database/categories.sql
mysql -uroot rubis < database/regions.sql

cd Client/
make client
make initDBSQL PARAM="all"

echo Running benchmark
make emulator
