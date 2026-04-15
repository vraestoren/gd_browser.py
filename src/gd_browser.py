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

    def _get(self, endpoint: str, params: dict = None) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}", params=params or {}).json()

    def _filter(self, data: dict) -> dict:
        return {key: value for key, value in data.items() if value is not None}

    def get_level(
            self,
            level_id: int,
            download: bool = False) -> dict:
        endpoint = f"/level/{level_id}"
        if download:
            endpoint += "?download"
        return self._get(endpoint)

    def get_user_profile(self, username: str) -> dict:
        return self._get(f"/profile/{username}")

    def search(
            self,
            query: str,
            count: int = 10,
            demon_filter: int = None,
            page: int = 0,
            gauntlet: int = None,
            search_type: str = "trending") -> dict:
        params = self._filter({
            "count": count,
            "demonFilter": demon_filter,
            "page": page,
            "gauntlet": gauntlet,
            "type": search_type
        })
        return self._get(f"/search/{query}", params)

    def get_leaderboard(
            self,
            count: int = 100,
            is_creator: bool = False) -> dict:
        params = {
            "count": count,
        }
        if is_creator:
            params["creator"] = ""
        return self._get("/leaderboard", params)

    def get_map_packs(self) -> dict:
        return self._get("/mappacks")

    def get_gauntlets(self) -> dict:
        return self._get("/gauntlets")

    def get_level_leaderboard(
            self,
            level_id: int,
            count: int = 100) -> dict:
        params = {"count": count}
        return self._get(f"/leaderboardLevel/{level_id}", params)

    def get_user_posts(
            self,
            user_id: int,
            page: int = 0,
            count: int = 10) -> dict:
        params = {
            "page": page,
            "count": count,
            "type": "profile"
        }
        return self._get(f"/comments/{user_id}", params)

    def get_user_comments(
            self,
            user_id: int,
            page: int = 0,
            count: int = 10) -> dict:
        params = {
            "page": page,
            "count": count,
            "type": "commentHistory"
        }
        return self._get(f"/comments/{user_id}", params)

    def get_level_comments(
            self,
            level_id: int,
            page: int = 0,
            is_top: bool = False,
            count: int = 10) -> dict:
        params = self._filter({
            "page": page,
            "count": count,
            "type": "level",
            "top": "" if is_top else None
        })
        return self._get(f"/comments/{level_id}", params)

    def check_song_verification(self, song_id: int) -> str:
        return self.session.get(f"/song/{song_id}")

    def analyze_level(self, level_id: int) -> dict:
        return self._get(f"/analyze/{level_id}")

    def get_user_icon(
            self,
            username: str,
            form: str = "cube",
            size: str = "auto") -> dict:
        params = {
            "form": form,
            "size": size
        }
        return self._get(f"/icon/{username}", params)
