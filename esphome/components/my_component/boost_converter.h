#pragma once

#include "esphome/core/component.h"

namespace esphome {
namespace my_component {

class MyComponent : public Component {
 public:
  void setup() override;
  void loop() override;
};

}  // namespace my_component
}  // namespace esphome