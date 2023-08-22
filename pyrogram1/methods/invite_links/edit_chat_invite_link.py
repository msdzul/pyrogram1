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
from pyrogram1 import types
from pyrogram1.scaffold import Scaffold


class EditChatInviteLink(Scaffold):
    async def edit_chat_invite_link(
        self,
        chat_id: Union[int, str],
        invite_link: str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None
    ) -> "types.ChatInviteLink":
        """Edit a non-primary invite link.

        You must be an administrator in the chat for this to work and must have the appropriate admin rights.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            invite_link (``str``):
                The invite link to edit

            name (``str``, *optional*):
                Invite link name.

            expire_date (``int``, *optional*):
                Point in time (Unix timestamp) when the link will expire.
                Defaults to None (no change), pass 0 to set no expiration date.

            member_limit (``int``, *optional*):
                Maximum number of users that can be members of the chat simultaneously after joining the chat via this
                invite link; 1-99999.
                Defaults to None (no change), pass 0 to set no member limit.

            creates_join_request (``bool``, *optional*):
                True, if users joining the chat via the link need to be approved by chat administrators.
                If True, member_limit can't be specified.

        Returns:
            :obj:`~pyrogram1.types.ChatInviteLink`: On success, the new invite link is returned

        Example:
            .. code-block:: python

                # Edit the member limit of a link
                link = app.edit_chat_invite_link(chat_id, invite_link, member_limit=9)

                # Set no expiration date of a link
                link = app.edit_chat_invite_link(chat_id, invite_link, expire_date=0)
        """
        r = await self.send(
            raw.functions.messages.EditExportedChatInvite(
                peer=await self.resolve_peer(chat_id),
                link=invite_link,
                expire_date=expire_date,
                usage_limit=member_limit,
                title=name,
                request_needed=creates_join_request
            )
        )

        users = {i.id: i for i in r.users}

        return types.ChatInviteLink._parse(self, r.invite, users)
