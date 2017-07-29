use tpch1g;

DROP TABLE IF EXISTS nation;
CREATE EXTERNAL TABLE nation  ( N_NATIONKEY  INT,
                            N_NAME       CHAR(25),
                            N_REGIONKEY  INT,
                            N_COMMENT    VARCHAR(152))
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ESCAPED BY '\\'
LOCATION '/data/tpch1g/nation';

DROP TABLE IF EXISTS region;
CREATE TABLE region  ( R_REGIONKEY  INT,
                            R_NAME       CHAR(25),
                            R_COMMENT    VARCHAR(152))
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ESCAPED BY '\\'
LOCATION '/data/tpch1g/region';

DROP TABLE IF EXISTS part;
CREATE TABLE part  ( P_PARTKEY     INT,
                          P_NAME        VARCHAR(55),
                          P_MFGR        CHAR(25),
                          P_BRAND       CHAR(10),
                          P_TYPE        VARCHAR(25),
                          P_SIZE        INT,
                          P_CONTAINER   CHAR(10),
                          P_RETAILPRICE DECIMAL(15,2),
                          P_COMMENT     VARCHAR(23))
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ESCAPED BY '\\'
LOCATION '/data/tpch1g/part';

DROP TABLE IF EXISTS supplier;
CREATE TABLE supplier ( S_SUPPKEY     INT,
                             S_NAME        CHAR(25),
                             S_ADDRESS     VARCHAR(40),
                             S_NATIONKEY   INT,
                             S_PHONE       CHAR(15),
                             S_ACCTBAL     DECIMAL(15,2),
                             S_COMMENT     VARCHAR(101))
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ESCAPED BY '\\'
LOCATION '/data/tpch1g/supplier';

DROP TABLE IF EXISTS partsupp;
CREATE TABLE partsupp ( PS_PARTKEY     INT,
                             PS_SUPPKEY     INT,
                             PS_AVAILQTY    INT,
                             PS_SUPPLYCOST  DECIMAL(15,2),
                             PS_COMMENT     VARCHAR(199))
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ESCAPED BY '\\'
LOCATION '/data/tpch1g/partsupp';

DROP TABLE IF EXISTS customer;
CREATE TABLE customer ( C_CUSTKEY     INT,
                             C_NAME        VARCHAR(25),
                             C_ADDRESS     VARCHAR(40),
                             C_NATIONKEY   INT,
                             C_PHONE       CHAR(15),
                             C_ACCTBAL     DECIMAL(15,2),
                             C_MKTSEGMENT  CHAR(10),
                             C_COMMENT     VARCHAR(117))
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ESCAPED BY '\\'
LOCATION '/data/tpch1g/customer';

DROP TABLE IF EXISTS orders;
CREATE TABLE orders  ( O_ORDERKEY       INT,
                           O_CUSTKEY        INT,
                           O_ORDERSTATUS    CHAR(1),
                           O_TOTALPRICE     DECIMAL(15,2),
                           O_ORDERDATE      TIMESTAMP,
                           O_ORDERPRIORITY  CHAR(15),  
                           O_CLERK          CHAR(15), 
                           O_SHIPPRIORITY   INT,
                           O_COMMENT        VARCHAR(79))
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ESCAPED BY '\\'
LOCATION '/data/tpch1g/orders';

DROP TABLE IF EXISTS lineitem;
CREATE TABLE lineitem ( L_ORDERKEY    INT,
                             L_PARTKEY     INT,
                             L_SUPPKEY     INT,
                             L_LINENUMBER  INT,
                             L_QUANTITY    DECIMAL(15,2),
                             L_EXTENDEDPRICE  DECIMAL(15,2),
                             L_DISCOUNT    DECIMAL(15,2),
                             L_TAX         DECIMAL(15,2),
                             L_RETURNFLAG  CHAR(1),
                             L_LINESTATUS  CHAR(1),
                             L_SHIPDATE    TIMESTAMP,
                             L_COMMITDATE  TIMESTAMP,
                             L_RECEIPTDATE TIMESTAMP,
                             L_SHIPINSTRUCT CHAR(25),
                             L_SHIPMODE     CHAR(10),
                             L_COMMENT      VARCHAR(44))
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ESCAPED BY '\\'
LOCATION '/data/tpch1g/lineitem';
