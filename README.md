# homeassistant-unraid

This is a custom component for [Home Assistant](http://home-assistant.io) that adds [UnRAID](http://unraid.net) data.

Tested on Unraid 6.8-RC9

## Config

In `/boot/config/plugins/dynamix/dynamix.cfg` contains a section labelled `[remote]`, here you should be able to find your `api_key`.

```ini
[remote]
apikey="c53a2R6c4A54043N4f4a65D4ba9fO103fbM491112Aa1519Padc7I2b735Ka768eE614d2Ydfbf7"
```

Copy this into your Home Assistant config along with the URL to your HA installation
```yaml
unraid:
    - host: http://192.168.0.10:8123/
      api_key: c53a2R6c4A54043N4f4a65D4ba9fO103fbM491112Aa1519Padc7I2b735Ka768eE614d2Ydfbf7
```
