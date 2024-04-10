create table auth_group
(
    id   integer      not null
        primary key autoincrement,
    name varchar(150) not null
        unique
);

create table django_content_type
(
    id        integer      not null
        primary key autoincrement,
    app_label varchar(100) not null,
    model     varchar(100) not null
);

create table auth_permission
(
    id              integer      not null
        primary key autoincrement,
    content_type_id integer      not null
        references django_content_type
            deferrable initially deferred,
    codename        varchar(100) not null,
    name            varchar(255) not null
);

create table auth_group_permissions
(
    id            integer not null
        primary key autoincrement,
    group_id      integer not null
        references auth_group
            deferrable initially deferred,
    permission_id integer not null
        references auth_permission
            deferrable initially deferred
);

create index auth_group_permissions_group_id_b120cbf9
    on auth_group_permissions (group_id);

create unique index auth_group_permissions_group_id_permission_id_0cd325b0_uniq
    on auth_group_permissions (group_id, permission_id);

create index auth_group_permissions_permission_id_84c5c92e
    on auth_group_permissions (permission_id);

create index auth_permission_content_type_id_2f476e4b
    on auth_permission (content_type_id);

create unique index auth_permission_content_type_id_codename_01ab375a_uniq
    on auth_permission (content_type_id, codename);

create unique index django_content_type_app_label_model_76bd3d3b_uniq
    on django_content_type (app_label, model);

create table django_migrations
(
    id      integer      not null
        primary key autoincrement,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime     not null
);

create table django_session
(
    session_key  varchar(40) not null
        primary key,
    session_data text        not null,
    expire_date  datetime    not null
);

create index django_session_expire_date_a5c62663
    on django_session (expire_date);

create table sqlite_master
(
    type     TEXT,
    name     TEXT,
    tbl_name TEXT,
    rootpage INT,
    sql      TEXT
);

create table sqlite_sequence
(
    name,
    seq
);

create table users_user
(
    id           integer      not null
        primary key autoincrement,
    last_login   datetime,
    is_superuser bool         not null,
    email        varchar(254) not null
        unique,
    password     varchar(128) not null,
    name         varchar(30)  not null,
    is_active    bool         not null,
    is_staff     bool         not null,
    created_at   datetime     not null,
    updated_at   datetime     not null
);

create table contacts_contact
(
    id                integer     not null
        primary key autoincrement,
    name              varchar(30) not null,
    email             varchar(254),
    phone             varchar(20),
    company           varchar(30),
    position          varchar(30),
    memo              text,
    profile_image_url varchar(200),
    address           varchar(100),
    birthday          date,
    website           varchar(200),
    created_at        datetime    not null,
    updated_at        datetime    not null,
    owner_id          bigint      not null
        references users_user
            deferrable initially deferred
);

create index contacts_contact_owner_id_0103c1ee
    on contacts_contact (owner_id);

create table contacts_contactlabel
(
    id         integer     not null
        primary key autoincrement,
    name       varchar(30) not null,
    created_at datetime    not null,
    updated_at datetime    not null,
    owner_id   bigint      not null
        references users_user
            deferrable initially deferred
);

create table contacts_contact_labels
(
    id              integer not null
        primary key autoincrement,
    contact_id      bigint  not null
        references contacts_contact
            deferrable initially deferred,
    contactlabel_id bigint  not null
        references contacts_contactlabel
            deferrable initially deferred
);

create index contacts_contact_labels_contact_id_2e8fb410
    on contacts_contact_labels (contact_id);

create unique index contacts_contact_labels_contact_id_contactlabel_id_6725807f_uniq
    on contacts_contact_labels (contact_id, contactlabel_id);

create index contacts_contact_labels_contactlabel_id_c744f29e
    on contacts_contact_labels (contactlabel_id);

create index contacts_contactlabel_owner_id_e81400a0
    on contacts_contactlabel (owner_id);

create table django_admin_log
(
    id              integer           not null
        primary key autoincrement,
    action_time     datetime          not null,
    object_id       text,
    object_repr     varchar(200)      not null,
    change_message  text              not null,
    content_type_id integer
        references django_content_type
            deferrable initially deferred,
    user_id         bigint            not null
        references users_user
            deferrable initially deferred,
    action_flag     smallint unsigned not null,
    check ("action_flag" >= 0)
);

create index django_admin_log_content_type_id_c4bce8eb
    on django_admin_log (content_type_id);

create index django_admin_log_user_id_c564eba6
    on django_admin_log (user_id);

create table users_user_groups
(
    id       integer not null
        primary key autoincrement,
    user_id  bigint  not null
        references users_user
            deferrable initially deferred,
    group_id integer not null
        references auth_group
            deferrable initially deferred
);

create index users_user_groups_group_id_9afc8d0e
    on users_user_groups (group_id);

create index users_user_groups_user_id_5f6f5a90
    on users_user_groups (user_id);

create unique index users_user_groups_user_id_group_id_b88eab82_uniq
    on users_user_groups (user_id, group_id);

create table users_user_user_permissions
(
    id            integer not null
        primary key autoincrement,
    user_id       bigint  not null
        references users_user
            deferrable initially deferred,
    permission_id integer not null
        references auth_permission
            deferrable initially deferred
);

create index users_user_user_permissions_permission_id_0b93982e
    on users_user_user_permissions (permission_id);

create index users_user_user_permissions_user_id_20aca447
    on users_user_user_permissions (user_id);

create unique index users_user_user_permissions_user_id_permission_id_43338c45_uniq
    on users_user_user_permissions (user_id, permission_id);

