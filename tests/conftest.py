import pytest

from tiktokpy_2026.tiktokpy import TikTokPy

@pytest.fixture()
async def bot() -> TikTokPy:
    async with TikTokPy() as bot:
        yield bot
