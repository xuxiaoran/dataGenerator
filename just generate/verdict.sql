DROP TABLE IF EXISTS Transactions, Customers, Stores, Products, Baskets, Time;

CREATE TABLE Time(
time_sqp INT NOT NULL,
time_code VARCHAR(6) NOT NULL PRIMARY KEY,
time_from VARCHAR(8) NOT NULL,
time_to VARCHAR(8) NOT NULL
);

CREATE TYPE sensitivity AS ENUM ('LA', 'MM', 'UM', 'XX');

CREATE TABLE Baskets(
bask_id BIGINT NOT NULL PRIMARY KEY,
time_code VARCHAR(6) NOT NULL,
bask_size VARCHAR(1) NOT NULL CHECK (bask_size IN('S', 'M', 'L')),
bask_price_sensitivity SENSITIVITY NOT NULL,
shop_mission VARCHAR(20) NOT NULL CHECK (shop_mission IN ('Small Shop', 'Top Up', 'Full Shop', 'XX')),
dominant_mission VARCHAR(10) CHECK (dominant_mission IN ('Fresh', 'Grocery', 'Mixed', 'Non Food', 'XX')),
FOREIGN KEY (time_code) REFERENCES Time(time_code)
);

CREATE TABLE Products(
prod_id BIGINT NOT NULL PRIMARY KEY,
prod_code VARCHAR(100) NOT NULL,
prod_desc TEXT,
prod_level10 VARCHAR(100) NOT NULL,
prod_level10_desc TEXT,
prod_level20 VARCHAR(100) NOT NULL,
prod_level20_desc TEXT,
prod_level30 VARCHAR(100) NOT NULL,
prod_level30_desc TEXT,
prod_level40 VARCHAR(100) NOT NULL,
prod_level40_desc TEXT
);

CREATE TABLE Stores(
store_id BIGINT NOT NULL PRIMARY KEY,
store_code VARCHAR(50) NOT NULL,
store_name VARCHAR(100),
store_format VARCHAR(2) NOT NULL CHECK (store_format IN ('LS', 'MS', 'SS', 'XLS')),
store_region VARCHAR(30) NOT NULL
);

CREATE TABLE Customers(
cust_id BIGINT NOT NULL PRIMARY KEY,
cust_code VARCHAR(100),
pref_store_id BIGINT,
price_sensitivity SENSITIVITY,
lifestage VARCHAR(2) CHECK (lifestage IN ('YA', 'OA', 'YF', 'OF', 'PE', 'OT', 'XX'))
);

CREATE TABLE Transactions(
bask_id BIGINT NOT NULL,
prod_id BIGINT NOT NULL,
store_id BIGINT NOT NULL,
cust_id BIGINT NOT NULL,
quantity INT NOT NULL,
spend NUMERIC(5,2) NOT NULL,
shop_date VARCHAR(8) NOT NULL,
time_code VARCHAR(6) NOT NULL,
weekday VARCHAR(1) NOT NULL CHECK (weekday IN ('1', '2', '3', '4', '5', '6', '7')),
hour VARCHAR(2) NOT NULL CHECK (hour IN ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14',
			'15','16','17','18','19','20','21','22','23')),
PRIMARY KEY(bask_id, prod_id),
FOREIGN KEY (bask_id) REFERENCES Baskets(bask_id),
FOREIGN KEY (prod_id) REFERENCES Products(prod_id),
FOREIGN KEY (store_id) REFERENCES Stores(store_id),
FOREIGN KEY (cust_id) REFERENCES Customers(cust_id)
);

