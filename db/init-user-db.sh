#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE rates (
	    id 						int4 not null primary key,
        value 					int4 not null,
	    parking_space_id 	    int4 not null
    );
    
    CREATE TABLE parking_space (
	    id          int4 not null primary key,
	    "type"      varchar(50) not null,
	    count       int4 not null
    );
EOSQL