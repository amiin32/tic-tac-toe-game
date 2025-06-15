CREATE DATABASE LMS;

USE LMS;

CREAT TABLE authors(
  author_id INT IDENTITY VARCHAR(4) PRIMARY KEY NOT NULL,
  author_name VARCHAR(30) NOT NULL

);

CREATE TABLE books (
  book_id INT VARCHAR(4) NOT NULL,
  title VARCHAR(50) NOT NULL,
  FOREIAN KEY author_id VARCHAR(4) references authors(author_id),
  publish_date DATE

);

CREATE TABLE members (
  member_id CHAR(4) PRIMARY KEY,
  name CHAR(30),
  city CHAR(20)

);

CREATE TABLE borrow (
  FOREIAN KEY member_id CHAR(4) references members(member_id),
  FOREIAN KEY book_id CHAR(4) references books(book_id),
  borrow_date DATE,
  return_date DATE


);