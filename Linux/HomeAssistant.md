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

## ESP32 Light AirSensor BME680

```yaml
esphome:
  name: esp32-wroom-44
  friendly_name: ESP32_WROOM_44

esp32:
  board: esp32dev
  framework:
    type: arduino

# Enable logging
logger:

# Enable Home Assistant API
api:
  encryption:
    key: "rlKJuHEiYC1o+5nbZxaH+TvpGJ/8J/URRNtnecqeot4="

ota:
  - platform: esphome
    password: "4992d333d63c746092f3134dfcb5b0bb"

wifi:
  networks:
    - ssid: !secret main_wifi_ssid
      password: !secret main_wifi_password

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Esp32-Wroom-44 Fallback Hotspot"
    password: "xlpxQS78BIix"

captive_portal:

web_server:

i2c:
  sda: 21
  scl: 22
  scan: true
  frequency: 800kHz

sensor:
  - platform: bme680
    temperature:
      name: "BME680 Temperature"
    pressure:
      name: "BME680 Pressure"
    humidity:
      name: "BME680 Humidity"
    gas_resistance:
      name: "BME680 Gas Resistance"
    address: 0x77
    update_interval: 60s

# Nastavimo GPIO21 za napajanje senzorja
#switch:
#  - platform: gpio
#    pin: GPIO02
#    id: "SensorPowerVCC"
#    name: "BME680 Power VCC"
#  - platform: gpio
#    pin: GPIO0
#    id: "SensorPowerGND"
#    name: "BME680 Power GND"

# Vključitev zunanje komponente z GitHuba
external_components:
  # shorthand
  source: github://aronsky/esphome-components

ble_adv_controller:
  - id: my_controller
    encoding: lampsmart_pro

light:
  - platform: ble_adv_controller
    ble_adv_controller_id: my_controller
    name: Living Room Light

button:
  - platform: ble_adv_controller
    ble_adv_controller_id: my_controller
    name: Pair
    cmd: pair
```

### Wireless uploading

ESP module lahko sprogramirmo tudi preko WiFija. Opazil sem, da se povezava
ne vzpostavi vedno... mislim pa, da je težav manj, če pred programiranjem 
dostopimo na server tega modula in šele nato sprogramiramo:

    1. ESPHome -> Module -> Visit ...
    2.              └> Edit -> Install

## SSH & TERMINAL

Za povezavo SSH in uporabo terminala na HA-ju je dobro uporabljati:
[Advanced SSH & Web Terminal18.0.0](http://homeassistant.local:8123/hassio/addon/a0d7b954_ssh/info)

Ne pozabi nastaviti uporabniškega imena in gesla v [konfuguracijski datoteki](http://homeassistant.local:8123/hassio/addon/a0d7b954_ssh/config) in shraniti nastavitve ter nenazadnje tudi ponovno zagnati terminal.

Za namestitev aplikacij lahko uprabljamo upaz kot na primer:

    apk add ranger

## Remote access

- [Glej na tej strani](https://www.youtube.com/watch?v=AK5E2T5tWyM)
