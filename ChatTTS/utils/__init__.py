def __getattr__(name):
    if name in {"check_all_assets", "download_all_assets"}:
        from .dl import check_all_assets, download_all_assets

        return locals()[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


from .gpu import select_device
from .io import FileLike, del_all, get_latest_modified_file, load_safetensors
from .log import logger
