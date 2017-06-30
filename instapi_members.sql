-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 30, 2017 at 03:47 PM
-- Server version: 5.7.18-log
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `instawork`
--

-- --------------------------------------------------------

--
-- Table structure for table `instapi_members`
--

CREATE TABLE `instapi_members` (
  `uid` int(11) NOT NULL,
  `firstname` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` int(11) NOT NULL,
  `role` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `instapi_members`
--

INSERT INTO `instapi_members` (`uid`, `firstname`, `lastname`, `email`, `phone`, `role`) VALUES
(4, 'ram', 'singh', 'ram@aa.aa', 1234567899, 2),
(5, 'hello', 'boy', 'hello@aa.aa', 1234567899, 2),
(6, 'yo', 'man', 'hello@aa.aa', 1234567899, 2),
(7, 'hahaha', 'man', 'hello@aa.aa', 1234567899, 2),
(8, 'lui', 'sui', 'hello@aa.aa', 1234567899, 2),
(9, 'sui', 'moi', 'hello@aa.aa', 1234567899, 2),
(10, 'lol', 'what', 'hello@aa.aa', 1234567899, 2),
(11, 'lol', 'what', 'hello@aa.aa', 1234567899, 2),
(12, 'lol', 'what', 'hello@aa.aa', 1234567899, 2),
(13, 'John', 'yeah', 'hello@aa.aa', 1234567899, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `instapi_members`
--
ALTER TABLE `instapi_members`
  ADD PRIMARY KEY (`uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `instapi_members`
--
ALTER TABLE `instapi_members`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
