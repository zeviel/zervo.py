import requests


class ZervoClient:
    def __init__(self, language: str = "en"):
        self.api = "https://wg6.pinpon.cool"
        self.token = None
        self.user_id = None
        self.language = language
        self.headers = {
            "User-Agent": "Dart/2.16 (dart:io)",
            "language": self.language
        }

    def register(
            self,
            google_id: str,
            role_id: int,
            nickname: str,
            birthday: str = "2003-04-07 20:00:00.000Z"):
        data = {
            "appRoleId": f"{role_id}",
            "nickname": nickname,
            "birthday": birthday,
            "source": "google",
            "uid": google_id
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/v2/app-user/register",
            data=data,
            headers=self.headers)

    def google_auth(self, google_id: str):
        data = {
            "source": "google",
            "id": google_id
        }
        response = requests.post(
            f"{self.api}/pinpon-app-auth/auth/login/source",
            data=data,
            headers=self.headers).json()
        self.token = response["data"]["pinponToken"]["token"]
        self.user_id = response["data"]["appUserId"]
        self.headers["pinpon-auth"] = self.token
        return response

    def send_comment(self, post_id: int, comment: str, images: list = []):
        data = {
            "contentId": post_id,
            "comment": comment,
            "images": images
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/app-comment/save",
            data=data,
            headers=self.headers).json()

    # like status: 1 - to like, 0 - to unlike
    def like_post(self, post_id: int, like_status: int = 1):
        data = {
            "typeId": post_id,
            "type": 1,
            "likeStatus": like_status
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/app-like/like/status",
            data=data,
            headers=self.headers).json()

    def send_friend_request(self, nickname: str, user_id: int):
        data = {
            "isNickname": True,
            "nickname": nickname,
            "receiveUserId": user_id,
            "source": 1
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/app-friend-req/save",
            data=data,
            headers=self.headers).json()

    def block_user(self, user_id: int, is_friend: bool = False):
        data = {
            "friendUserId": user_id,
            "isFriend": is_friend
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/app-friend/block",
            data=data,
            headers=self.headers).json()

    def unblock_user(self, user_id: int):
        data = {"friendUserId": user_id}
        return requests.post(
            f"{self.api}/pinpon-app-system/app-friend/unblock",
            data=data,
            headers=self.headers).json()

    def get_album_info(self, album_id: int, limit: int = 10):
        return requests.get(
            f"{self.api}/pinpon-app-system/v2/app-meme/page?limit={limit}&albumId={album_id}",
            headers=self.headers).json()

    def get_post_comments(
            self,
            post_id: int,
            size: int = 10,
            current: int = 1):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-comment/list?contentId={post_id}&size={size}&current={current}&commentId",
            headers=self.headers).json()

    def get_app_roles(self):
        return requests.get(
            f"{self.api}/pinpon-app-auth/pinpon-app-system/v2/app-role/default",
            headers=self.headers).json()

    def get_friends_list(self):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-friend/list",
            headers=self.headers).json()

    def get_role_info(self, role_id: int):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-role/detail?roleId={role_id}",
            headers=self.headers).json()

    def get_recent_posts(self, size: int = 10, current: int = 1):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-content/query?size={size}&current={current}",
            headers=self.headers).json()

    def get_user_oc_list(self, user_id: int):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-oc/list?appUserId={user_id}",
            headers=self.headers).json()

    def get_user_info(self, user_id: int):
        return requests.get(
            f"{self.api}/pinpon-app-system/v2/app-user/detail?appUserId={user_id}",
            headers=self.headers).json()

    def get_user_stats(self, user_id: int):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-content/stats?appUserId={user_id}",
            headers=self.headers).json()

    def get_user_posts(self, user_id: int, size: int = 10):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-content/list?appUserId={user_id}&contentId&size={size}",
            headers=self.headers).json()

    def get_user_albums(self, user_id: int):
        return requests.get(
            f"{self.api}/pinpon-app-system/v2/app-album/list?appUserId={user_id}",
            headers=self.headers).json()

    def get_recommended_channels(
            self,
            current: int = 1,
            size: int = 10,
            name: str = None):
        return requests.get(
            f"{self.api}/pinpon-app-system/v2/app-channel/recommend/tag?current={current}&size={size}&name={name}",
            headers=self.headers).json()

    def join_channel(self, channel_id: int):
        data = {channel_id}
        return requests.post(
            f"{self.api}/pinpon-app-system/v2/app-channel-user/save",
            data=data,
            headers=self.headers).json()

    def leave_channel(self, channel_id: int):
        data = {"channelId": channel_id}
        return requests.post(
            f"{self.api}/pinpon-app-system/v2/app-channel-user/remove",
            data=data,
            headers=self.headers).json()

    def invite_to_channel(self, channel_id: int, user_id: int):
        data = {
            "guildId": "1111111111111111111",
            "appUserIds": [
                user_id
            ],
            "channelId": channel_id
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/app-channel-user/invite",
            data=data,
            headers=self.headers).json()

    def get_channel_info(self, channel_id: int):
        return requests.get(
            f"{self.api}/pinpon-app-system/v2/app-channel/detail?channelId={channel_id}",
            headers=self.headers).json()

    def get_channel_users(
            self,
            channel_id: int,
            current: int = 1,
            size: int = 10):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-channel-user/{channel_id}?current={current}&size={size}",
            headers=self.headers).json()

    def get_channel_moderators(self, channel_id: int):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-channel-user/moderator?channelId={channel_id}",
            headers=self.headers).json()

    def get_current_session(self):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-user/current-detail",
            headers=self.headers).json()

    def get_recommended_users(
            self,
            current: int = 1,
            size: int = 10,
            name: str = None):
        return requests.get(
            f"{self.api}/pinpon-app-system/v4/app-recommend?size={size}&current={current}&name={name}",
            headers=self.headers).json()

    def get_recommended_albums(
            self,
            current: int = 1,
            size: int = 10,
            name: str = None):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-album/recommend?current={current}&size={size}&name={name}",
            headers=self.headers).json()

    def get_recommended_all(
            self,
            current: int = 1,
            size: int = 10,
            name: str = None):
        return requests.get(
            f"{self.api}/pinpon-app-system/v4/app-recommend/all?current={current}&size={size}&name={name}",
            headers=self.headers).json()

    def get_app_tags(self):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-tag/list",
            headers=self.headers).json()

    def get_channel_blacklist(
            self,
            channel_id: int,
            current: int = 1,
            size: int = 10):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-group-black/list?current={current}&size={size}&groupId={channel_id}",
            headers=self.headers).json()

    def create_channel(
            self,
            title: str,
            avatar: str = "",
            max_age: int = 1000,
            min_age: int = 0,
            tag_list: list = []):
        data = {
            "avatar": avatar,
            "maxAge": max_age,
            "minAge": min_age,
            "name": title,
            "tagList": tag_list
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/v3/app-channel/chat/save",
            data=data,
            headers=self.headers).json()

    def edit_channel(
            self,
            channel_id: int,
            title: str = None,
            description: str = None,
            language: str = None):
        data = {"channelId": channel_id}
        if title:
            data["name"] = title
        elif description:
            data["bio"] = description
        elif language:
            data["language"] = language
        return requests.post(
            f"{self.api}/pinpon-app-system/v2/app-channel/update",
            data=data,
            headers=self.headers).json()

    def delete_channel(self, channel_id: int):
        data = {"channelId": channel_id}
        return requests.post(
            f"{self.api}/pinpon-app-system/v2/app-channel/remove",
            data=data,
            headers=self.headers).json()

    # types: 0 - violation, 1 - tease, 2 - spam, 3 - fraud
    def report_user(
            self,
            user_id: int,
            description: str,
            type: int = 0,
            url: str = None):
        data = {
            "reportedUserId": user_id,
            "description": description,
            "type": type,
            "url": url
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/app-report/save",
            data=data,
            headers=self.headers).json()

    def get_friend_requests(self):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-friend-req/list",
            headers=self.headers).json()

    def edit_profile(
            self,
            nickname: str = None,
            description: str = None,
            language: str = None,
            role_id: int = None,
            gender: int = 1):
        data = {}
        if nickname:
            data["nickname"] = nickname
        elif description:
            data["bio"] = description
        elif language:
            data["language"] = language
        elif gender:
            data["sex"] = gender
        elif role_id:
            data["appRoleId"] = role_id
        return requests.post(
            f"{self.api}/pinpon-app-system/app-user/update",
            data=data,
            headers=self.headers).json()

    def edit_profile_id(self, id: str):
        return requests.post(
            f"{self.api}/pinpon-app-system/app-user/update/userId?userId={id}",
            headers=self.headers).json()

    def get_owned_app_roles(self):
        return requests.get(
            f"{self.api}/pinpon-app-system/v2/app-role/owned-list-all",
            headers=self.headers).json()

    def create_post(self, theme_id: int, content: str, images: list = []):
        data = {
            "channelId": theme_id,
            "content": content,
            "images": images
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/app-content/save",
            data=data,
            headers=self.headers).json()

    def delete_post(self, post_id: int):
        return requests.post(
            f"{self.api}/pinpon-app-system/app-content/remove?contentId={post_id}",
            headers=self.headers).json()

    def create_oc(
            self,
            name: str,
            description: str,
            can_copy: int = 0,
            image_url: str = None,
            audio_url: str = None,
            emotion: str = "",
            sort: int = 0):
        data = {
            "appOC": {
                "name": name,
                "bio": description,
                "isCopy": can_copy
            },
            "addAppOcStatues": [
                {
                    "audioUrl": audio_url,
                    "emotion": emotion,
                    "sort": sort,
                    "url": image_url
                }
            ]
        }
        return requests.post(
            f"{self.api}/pinpon-app-system/app-oc/save",
            data=data,
            headers=self.headers).json()

    def delete_oc(self, oc_id: int):
        data = {"ids": oc_id}
        return requests.post(
            f"{self.api}/pinpon-app-system/app-oc/remove",
            data=data,
            headers=self.headers).json()

    def get_joined_channels(self):
        return requests.get(
            f"{self.api}/pinpon-app-system/v3/app-channel/chat/list",
            headers=self.headers).json()

    def get_game_maps(self, current: int = 1, page: int = 10):
        return requests.get(
            f"{self.api}/pinpon-app-system/game-map/list?current={current}&page={page}",
            headers=self.headers).json()

    def get_points(self):
        return requests.get(
            f"{self.api}/pinpon-app-system/app-user/point",
            headers=self.headers).json

    def spin_gachapon(self):
        return requests.post(
            f"{self.api}/pinpon-app-system/app-library/draw",
            headers=self.headers).json()
