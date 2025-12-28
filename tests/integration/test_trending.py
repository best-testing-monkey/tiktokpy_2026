import pytest
from loguru import logger

from tiktokpy_2026.tiktokpy import TikTokPy
from tiktokpy_2026.tiktokpy.models.feed import FeedItem


@pytest.mark.asyncio()
async def test_trending(bot: TikTokPy):
    trending = await bot.trending(amount=50)
    logger.info(trending)

    assert len(trending) == 50
    assert isinstance(trending[0], FeedItem)
