#  Pyrogram1 - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram1.
#
#  Pyrogram1 is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram1 is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram1.  If not, see <http://www.gnu.org/licenses/>.

from typing import Union

from pyrogram1 import raw
from pyrogram1.scaffold import Scaffold


class GetChatMembersCount(Scaffold):
    async def get_chat_members_count(
        self,
        chat_id: Union[int, str]
    ) -> int:
        """Get the number of members in a chat.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            ``int``: On success, the chat members count is returned.

        Raises:
            ValueError: In case a chat id belongs to user.

        Example:
            .. code-block:: python

                count = app.get_chat_members_count(chat_id)
                print(count)
        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerChat):
            r = await self.send(
                raw.functions.messages.GetChats(
                    id=[peer.chat_id]
                )
            )

            return r.chats[0].participants_count
        elif isinstance(peer, raw.types.InputPeerChannel):
            r = await self.send(
                raw.functions.channels.GetFullChannel(
                    channel=peer
                )
            )

            return r.full_chat.participants_count
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user')
