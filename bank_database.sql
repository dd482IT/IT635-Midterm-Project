CREATE TABLE "clients" (
  "client_id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "user_name" varchar,
  "created_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "accounts" (
  "acccount_id" int PRIMARY KEY,
  "client_id" int,
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

ALTER TABLE "accounts" ADD FOREIGN KEY ("client_id") REFERENCES "clients" ("user_name");

ALTER TABLE "transactions" ADD FOREIGN KEY ("from_id") REFERENCES "accounts" ("acccount_id");

ALTER TABLE "transactions" ADD FOREIGN KEY ("to_id") REFERENCES "accounts" ("acccount_id");
