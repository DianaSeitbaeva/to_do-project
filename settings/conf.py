# -----------------------------------------------
# Path
#
SECRET_KEY = 'vnz&^!36%n0tm^85w+21ssyd8ok2t3q_)tp-%!@*gsxf+so#2('
ADMIN_SITE_URL = 'custom_admin/'

# -----------------------------------------------
# DEBUG TOOLBAR PANELS SETTINGS
#
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# -----------------------------------------------
# SHELL_PLUS CONFIGURATIONS
#
SHELL_PLUS_PRE_IMPORTS = [
    ('django.db', ('connection', 'reset_queries', 'connections')),
    ('datetime', ('datetime', 'timedelta', 'date')),
    ('json', ('loads', 'dumps')),
]
SHELL_PLUS_MODEL_ALIASES = {
    'university': {
        'Student': 'S',
        'Account': 'A',
        'Group': 'G',
        'Professor': 'P',
        'StudentHomework': 'H',
        'File': 'FF'
    },
}
SHELL_PLUS = 'ipython'
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000
