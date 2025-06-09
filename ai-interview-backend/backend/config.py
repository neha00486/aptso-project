GEMINI_API_KEY=""
try:
    from config_s import GEMINI_API_KEY_S
    GEMINI_API_KEY = GEMINI_API_KEY_S
except ImportError:
    GEMINI_API_KEY = "AIzaSyAZeutNl9p_zhRIw96O2mdI-2VqKK0RhNM" #<-------------ADD YOU API KEY HERE

MODEL_ID = "gemini-2.0-flash-exp"