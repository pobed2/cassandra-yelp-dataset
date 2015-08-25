CREATE TYPE business_hours (
  open text,
  close text
);

CREATE TABLE businesses(
  business_id text PRIMARY KEY,
  full_address text,
  hours map<text, frozen<business_hours>>,
  open boolean,
  categories list<text>,
  city text,
  review_count int,
  name text,
  neighborhoods list<text>,
  longitude double,
  latitude double,
  state text,
  stars decimal,
  attributes map<text, boolean>,
  type text
);

CREATE TABLE reviews(
  review_id text PRIMARY KEY,
  user_id text,
  business_id text,
  votes map<text, int>,
  stars decimal,
  date text,
  text text,
  type text
);

CREATE TABLE users(
  user_id text PRIMARY KEY,
  name text,
  yelping_since text,
  votes map<text, int>,
  review_count int,
  friends set<text>,
  fans int,
  average_stars double,
  type text,
  compliments map<text, int>,
  elite set<int>
);

CREATE TABLE tips(
  tip_id uuid PRIMARY KEY,
  user_id text,
  text text,
  business_id text,
  likes int,
  date text,
  type text
);

CREATE TABLE checkin_info(
  checkin_id uuid PRIMARY KEY,
  checkin_info map<text, int>,
  business_id text,
  type text
);
