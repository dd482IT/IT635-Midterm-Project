CREATE TABLE "clients" (
  "client_id" INT IDENTITY(1,1) PRIMARY KEY,
  "user_name" varchar(255),
  "first_Name" varchar(255),
  "last_Name" varchar(255),
  "password" varchar(255), 
  "created_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "accounts" (
  "acccount_id" int PRIMARY KEY,
  "client_id" int REFERENCES clients(client_id),
  "balance" int,
  "created_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "transactions" (
  "transaction_id" int,
  "from_id" int,
  "to_id" int,
  "date_of_t" date,
  "amount" int,
  "created_at" timestamptz DEFAULT 'now()'
);

ALTER TABLE "transactions" ADD FOREIGN KEY ("from_id") REFERENCES "accounts" ("acccount_id");

ALTER TABLE "transactions" ADD FOREIGN KEY ("to_id") REFERENCES "accounts" ("acccount_id");
