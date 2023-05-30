import logging
from openai import Image, error
from slugify import slugify

from app.db.errors import EntityDoesNotExist
from app.db.repositories.items import ItemsRepository
from app.models.domain.items import Item
from app.models.domain.users import User


async def check_item_exists(items_repo: ItemsRepository, slug: str) -> bool:
    try:
        await items_repo.get_item_by_slug(slug=slug)
    except EntityDoesNotExist:
        return False

    return True

def get_item_image_if_not_exists(title: str, image_url: str) -> str:
    if image_url != "":
        return image_url

    try:
        response = Image.create(prompt=title, n=1, size="256x256")
        return response['data'][0]['url']
    except error.OpenAIError as e:
        logging.error("Could not generate openai image. Leaving item image empty.")
        logging.error(e.http_status, e.error)


def get_slug_for_item(title: str) -> str:
    return slugify(title)


def check_user_can_modify_item(item: Item, user: User) -> bool:
    return item.seller.username == user.username
