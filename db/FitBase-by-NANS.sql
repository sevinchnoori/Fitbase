CREATE DATABASE
IF NOT EXISTS FitBase;

grant all privileges on FitBase.* to 'webapp'@'%';
flush privileges;


USE FitBase;

CREATE TABLE
    IF NOT EXISTS Gym
(
    gid       int PRIMARY KEY,
    name      varchar(50) NOT NULL,
    openTime  time        NOT NULL,
    closeTime time        NOT NULL,
    street    varchar(50) NOT NULL,
    city      varchar(50) NOT NULL,
    state     varchar(2)  NOT NULL,
    zip       int         NOT NULL
);

CREATE TABLE
    IF NOT EXISTS MarketingConsultant
(
    mcid  int PRIMARY KEY,
    first varchar(50) NOT NULL,
    last  varchar(50) NOT NULL
);

CREATE TABLE
    IF NOT EXISTS Membership
(
    msid  int PRIMARY KEY,
    type  varchar(50) NOT NULL,
    price double      NOT NULL,
    mcid  int,
    FOREIGN KEY
        (mcid) REFERENCES MarketingConsultant
        (mcid)
);

CREATE TABLE
    IF NOT EXISTS Manager
(
    first    varchar(50) NOT NULL,
    last     varchar(50) NOT NULL,
    email    varchar(50) NOT NULL,
    phoneNum varchar(20) NOT NULL,
    mnid     int PRIMARY KEY
);

# insert into Manager(first, last, email, phoneNum, mnid)
# values ('nidhi', 'hosamane', 'dhiw', '91829', 820);
#
# select * from Manager


CREATE TABLE
    IF NOT EXISTS Member
(
    mid        int PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name  varchar(50) NOT NULL,
    gender     varchar(50) NOT NULL,
    years      int         NOT NULL NOT NULL,
    age        int         NOT NULL,
    mcid       int,
    FOREIGN KEY
        (mcid) REFERENCES MarketingConsultant
        (mcid),
    msid       int,
    FOREIGN KEY
        (msid) REFERENCES Membership
        (msid) ON UPDATE CASCADE,
    phoneNum_1 varchar(20) NOT NULL,
    phoneNum_2 varchar(20),
    email_1    varchar(50) NOT NULL,
    email_2    varchar(50)
);

# drop table Trainer;
CREATE TABLE
    IF NOT EXISTS Trainer
(
    first  varchar(50) NOT NULL,
    last   varchar(50) NOT NULL,
    tid    int PRIMARY KEY,
    gender varchar(50) NOT NULL,
    mnid   int,
    gid    int,
    mcid   int,
    FOREIGN KEY
        (mnid) REFERENCES Manager
        (mnid),
    FOREIGN KEY
        (gid) REFERENCES Gym
        (gid),
    FOREIGN KEY
        (mcid) REFERENCES MarketingConsultant
        (mcid)
);

CREATE TABLE
    IF NOT EXISTS Specialities
(
    tid       int,
    specialty varchar(50) NOT NULL,
    FOREIGN KEY
        (tid) REFERENCES Trainer
        (tid)
);

CREATE TABLE
    IF NOT EXISTS Gym_Mem
(
    mid int,
    gid int NOT NULL,
    FOREIGN KEY
        (mid) REFERENCES Member
        (mid) ON DELETE CASCADE
);

CREATE TABLE
    IF NOT EXISTS Certs
(
    tid           int,
    certification varchar(50) NOT NULL,
    FOREIGN KEY
        (tid) REFERENCES Trainer
        (tid)
);

CREATE TABLE
    IF NOT EXISTS Interests
(
    mid      int,
    interest varchar(50),
    FOREIGN KEY
        (mid) REFERENCES Member
        (mid) ON DELETE CASCADE
);

CREATE TABLE
    IF NOT EXISTS Orders
(
    totalCost double NOT NULL,
    oid       int PRIMARY KEY,
    mcid      int,
    mid       int,
    FOREIGN KEY
        (mcid) REFERENCES MarketingConsultant
        (mcid),
    FOREIGN KEY
        (mid) REFERENCES Member
        (mid) ON DELETE CASCADE
);

CREATE TABLE
    IF NOT EXISTS Product
(
    pid   int PRIMARY KEY,
    price double      NOT NULL,
    name  varchar(50) NOT NULL,
    type  varchar(50) NOT NULL
);

CREATE TABLE
    IF NOT EXISTS Equipment
(
    eid        int PRIMARY KEY,
    difficulty varchar(10)
);

CREATE TABLE
    IF NOT EXISTS Prod_Order
(
    oid int,
    pid int,
    FOREIGN KEY
        (oid) REFERENCES Orders
        (oid),
    FOREIGN KEY
        (pid) REFERENCES Product
        (pid)
);

CREATE TABLE
    IF NOT EXISTS Class
(
    cid        int PRIMARY KEY,
    activity   varchar(50) NOT NULL,
    name       varchar(50) NOT NULL,
    startTime  datetime    NOT NULL,
    endTime    datetime    NOT NULL,
    roomNum    int         NOT NULL,
    totalSeats int         NOT NULL,
    tid        int,
    FOREIGN KEY
        (tid) REFERENCES Trainer
        (tid),
    mcid       int,
    FOREIGN KEY
        (mcid) REFERENCES MarketingConsultant
        (mcid)
);

CREATE TABLE
    IF NOT EXISTS Class_Mem
(
    mid int,
    cid int,
    FOREIGN KEY
        (mid) REFERENCES Member
        (mid) ON DELETE CASCADE,
    FOREIGN KEY
        (cid) REFERENCES Class
        (cid)
);

CREATE TABLE
    IF NOT EXISTS Train_Equip
(
    tid int,
    eid int,
    FOREIGN KEY
        (tid) REFERENCES Trainer
        (tid),
    FOREIGN KEY
        (eid) REFERENCES Equipment
        (eid)
);

CREATE TABLE
    IF NOT EXISTS PersonalTraining
(
    ptid     int PRIMARY KEY,
    length   int         NOT NULL,
    activity varchar(50) NOT NULL,
    tid      int,
    FOREIGN KEY
        (tid) REFERENCES Trainer
        (tid),
    mid      int,
    FOREIGN KEY
        (mid) REFERENCES Member
        (mid) ON DELETE CASCADE
);

CREATE TABLE
    IF NOT EXISTS Discount
(
    type varchar(50) PRIMARY KEY,
    msid int,
    FOREIGN KEY
        (msid) REFERENCES Membership
        (msid) ON UPDATE CASCADE
);