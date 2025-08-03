#include "esphome.h"

class BoostConverter : public Component {
 public:
  BoostConverter(LEDCOutput *pwm) : pwm_(pwm) {}

  void setup() override {
    adc1_config_width(ADC_WIDTH_BIT_12);  // 12-bit ADC
    adc1_config_channel_atten(ADC1_CHANNEL_0, ADC_ATTEN_DB_11); // GPIO0 = ADC1_CHANNEL_0
  }

  void loop() override {
    static uint32_t last_check = 0;
    uint32_t now = micros();

    // Run every 200 µs
    if (now - last_check < 200)
      return;
    last_check = now;

    // Read raw ADC (0-4095)
    int raw = adc1_get_raw(ADC1_CHANNEL_0);
    float voltage = (float)raw / 4095.0f * 3.3f;  // Scale to voltage

    // Optional debug
    // ESP_LOGD("BOOST", "Voltage: %.2f V", voltage);

    // Turn off PWM if voltage is low
    if (voltage < 2.5f) {
      pwm_->set_level(0.0f);
    } else {
      pwm_->set_level(0.5f);  // Adjust for desired duty cycle
    }
  }

 protected:
  LEDCOutput *pwm_;
};