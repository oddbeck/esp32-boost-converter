from esphome.components import custom
import esphome.config_validation as cv

CODEOWNERS = ["@yourgithub"]

# This registers the C++ class so ESPHome knows to compile it
custom.custom_component_schema(cv.Schema({}))