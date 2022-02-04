"""Top-level package for dappman."""
# dappman/__init__.py

__app_name__ = "dappman"
__version__ = "0.1.0"

(
    SUCCESS,
    ALGOD_ERROR,
    ENV_ERROR,
    DIR_ERROR,
    CREATE_ERROR,
    UPDATE_ERROR,
    DELETE_ERROR,
    APP_ID_ERROR,
    JSON_ERROR,
) = range(9)

ERRORS = {
    ALGOD_ERROR: "algod error",
    ENV_ERROR: "environment variable error",
    DIR_ERROR: "directory error",
    CREATE_ERROR: "application create error",
    UPDATE_ERROR: "application update error",
    DELETE_ERROR: "application delete error",
    APP_ID_ERROR: "app id error",
}
