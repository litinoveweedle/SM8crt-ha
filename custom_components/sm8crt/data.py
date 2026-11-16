FULL_NAME = "HALL Current Sensor DAQ"
LINK = "https://sequentmicrosystems.com/products/hall-current-sensor-daq-stackable-hat-for-raspberry-pi"


import SM8crt
API = SM8crt.SM8crt
DOMAIN = "sm8crt"
NAME_PREFIX = "sm8crt"

SM_MAP = {
    "datetime": {
        "rtc": {
                "chan_no": 1,
                "com": {
                    "get": "get_rtc",
                    "set": "set_rtc",
                },
        },
    },
    "sensor":  {
        "crt": {
                "chan_no": 8,
                "uom": "A",
                "com": {
                    "get": "get_crt",
                },
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                },
        },
        "crt_rms": {
                "chan_no": 8,
                "uom": "A",
                "com": {
                    "get": "get_crt_rms",
                },
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                },
        },
    },
    "switch": {
        "led": {
                "chan_no": 8,
                "com": {
                    "get": "get_led",
                    "set": "set_led"
                },
                "icon": {
                    "on": "mdi:led-on",
                    "off": "mdi:led-off"
                }
        },
        "crt_sensor_type": {
                "chan_no": 8,
                "com": {
                    "get": "get_crt_sensor_type",
                    "set": "set_crt_sensor_type"
                },
                # "icon": {
                #     "on": "mdi:led-on",
                #     "off": "mdi:led-off"
                # }
        },
    },
    "number": {
        "crt_range": {
                "chan_no": 8,
                "uom": "A",
                "min_value": 1.0,
                "max_value": 300.0,
                "step": 1.0,
                "com": {
                    "get": "get_crt_range",
                    "set": "set_crt_range"
                },
                # TODO: Improve this icons
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                }
        },
    }
}
