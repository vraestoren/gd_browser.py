# <img src="https://gdbrowser.com./assets/coin.png" width="28" style="vertical-align:middle;" /> gd_browser.py

> Web-API for [GDBrowser](https://gdbrowser.com) browse Geometry Dash levels, users, leaderboards, comments, and more.

## Quick Start
```python
from gd_browser import GdBrowser

gd = GdBrowser()

# Get a user profile
user = gd.get_user_profile(username="RobTop")
print(user)
```

---

## Levels

| Method | Description |
|--------|-------------|
| `get_level(level_id, download)` | Get level info, optionally with download data |
| `search(query, count, demon_filter, page, gauntlet, search_type)` | Search for levels |
| `analyze_level(level_id)` | Get detailed analysis of a level |
| `get_map_packs()` | Get all map packs |
| `get_gauntlets()` | Get all gauntlets |

**Search types:** `trending`, `featured`, `magic`, `awarded`, `recent`, `mostDownloaded`, `mostLiked`, `top`
```python
# Search for levels
gd.search("bloodbath", count=5, search_type="top")

# Get level with download data
gd.get_level(level_id=10565053, download=True)
```

---

## Users

| Method | Description |
|--------|-------------|
| `get_user_profile(username)` | Get a user's public profile |
| `get_user_posts(user_id, page, count)` | Get a user's profile posts |
| `get_user_comments(user_id, page, count)` | Get a user's comment history |
| `get_user_icon(username, form, size)` | Get a user's icon image |

**Icon forms:** `cube`, `ship`, `ball`, `ufo`, `wave`, `robot`, `spider`
```python
# Get profile
gd.get_user_profile("Serponge")

# Get user icon
gd.get_user_icon("RobTop", form="cube", size="auto")
```

---

## Leaderboards

| Method | Description |
|--------|-------------|
| `get_leaderboard(count, is_creator)` | Get top players or creators |
| `get_level_leaderboard(level_id, count)` | Get top scores for a level |
```python
# Top 100 players
gd.get_leaderboard(count=100)

# Top creators
gd.get_leaderboard(is_creator=True)
```

---

## Comments

| Method | Description |
|--------|-------------|
| `get_level_comments(level_id, page, is_top, count)` | Get comments on a level |
```python
# Top comments on a level
gd.get_level_comments(level_id=10565053, is_top=True)
```

---

## Songs

| Method | Description |
|--------|-------------|
| `check_song_verification(song_id)` | Check if a song is allowed for use |
