/*
 Navicat Premium Data Transfer

 Source Server         : cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : cis3368.c2sn9hhzxonj.us-east-1.rds.amazonaws.com:3306
 Source Schema         : CIS3368db

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 19/05/2022 17:25:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for destinations
-- ----------------------------
DROP TABLE IF EXISTS `destinations`;
CREATE TABLE `destinations`  (
  `destination_id` int NOT NULL AUTO_INCREMENT,
  `country` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `city` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sightseeing` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`destination_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 37 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of destinations
-- ----------------------------
INSERT INTO `destinations` VALUES (25, 'Brazil', 'Rio De Janiero', 'Christ the Redeemer Statue');
INSERT INTO `destinations` VALUES (30, 'Russia', 'Moscow', 'The Red Square');
INSERT INTO `destinations` VALUES (32, 'USA', 'Houston', 'Shopping Malls');

-- ----------------------------
-- Table structure for person
-- ----------------------------
DROP TABLE IF EXISTS `person`;
CREATE TABLE `person`  (
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `password` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of person
-- ----------------------------

-- ----------------------------
-- Table structure for persons
-- ----------------------------
DROP TABLE IF EXISTS `persons`;
CREATE TABLE `persons`  (
  `personID` int NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of persons
-- ----------------------------
INSERT INTO `persons` VALUES (NULL, 'admin', '1');
INSERT INTO `persons` VALUES (NULL, 'water', '123456');
INSERT INTO `persons` VALUES (NULL, 'fpizza', '123456');

-- ----------------------------
-- Table structure for trips
-- ----------------------------
DROP TABLE IF EXISTS `trips`;
CREATE TABLE `trips`  (
  `trip_id` int NOT NULL AUTO_INCREMENT,
  `transportation` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `tripname` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `destination_id` int NOT NULL,
  PRIMARY KEY (`trip_id`) USING BTREE,
  INDEX `FK_destination_id_idx`(`destination_id` ASC) USING BTREE,
  CONSTRAINT `FK_destination_id` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`destination_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of trips
-- ----------------------------
INSERT INTO `trips` VALUES (27, 'Car', '2022-04-22', '2022-04-28', 'Brazil Trip', 25);
INSERT INTO `trips` VALUES (29, 'Plane', '2022-04-20', '2022-04-22', 'Russia Trip', 30);

SET FOREIGN_KEY_CHECKS = 1;
