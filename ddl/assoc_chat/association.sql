create table association
(
    nom         varchar(100) null,
    rna         varchar(100) not null
        primary key,
    adresse     varchar(100) null,
    code_postal int          null,
    ville       varchar(100) null,
    telephone   varchar(100) null
);

