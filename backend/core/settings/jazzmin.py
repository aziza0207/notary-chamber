from decouple import config

FRONTEND_HOME = config('FRONTEND_HOME', default='')

JAZZMIN_SETTINGS = {
    "site_title": "Notary Chamber",

    "site_logo": 'admin/notary_2.png',

    "copyright": "Sanarip Galley",
    "topmenu_links": [

        {"name": "Главная",  "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Открыть сайт", "url": FRONTEND_HOME, "new_window": True},

        {"app": "notary", },

        {"app": "content", },
        
        {"app": "structure", },
        
        {"app": "ed_centres", },
    ],

    # Whether to display the side menu

    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "order_with_respect_to": [
        "notary.notary", "notary.recipient", "notary.EducationalCentre",
        "notary.roles", "notary.NotaryFlow", "notary.MinistryFlow",
        
        "content.contact", "content.faq", "content.document", "content.link",
        "content.aphorism", "content.news", "content.photoset", "content.video",
        
        "structure.GeneralAssembly", "structure.NotaryCouncil", "structure.Comission",
        
        "ed_centres.CenterInfo", "ed_centres.CenterTask", "ed_centres.ManagerProfile",
        "ed_centres.StudyPlan", "ed_centres.TeachingStaff", "ed_centres.EducationalMaterial",
        ],

    # "show_ui_builder": True
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}