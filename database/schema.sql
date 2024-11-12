CREATE TABLE IF NOT EXISTS `tribunal` (
  `user_id` VARCHAR(20) NOT NULL,
  `server_id` VARCHAR(20) NOT NULL,
  `likes_received` INTEGER NOT NULL,
  `likes_given` INTEGER NOT NULL,
  `dislikes_received` INTEGER NOT NULL,
  `dislikes_given` INTEGER NOT NULL,
  `punishments_received` INTEGER NOT NULL,
  PRIMARY KEY (`user_id`, `server_id`)
);

CREATE TABLE IF NOT EXISTS `messages` (
  `user_id` VARCHAR(20) NOT NULL,
  `server_id` VARCHAR(20) NOT NULL,
  `message` TEXT NOT NULL,
  `dislikes` INTEGER NOT NULL,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`user_id`, `server_id`)
);