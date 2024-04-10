INSERT INTO django_content_type (id, app_label, model) VALUES (1, 'contacts', 'contact');
INSERT INTO django_content_type (id, app_label, model) VALUES (2, 'users', 'user');
INSERT INTO django_content_type (id, app_label, model) VALUES (3, 'contacts', 'contactlabel');

INSERT INTO users_user (id, last_login, is_superuser, email, password, name, is_active, is_staff, created_at, updated_at) VALUES (1, '2024-04-10 04:50:26.747300', 1, 'tester1@kidsnote.com', 'pbkdf2_sha256$260000$h5AsoDiiY3epxzli9VScI9$MamP9nLWW0WfuBslPZCztvRNPRKhxjakCQrdAl7A7k8=', '테스터1', 1, 1, '2024-04-10 04:50:16.245964', '2024-04-10 04:50:16.245992');
INSERT INTO users_user (id, last_login, is_superuser, email, password, name, is_active, is_staff, created_at, updated_at) VALUES (2, null, 0, 'tester2@kidsnote.com', 'pbkdf2_sha256$260000$kjENpSIPX0ABp6ft6a8Nk2$Ur5Hh2Zjw2LTz5PMy0TtAhmfWaxjAXVd9rFdcs+NpQA=', '테스터2', 1, 0, '2024-04-10 04:53:17.818268', '2024-04-10 04:53:17.818289');

INSERT INTO contacts_contact (id, name, email, phone, company, position, memo, profile_image_url, address, birthday, website, created_at, updated_at, owner_id) VALUES (1, '김유경', 'u.gaemi@gmail.com', '01040707835', '키즈노트', '백엔드 개발자', 'Python / Django', null, '서울특별시 송파구', '1996-05-22', 'https://ugaemi.com', '2024-04-10 04:51:28.675662', '2024-04-10 05:02:55.035653', 1);
INSERT INTO contacts_contact (id, name, email, phone, company, position, memo, profile_image_url, address, birthday, website, created_at, updated_at, owner_id) VALUES (2, '홍길동', 'yorijori@kidsnote.com', '01012341234', '키즈노트', '프론트 개발자', 'React.js', null, null, null, null, '2024-04-10 04:52:43.674074', '2024-04-10 04:52:43.674112', 1);
INSERT INTO contacts_contact (id, name, email, phone, company, position, memo, profile_image_url, address, birthday, website, created_at, updated_at, owner_id) VALUES (3, '김철수', 'soo@naver.com', '01012345555', null, null, '', null, null, null, null, '2024-04-10 05:02:34.647112', '2024-04-10 05:02:34.647169', 1);

INSERT INTO contacts_contact_labels (id, contact_id, contactlabel_id) VALUES (1, 1, 1);
INSERT INTO contacts_contact_labels (id, contact_id, contactlabel_id) VALUES (2, 3, 3);
INSERT INTO contacts_contact_labels (id, contact_id, contactlabel_id) VALUES (3, 1, 2);

INSERT INTO contacts_contactlabel (id, name, created_at, updated_at, owner_id) VALUES (1, '회사', '2024-04-10 04:53:36.476614', '2024-04-10 04:53:36.476660', 1);
INSERT INTO contacts_contactlabel (id, name, created_at, updated_at, owner_id) VALUES (2, '지인', '2024-04-10 04:53:46.902631', '2024-04-10 04:53:46.902670', 1);
INSERT INTO contacts_contactlabel (id, name, created_at, updated_at, owner_id) VALUES (3, '친구', '2024-04-10 04:53:53.689349', '2024-04-10 04:53:53.689391', 1);
