{
    "chrome": {
    "default": "128.0",
    "versions": {
        "128.0": {
            "image": "selenoid/chrome:128.0",
            "port": "4444",
            "path": "/"
            }
        }
    },
    "firefox": {
    "default": "125.0",
    "versions": {
        "125.0": {
            "image": "selenoid/firefox:125.0",
            "port": "4444",
            "path": "/wd/hub",
            "env": ["MOZ_DISABLE_CONTENT_SANDBOX=1"],
            "args": ["--disable-content-signature-verification"]
            }
        }
    },
    "edge": {
        "default": "122.0",
        "versions": {
            "122.0": {
                "image": "selenoid/microsoft-edge:122.0",
                "port": "4444",
                "path": "/"
            }
        }
    }
}