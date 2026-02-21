import os

from libretranslate.app import create_app
from libretranslate.main import get_args

args = get_args()
app = create_app(args)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
