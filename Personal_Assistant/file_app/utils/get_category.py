IMAGE_EXT = (
    "jpg",
    "jpeg",
    "png",
    "gif",
    "bmp",
    "tiff",
    "tif",
    "webp",
    "svg",
    "jp2",
    "j2k",
    "psd",
    "ico",
    "heic",
    "heif",
    "cr2",
    "nef",
    "arw",
    "dng",
)

AUDIO_EXT = (
    "mp3",
    "wav",
    "flac",
    "aac",
    "ogg",
    "aiff",
    "wma",
    "m4a",
    "ape",
    "opus",
    "m4p",
    "mid",
    "midi",
    "amr",
    "wv",
    "ac3",
)

VIDEO_EXT = (
    "mp4",
    "avi",
    "mov",
    "wmv",
    "flv",
    "mkv",
    "webm",
    "mpeg",
    "mpg",
    "3gp",
    "ts",
    "m4v",
    "vob",
    "rm",
    "asf",
    "swf",
    "ogv",
    "divx",
    "xvid",
    "h264",
    "x264",
)

DOCUMENT_EXT = (
    "pdf",
    "doc",
    "docx",
    "xls",
    "xlsx",
    "ppt",
    "pptx",
    "txt",
    "csv",
    "rtf",
    "numbers",
    "odt",
    "ods",
    "odp",
    "html",
    "xml",
    "json",
    "epub",
    "psd",
    "ai",
    "indd",
    "pages",
)


def get_category(filename: str) -> str:
    """
    Get the category of a file based on its extension.

    Args:
        filename (str): The name of the file including its extension.

    Returns:
        str: The category of the file ('image', 'audio', 'video', 'document', or 'other').
    """
    ext = filename.rsplit(".")[-1]

    if ext in IMAGE_EXT:
        return "image"
    if ext in AUDIO_EXT:
        return "audio"
    if ext in VIDEO_EXT:
        return "video"
    if ext in DOCUMENT_EXT:
        return "document"
    return "other"


print(get_category("afasf.doc"))
