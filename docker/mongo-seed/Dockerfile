FROM mongo
COPY init.json /init.json
CMD mongoimport --host mongodb --db gitH    ub --collection issues --type json --file /init.json --jsonArray