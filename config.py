# REQUIRED CONFIG
BOT_TOKEN = "7683734636:AAESOJ4QApLRY6vBqKfwstbOjWd_2dtIXBk"
OWNER_ID = 7348205141
TELEGRAM_API = 23621595
TELEGRAM_HASH = "de904be2b4cd4efe2ea728ded17ca77d"

# SEMI-REQUIRED, WE SUGGEST TO FILL IT FROM MONGODB
DATABASE_URL = ""

# OPTIONAL CONFIG
TG_PROXY = {}
USER_SESSION_STRING = ""
DOWNLOAD_DIR = "/tmp"
CMD_SUFFIX = ""
AUTHORIZED_CHATS = "-1001551886347"
SUDO_USERS = "7348205141 1249672673"
DEFAULT_UPLOAD = "rc"
FILELION_API = ""
STREAMWISH_API = ""
EXCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SUBSTITUTE = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}

# INKYPINKY
DELETE_LINKS = True
AUTO_DELETE = True
FSUB_IDS = "-1001551886347"
TOKEN_TIMEOUT = 0
PAID_CHANNEL_ID = 0
PAID_CHANNEL_LINK = ""
SET_COMMANDS = True
METADATA_KEY = ""
WATERMARK_KEY = ""
LOG_CHAT_ID = -1002564797463
LEECH_FILENAME_CAPTION = ""
HYDRA_IP = ""
HYDRA_API_KEY = ""
INSTADL_API = ""

# GDrive Tools
GDRIVE_ID = "1k8jjHGYRWA6mn5nsodprhnHWkwxuSrzv"
IS_TEAM_DRIVE = True # Set True useing Shared Drive 
STOP_DUPLICATE = True # Recommended For Heavy Usage
INDEX_URL = ""

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""

# Mega credentials
MEGA_EMAIL = ""
MEGA_PASSWORD = ""

# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    },
]

# Update
UPSTREAM_REPO = ""
UPSTREAM_BRANCH = ""

# Leech
LEECH_SPLIT_SIZE = 2097152000 # 2gb in Bytes
AS_DOCUMENT = False
MEDIA_GROUP = False
USER_TRANSMISSION = False
HYBRID_LEECH = True
LEECH_FILENAME_PREFIX = ""
LEECH_DUMP_CHAT = "-1002512081518"
THUMBNAIL_LAYOUT = ""

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
BASE_URL_PORT = 80
WEB_PINCODE = False

# Queueing system
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0
AUTO_DELETE = os.environ.get("AUTO_DELETE", "False").lower() == "true"
