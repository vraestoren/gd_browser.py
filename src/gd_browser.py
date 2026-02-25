from requests import Session

class GdBrowser:
    def __init__(self) -> None:
        self.api = "https://gdbrowser.com/api"
        self.session = Session()
        self.session.headers = {
            "Server": "nginx/1.14.0 (Ubuntu)",
            "Content-type": "application/json; charset=utf-8",
            "Connection": "keep-alive"
        }

    def get_level(
            self, 
            level_id: int,
            download: bool = False) -> dict:
        return self.session.get(
             f"{self.api}/level/{level_id}?download" if download else f"{self.api}/level/{level_id}").json()

    def get_user_profile(self, username: str) -> dict:
        return self.session.get(f"{self.api}/profile/{username}").json()

    def search(
            self,
            query: str,
            count: int = 10,
            demon_filter: int = None,
            page: int = 0,
            gauntlet: int = None,
            type: str = "trending") -> dict:
        params = {
            "demonFilter": demon_filter,
            "page": page,
            "gauntlet": gauntlet,
            "type": type
        }
        filtered_params = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/search/{query}?count={count}", params=filtered_params).json()

    def get_leaderboard(
            self,
            count: int = 100, 
            is_creator: bool = False) -> dict:
        url = f"{self.api}/leaderboard?count={count}"
        if is_creator:
            url += "&creator"
        return self.session.get(url).json()

    def get_map_packs(self) -> dict:
        return self.session.get(f"{self.api}/mappacks").json()

    def get_gauntlets(self) -> dict:
        return self.session.get(f"{self.api}/gauntlets").json()

    def get_level_leaderboard(
            self,
            level_id: int,
            count: int = 100) -> dict:
        return self.session.get(
            f"{self.api}/leaderboardLevel/{level_id}?count={count}").json()

    def get_user_posts(
            self,
            user_id: int,
            page: int = 0,
            count: int = 10,
            type: str = "profile") -> dict:
        return self.session.get(
            f"{self.api}/comments/{user_id}?page={page}&count={count}&type={type}").json()

    def get_user_comments(
            self,
            user_id: int,
            page: int = 0,
            count: int = 10,
            type: str = "commentHistory") -> dict:
        return self.session.get(
            f"{self.api}/comments/{user_id}?page={page}&count={count}&type={type}").json()

    def get_level_comments(
            self,
            level_id: int,
            page: int = 0,
            is_top: bool = False,
            count: int = 10,
            type: str = "commentHistory") -> dict:
        url = f"{self.api}/comments/{level_id}?page={page}&count={count}&type={type}"
        if is_top:
            url += "&top"
        return self.session.get(url).json()

    def check_song_verification(self, song_id: int) -> dict:
        return self.session.get(f"{self.api}/song/{song_id}").text

    def analyze_level(self, level_id: int) -> dict:
        return self.session.get(f"{self.api}/analyze/{level_id}").json()

    def get_user_icon(
            self,
            username: str,
            form: str = "cube",
            size: str = "auto") -> dict:
        return self.session.get(
            f"{self.api}/icon/{username}?form={form}&size={size}").json()
