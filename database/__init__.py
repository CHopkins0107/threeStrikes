"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.2.0
"""

import aiosqlite


class DatabaseManager:
    def __init__(self, *, connection: aiosqlite.Connection) -> None:
        self.connection = connection
        
    # Check if user exists, returns user if true
    async def check_user(
        self, user_id: int, server_id: int, create_if_none=False
    ) -> dict:
        """
        This function will check if a user exists in the database.

        :param user_id: The ID of the user.
        :param server_id: The ID of the server.
        :return: The user if they exist, None otherwise.
        """
        async with self.connection.execute(
            "SELECT 1 FROM tribunal WHERE user_id = ?",
            (user_id)
        ) as cursor:
            user_exists = await cursor.fetchone() is not None
            
            return bool(user_exists)
            
        