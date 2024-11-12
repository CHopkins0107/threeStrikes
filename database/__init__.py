"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.2.0
"""

import aiosqlite
import datetime


class DatabaseManager:
    def __init__(self, *, connection: aiosqlite.Connection) -> None:
        self.connection = connection
        
    # Check if user exists, returns user if true
    async def check_user(
        self, user_id: int, server_id: int, create_if_none=False
    ) -> dict | None:
        """
        This function will check if a user exists in the database.

        :param user_id: The ID of the user.
        :param server_id: The ID of the server.
        :param create_if_none: If True, create a new user entry if it doesn't exist.
        :return: The user if they exist, None otherwise.
        """
        async with self.connection.execute(
            "SELECT * FROM tribunal WHERE user_id = ? AND server_id = ?",
            (str(user_id), str(server_id))
        ) as cursor:
            result = await cursor.fetchone()
            
            if result:
                # Convert the result to a dictionary
                print("user found")
                columns = [column[0] for column in cursor.description]
                return dict(zip(columns, result))
            elif create_if_none:
                # Create a new user entry if it doesn't exist
                await self.connection.execute(
                    """
                    INSERT INTO tribunal (user_id, server_id, likes_received, likes_given, 
                    dislikes_received, dislikes_given, punishments_received)
                    VALUES (?, ?, 0, 0, 0, 0, 0)
                    """,
                    (str(user_id), str(server_id))
                )
                await self.connection.commit()
                print("user not found, creating")
                return await self.check_user(user_id, server_id)
            else:
                print("user not found")
                return None
    
    async def add_user(
        self, user_id: int, server_id: int
    ) -> bool:
        """
        This function will add a user to the database.

        :param user_id: The ID of the user.
        :param server_id: The ID of the server.
        :return: True if the user was added, False otherwise.
        """
        user_data = await self.check_user(user_id, server_id)
        if user_data:
            print("user already exists")
            return False
        else:
            await self.connection.execute(
                """
                INSERT INTO tribunal (user_id, server_id, likes_received, likes_given,
                dislikes_received, dislikes_given, punishments_received)
                VALUES (?, ?, 0, 0, 0, 0, 0)
                """,
                (str(user_id), str(server_id))
            )
            await self.connection.commit()
            print("user added")
            return True
    
    async def update_dislikes(
        self, user_id: int, server_id: int, value: int
    ):
        async with self.connection.execute(
            """UPDATE tribunal 
            SET dislikes_received = dislikes_received + ?
            WHERE user_id = ? AND server_id = ?""",
            (value, str(user_id), str(server_id))
        ) as cursor:
            await self.connection.commit()
            if cursor.rowcount > 0:
                print ("Dislikes Successfully Updated")
                return True
            else:
                print ("Dislikes Failed to Update, adding user")
                await self.add_user(user_id, server_id)
                return await self.update_dislikes(user_id, server_id, value)
            
    async def get_dislikes_received(
        self, user_id: int, server_id: int
    ) -> int:
    
        user_data = await self.check_user(user_id, server_id)
        if user_data:
            return user_data["dislikes_received"]
        return -1
            
    async def update_dislikes_given(
        self, user_id: int, server_id: int, value: int
    ):
        async with self.connection.execute(
            """UPDATE tribunal
            SET dislikes_given = dislikes_given + ?
            WHERE user_id = ? AND server_id = ?""",
            (value, str(user_id), str(server_id))
        ) as cursor:
            await self.connection.commit()
            if cursor.rowcount > 0:
                print ("Dislikes Given Successfully Updated")
                return True
            else:
                print ("Dislikes Given Failed to Update, adding user")
                await self.add_user(user_id, server_id)
                return await self.update_dislikes_given(user_id, server_id, value)
    
    async def get_dislikes_given(
        self, user_id: int, server_id: int
    ) -> int:

        user_data = await self.check_user(user_id, server_id)
        if user_data:
            return user_data["dislikes_given"]
        return -1
    
    async def update_likes(
        self, user_id: int, server_id: int, value: int
    ):
        async with self.connection.execute(
            """UPDATE tribunal 
            SET likes_received = likes_received + ?
            WHERE user_id = ? AND server_id = ?""",
            (value, str(user_id), str(server_id))
        ) as cursor:
            await self.connection.commit()
            if cursor.rowcount > 0:
                print ("Likes Successfully Updated")
                return True
            else:
                print ("Likes Failed to Update, adding user")
                await self.add_user(user_id, server_id)
                return await self.update_likes(user_id, server_id, value)
            
    async def get_likes_received(
        self, user_id: int, server_id: int
    ) -> int:

        user_data = await self.check_user(user_id, server_id)
        if user_data:
            return user_data["likes_received"]
        return -1
    
    async def update_likes_given(
        self, user_id: int, server_id: int, value: int
    ):
        async with self.connection.execute(
            """UPDATE tribunal
            SET likes_given = likes_given + ?
            WHERE user_id = ? AND server_id = ?""",
            (value, str(user_id), str(server_id))
        ) as cursor:
            await self.connection.commit()
            if cursor.rowcount > 0:
                print ("Likes Given Successfully Updated")
                return True
            else:
                print ("Likes Given Failed to Update, adding user")
                await self.add_user(user_id, server_id)
                return await self.update_likes_given(user_id, server_id, value)
    
    async def get_likes_given(
        self, user_id: int, server_id: int
    ) -> int:

        user_data = await self.check_user(user_id, server_id)
        if user_data:
            return user_data["likes_given"]
        return -1
    
    async def update_punishments(
        self, user_id: int, server_id: int, value: int, message: str, dislikes: int
    ):
        # Update Tribunal Table
        async with self.connection.execute(
            """UPDATE tribunal
            SET punishments_received = punishments_received + ?
            WHERE user_id = ? AND server_id = ?""",
            (value, str(user_id), str(server_id))
        ) as cursor:
            await self.connection.commit()
            if cursor.rowcount > 0:
                print ("Punishments Successfully Updated")
            else:
                print("Punishments Failed to Update in tribunal table, adding user")
                await self.add_user(user_id, server_id)
                return await self.update_punishments(user_id, server_id, value, message, dislikes)
            
        # Update or insert into the messages table
        current_date = datetime.datetime.now().isoformat()
        async with self.connection.execute(
            """INSERT INTO messages (user_id, server_id, message, dislikes, date)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(user_id, server_id) DO UPDATE SET
            message = ?, dislikes = ?, date = ?""",
            (str(user_id), str(server_id), message, dislikes, current_date,
            message, dislikes, current_date)
        ) as cursor:
            await self.connection.commit()
            if cursor.rowcount > 0:
                print("Message Successfully Updated/Inserted in messages table")
            else:
                print("Message Failed to Update/Insert in messages table")
                return False

        return True
            
    async def get_punishments_received(
        self, user_id: int, server_id: int
    ) -> int:

        user_data = await self.check_user(user_id, server_id)
        if user_data:
            return user_data["punishments_received"]
        return -1
            
    
    
    
    
    
    
    
    
    
    
    
    