import cloudinary
from cloudinary.utils import cloudinary_url
from django import template

register = template.Library()


def download_url(file_public_id: str) -> str:
    """
    Generate a download URL for a file in Cloudinary.

    Args:
        file_public_id (str): The public ID of the file in Cloudinary.

    Returns:
        str: The download URL for the file.
    """
    cloudinary.config(
        cloud_name="dpavzurzn",
        api_key="139162117698447",
        api_secret="rJG8kcY9XbZWGDRkjFl27o_45iY",
    )

    download_url, options = cloudinary_url(
        file_public_id,
        resource_type="raw",
        attachment=True,
        type="application/octet-stream",
    )

    return download_url


register.filter("download_url", download_url)
