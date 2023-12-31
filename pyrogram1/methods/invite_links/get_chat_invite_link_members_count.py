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


class GetChatInviteLinkMembersCount(Scaffold):
    async def get_chat_invite_link_members_count(
        self,
        chat_id: Union[int, str],
        invite_link: str
    ) -> int:
        """Get the count of the members who joined the chat with the invite link.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            invite_link (str):
                The invite link.

        Returns:
            ``int``: On success, the joined chat members count is returned.
        """
        r = await self.send(
            raw.functions.messages.GetChatInviteImporters(
                peer=await self.resolve_peer(chat_id),
                link=invite_link,
                limit=1,
                offset_date=0,
                offset_user=raw.types.InputUserEmpty()
            )
        )

        return r.count
