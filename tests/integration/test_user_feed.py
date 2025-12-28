import pytest
from loguru import logger

from tiktokpy_2026.tiktokpy import TikTokPy
from tiktokpy_2026.tiktokpy.models.feed import FeedItem


@pytest.mark.asyncio()
async def test_user_feed(bot: TikTokPy):
    feed = await bot.user_feed(username="@tiktok_russia")
    logger.info(feed)

    assert len(feed) == 50
    assert isinstance(feed[0], FeedItem)
