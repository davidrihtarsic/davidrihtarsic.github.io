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
### PWR Metere

V ESPHome sta dve funkciji, ki lahko merita pogostost pulzov:
- pulse_meter in
- pulse_counter

Pulse_meter je imel v zadnjem času nekaj težav in je občasno pokazal neverjetno napačne podatkje,
zato je bolje, da v tem primeru uporabljamo kodo prejšnje različice te funkcije:

```yaml
external_components:
  - source: github://esphome/esphome@2023.5.4
    components: [pulse_meter]
```

#### Pulse_counter

```yaml
esphome:
  name: pwr-test
  friendly_name: PWR_Test

esp32:
  board: esp32dev
  framework:
    type: arduino

# Enable logging
logger:

# Enable Home Assistant API
api:
  encryption:
    key: "otLKBa9eccowzkE61Azb9n0f5Gq5Qy5RKK7kL7saFD4="

ota:
  - platform: esphome
    password: "084c352dd35c55482d1ca94c9d906749"

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Pwr-Test Fallback Hotspot"
    password: "L2jzkNFtkCGd"

captive_portal:

web_server:

# Example configuration entry
sensor:
  - platform: pulse_counter
    icon: mdi:flash-outline
    pin: GPIO26
    state_class: measurement
    device_class: power
    unit_of_measurement: 'W'
    name: 'Power Meter House'
    accuracy_decimals: 0
    filters:
      - multiply: 60  # (60s/1000 pulses per kWh)

    total:
      unit_of_measurement: 'kWh'
      name: 'Energy Meter House'
      accuracy_decimals: 3
      filters:
        - multiply: 0.001  # (1/1000 pulses per kWh)
```

### Glow Pulse meter

```yaml
substitutions:
  name: home-assistant-glow-ea93f8
  # Define the GPIO pins
  pulse_pin: GPIO26 
  status_led: GPIO19
  led_pin_red: GPIO5
  led_pin_green: GPIO18
packages:
  klaasnicolaas.home-assistant-glow: github://klaasnicolaas/home-assistant-glow/home-assistant-glow/esp32.yaml@main
esphome:
  name: ${name}
  name_add_mac_suffix: false
api:
  encryption:
    key: 7BGZNKt2aIjU2+s2Tful9WWPjfekbwxSTRoMBqulTMU=


wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
```

```yaml
# ta program je delal,
# vendar na vsake toliko ni ok moč kW

substitutions:
  name: home-assistant-glow-ea93f8
  device_name: home-assistant-glow
  friendly_name: Home Assistant Glow
  project_version: "4.2.3"
  device_description: "Measure your energy"
  # Define the GPIO pins
  pulse_pin: GPIO26
  status_led: GPIO5
  led_pin_red: GPIO2
  led_pin_green: GPIO4


#packages:
#  klaasnicolaas.home-assistant-glow: github://klaasnicolaas/home-assistant-glow/home-assistant-glow/esp32.yaml@main
esp32:
  board: esp32dev
  framework:
    type: arduino

esphome:
  name: ${name}
  name_add_mac_suffix: False
  comment: '${device_description}'
  min_version: 2024.6.0
  project:
    name: "klaasnicolaas.home-assistant-glow"
    version: "${project_version}"

dashboard_import:
  package_import_url: github://klaasnicolaas/home-assistant-glow/home-assistant-glow/esp32.yaml@main

packages:
  remote_package:
    url: https://github.com/klaasnicolaas/home-assistant-glow/
    ref: "4.2.3"
    files:
      - components/basis.yaml
#      - components/updates.yaml
      - components/status_led.yaml
      - components/pulse_meter.yaml

api:
  encryption:
    key: 7BGZNKt2aIjU2+s2Tful9WWPjfekbwxSTRoMBqulTMU=

# Enable logging
logger:

# Allow provisioning Wi-Fi via serial
improv_serial:

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  ap:
    ssid: '${friendly_name}'

# In combination with the `ap` this allows the user
# to provision wifi credentials to the device via WiFi AP.
captive_portal:

# Local Web Server running on port 80
web_server:
  id: esphome_web_server
  version: 3

```

### Temperature sensor - sensor

```yaml
esphome:
  name: wemos-01
  friendly_name: WeMos_01
  on_boot: 
    then:
    - output.turn_off: gpio_d1
    - output.turn_on:  gpio_d2

esp8266:
  board: esp01_1m

# Enable logging
logger:

# Enable Home Assistant API
api:
  encryption:
    key: "o1bvmPgdspkGbUmACoYD/koUbsLpif0Q8FZMFcdQzfc="

ota:
  - platform: esphome
    password: "91a790ba587af5c17d91a6f75bc5ffdd"

wifi:
  networks:
    - ssid: !secret main_wifi_ssid
      password: !secret main_wifi_password
    - ssid: !secret extended_wifi_ssid
      password: !secret extended_wifi_password 

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Wemos-01 Fallback Hotspot"
    password: "StYrNzepoY8z"

captive_portal:

web_server:

output:
  - platform: gpio
    pin: GPIO05
    id: gpio_d1
  - platform: gpio
    pin: GPIO04
    id: gpio_d2

sensor:
  - platform: ntc
    sensor: temp_volt_divider
    calibration:
      b_constant: 3435
      reference_temperature: 25°C
      reference_resistance: 5.0kOhm
    name: "TTF-502"

  - platform: resistance
    id: temp_volt_divider
    sensor: adc_pin
    configuration: DOWNSTREAM
    resistor: 4.7kOhm
    reference_voltage: 3.2V
    name: "TTF-502 resistance"

  - platform: adc
    pin: A0
    name: "ADC Pin"
    id: adc_pin
    update_interval: 10s
    filters:
      - multiply: 3.05

deep_sleep:
  run_duration: 10s
  sleep_duration: 10min
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

## Tuya

Gleja nastavitve za pridobitev LocalKey:
- https://github.com/jasonacox/tinytuya#setup-wizard---getting-local-keys

## ApexCharts


