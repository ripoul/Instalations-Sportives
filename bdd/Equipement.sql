-- phpMyAdmin SQL Dump
-- version 4.3.11.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 11, 2016 at 12:22 PM
-- Server version: 5.5.50-0+deb7u2
-- PHP Version: 5.4.45-1~dotdeb+7.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


--
-- Table structure for table `Equipement`
--

CREATE TABLE IF NOT EXISTS `equipement` (
  `id` int(20) CHARACTER SET utf8 NOT NULL,
  `nom` varchar(200) CHARACTER SET utf8 NOT NULL,
  `activite` int(20) CHARACTER SET utf8 NOT NULL,
  `installation` int(20) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `equipement`
--

--INSERT INTO `joueurs` (`pseudo`, `motDePasse`) VALUES
--('titi', '$6$VsDCW/kqInRv$/bkDT4rmkNLGo704srZE1riI4u7IUUcSuuEqrdkeBJ.3RcsnEO.ihAnWvIWJ0fSoP3hVa/OpWTbhi50xQhzEk1'),
--('toto', '$6$RTRffX4m9FBU$GQPzOIuRByEJMeT8r9fydj8eKfi7yurb0SQiT./3pHnG5ni2f96gboxLE4LZgCgEVMWMP6z.AxaOM8KaWJCmn0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `equipement`
--
ALTER TABLE `equipement`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `equipement`
ADD CONSTRAINT `equipement_act` FOREIGN KEY (`activite`) REFERENCES `activite` (`id`);

ALTER TABLE `equipement`
ADD CONSTRAINT `equipement_inst` FOREIGN KEY (`installation`) REFERENCES `installation` (`id`);


