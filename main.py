import os

# Keep inference CPU usage predictable in constrained hosting environments.
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")

from libretranslate.app import create_app
from libretranslate.main import get_parser


def _get_app_args():
    parser = get_parser()
    # Ignore gunicorn CLI args when this module is imported as `main:app`.
    args, _ = parser.parse_known_args()
    if args.url_prefix and not args.url_prefix.startswith('/'):
        args.url_prefix = '/' + args.url_prefix
    return args


app = create_app(_get_app_args())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
