# homeassistant-unraid

![GitHub](https://img.shields.io/github/license/jiminald/unraid)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

This is a custom component for [Home Assistant](http://home-assistant.io) that adds [UnRAID](http://unraid.net) data as a sensor to HA.

This component uses a GraphQL API component for a under development module [unraid.net](https://github.com/limetech/Unraid.net)

Tested on Unraid 6.8

## Setup

First, you will need to install the unraid.net plugin onto your unraid instance [https://github.com/limetech/Unraid.net/blob/next/Unraid.net.plg](https://github.com/limetech/Unraid.net/blob/next/Unraid.net.plg)

This will add a new section to your Settings > Management Access titled unraid.net. Register your instance using your unraid.net forum account.

Now SSH into your unraid installation and run the following command
`/etc/rc.d/rc.unraid-api start`

## Config

Once you've completed the setup, go to `/boot/config/plugins/dynamix/dynamix.cfg` contains a section labelled `[remote]`, here you should be able to find your `api_key`.

```ini
[remote]
apikey="c53a2R6c4A54043N4f4a65D4ba9fO103fbM491112Aa1519Padc7I2b735Ka768eE614d2Ydfbf7"
```

Go to your Home Assistance installation and setup a new integration. Find unraid in the list and enter the URL to your installation and the API Key found in the file above.

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)
