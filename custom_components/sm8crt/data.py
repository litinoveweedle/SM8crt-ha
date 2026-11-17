import SM8crt

FULL_NAME = "HALL Current Sensor DAQ"
LINK = "https://sequentmicrosystems.com/products/hall-current-sensor-daq-stackable-hat-for-raspberry-pi"
API = SM8crt.SM8crt
DOMAIN = "sm8crt"
NAME_PREFIX = "sm8crt"

SM_MAP = {
    "button": {
        "watchdog_reload": {
            "chan_no": 1,
            "optional": True,
            "com": {"set": "wdt_reload"},
        },
    },
    "datetime": {
        "rtc": {
            "chan_no": 1,
            "com": {
                "get": "get_rtc",
                "set": "set_rtc",
            },
        },
    },
    "sensor": {
        "watchdog_count": {
            "chan_no": 1,
            "optional": True,
            "com": {"get": "wdt_get_reset_count"},
        },
        "crt": {
            "chan_no": 8,
            "uom": "A",
            "com": {
                "get": "get_crt",
            },
            "icon": {"on": "mdi:flash-triangle", "off": "mdi:flash-triangle"},
        },
        "crt_rms": {
            "chan_no": 8,
            "uom": "A",
            "com": {
                "get": "get_crt_rms",
            },
            "icon": {"on": "mdi:flash-triangle", "off": "mdi:flash-triangle"},
        },
    },
    "switch": {
        "led": {
            "chan_no": 8,
            "com": {"get": "get_led", "set": "set_led"},
            "icon": {"on": "mdi:led-on", "off": "mdi:led-off"},
        },
        "crt_sensor_type": {
            "chan_no": 8,
            "com": {"get": "get_crt_sensor_type", "set": "set_crt_sensor_type"},
            # "icon": {
            #     "on": "mdi:led-on",
            #     "off": "mdi:led-off"
            # }
        },
    },
    "number": {
        "watchdog_period": {
            "chan_no": 1,
            "optional": True,
            "uom": "s",
            "min_value": 1,
            "max_value": 65535,
            "step": 1,
            "com": {"get": "wdt_get_period", "set": "wdt_set_period"},
        },
        "watchdog_initial": {
            "chan_no": 1,
            "optional": True,
            "uom": "s",
            "min_value": 1,
            "max_value": 65535,
            "step": 1,
            "com": {"get": "wdt_get_init_period", "set": "wdt_set_init_period"},
        },
        "crt_range": {
            "chan_no": 8,
            "uom": "A",
            "min_value": 1.0,
            "max_value": 300.0,
            "step": 1.0,
            "com": {"get": "get_crt_range", "set": "set_crt_range"},
            # TODO: Improve this icons
            "icon": {"on": "mdi:flash-triangle", "off": "mdi:flash-triangle"},
        },
    },
}
