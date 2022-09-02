-- settings.sql
	CREATE DATABASE wabi;
	CREATE USER wabiuser WITH PASSWORD 'wabi';
	GRANT ALL PRIVILEGES ON DATABASE wabi name TO wabiuser;
