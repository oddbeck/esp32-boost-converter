#include "my_component.h"
#include "esphome/core/log.h"

namespace esphome {
namespace my_component {

static const char *const TAG = "my_component";

void BoostConverter::setup() {
  ESP_LOGI(TAG, "Setting up MyComponent");
}

void BoostConverter::loop() {
  ESP_LOGD(TAG, "Looping MyComponent");
}

}  // namespace my_component
}  // namespace esphome