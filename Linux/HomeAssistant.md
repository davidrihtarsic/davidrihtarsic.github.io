HOMEASSISTANT
================================================================================

## HomeESP

HA ima zelo dobro podporo za ESP krmilnike. ESP32 ali ESP8266 lahko programirate
s HA-jem z nekaj kliki. Za komunikacijo z ESP krmilniki potrebujete:
[ESPHome](http://homeassistant.local:8123/hassio/addon/5c53de3b_esphome/info).

### Edit file

Primer edit datoteke za ESP8266 z OLED displayem:

```yaml
esphome:
  name: esp8266oled-2
  friendly_name: ESP8266OLED_2

esp8266:
  board: esp01_1m

# Enable logging
logger:

# Enable Home Assistant API
api:
  encryption:
    key: "j/BnvsdLlKd02Y/ObJ/U00Zx0f58IA+PszK3p4I+ruo="

ota:
  - platform: esphome
    password: "ecfd994d055a8c1f0a3424ee797cefa0"

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Esp8266Oled-2 Fallback Hotspot"
    password: "dOYlSLqqJjhD"

captive_portal:

web_server:
  
# Example configuration entry
sensor:
  - platform: aht10
    i2c_id: bus_a
    variant: AHT10
    temperature:
      name: "Jure's Room Temperature"
      id: ath10_temp
    humidity:
      name: "Jure's Room Humidity"
      id: ath10_hum
    update_interval: 60s

# Example configuration entry for ESP32
i2c:
  - id: bus_d
    sda: GPIO14
    scl: GPIO12
    scan: true
  - id: bus_a
    sda: GPIO03
    scl: GPIO01
    scan: true  

font:
  - file: "gfonts://Roboto"
    id: roboto
    size: 16

display:
  - platform: ssd1306_i2c
    i2c_id: bus_d
    model: "SSD1306 128x64"
    id: oled
    address: 0x3C
    #it.strftime(0, 0, id(roboto), "%H:%M:%S", id(esptime).now());
    lambda: |-
      it.printf(0, 0, id(roboto), "IP: %s", WiFi.localIP().toString().c_str());      
      it.printf(10, 20, id(roboto), "T = %.1f °C", id(ath10_temp).state);
      it.printf(10, 40, id(roboto), "H = %.1f %%", id(ath10_hum).state);
    update_interval: 10s

time:
  - platform: homeassistant
    on_time:
      # Every morning
      - cron: '0 0 8 * * *'
        then:
          - lambda: id(oled).turn_on();
      # Every night
      - cron: '0 0 21 * * *'
        then:
          - lambda: id(oled).turn_off();
```

## SSH & TERMINAL

Za povezavo SSH in uporabo terminala na HA-ju je dobro uporabljati:
[Advanced SSH & Web Terminal18.0.0](http://homeassistant.local:8123/hassio/addon/a0d7b954_ssh/info)

Ne pozabi nastaviti uporabniškega imena in gesla v [konfuguracijski datoteki](http://homeassistant.local:8123/hassio/addon/a0d7b954_ssh/config) in shraniti nastavitve ter nenazadnje tudi ponovno zagnati terminal.

Za namestitev aplikacij lahko uprabljamo upaz kot na primer:

    apk add ranger




