import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output
from esphome.const import CONF_ID

empty_binary_output_ns = cg.esphome_ns.namespace("example_component")
EmptyBinaryOutput = empty_binary_output_ns.class_(
    "ExampleComponent", output.BinaryOutput, cg.Component
)

CONFIG_SCHEMA = output.BINARY_OUTPUT_SCHEMA.extend(
    {
        cv.Required(CONF_ID): cv.declare_id(EmptyBinaryOutput),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await output.register_output(var, config)
    await cg.register_component(var, config)