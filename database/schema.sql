CREATE TABLE IF NOT EXISTS `tribunal` (
  `user_id` varchar(20) NOT NULL,
  `server_id` varchar(20) NOT NULL,
  `likes_received` int(9) NOT NULL,
  `likes_given` int(9) NOT NULL,
  `dislikes_received` int(9) NOT NULL,
  `dislikes_given` int(9) NOT NULL,
  `punishments_received` int(9) NOT NULL
  PRIMARY KEY (`user_id`)
);