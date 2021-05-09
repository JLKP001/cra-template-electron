import os
import random
import argparse

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Header


app = FastAPI()
_environ = os.environ.copy()


async def check_secret(secret_token: str = Header(None)) -> None:
    """Dependency to check if a secret token is valid.
    This ensures only applications with the secret key specified when starting 
    the server or in environment variable is able to post to the server.
    If no secret token is specified while starting or in environment variables 
    this dependency does nothing.

    Args:
        secret_token (str, optional): Secret token sent with request. 
            Defaults to None.

    Raises:
        HTTPException: Secret Token invalid
    """
    if (_environ.get("SECRET_TOKEN") and
            secret_token != _environ.get("SECRET_TOKEN")):
        raise HTTPException(status_code=401, detail="Secret Token invalid")


@app.post("/roll", dependencies=[Depends(check_secret)])
async def roll_dice() -> int:
    """Generates and returns a random integer from 1 to 6.

    Returns:
        int: Random integer between 1 and 6 inclusive
    """
    return random.randint(1, 6)


def init_argparse() -> argparse.ArgumentParser:
    """Initialises argparse and returns an argument parser

    Returns:
        argparse.ArgumentParser: Object for parsing CLI arguments
    """
    parser = argparse.ArgumentParser(
        description="Launches the Python API",
    )
    parser.add_argument("--host", dest="host", default="127.0.0.1",
                        help="Bind socket to host. [default: %(default)s]")
    parser.add_argument("--port", dest="port", default=8000, type=int,
                        help="Bind socket to port. [default: %(default)s]")
    parser.add_argument("--log-level", dest="log_level", default="info",
                        choices=["critical", "error", "warning",
                                 "info", "debug", "trace"],
                        help="Log level. [default: %(default)s]")
    parser.add_argument("--secret", dest="secret", default=None,
                        help="Server secret token. [default: %(default)s]")
    return parser


if __name__ == "__main__":
    parser = init_argparse()
    args = parser.parse_args()

    if args.secret:
        _environ["SECRET_TOKEN"] = args.secret

    uvicorn.run(app, host=args.host, port=args.port,
                log_level=args.log_level)
