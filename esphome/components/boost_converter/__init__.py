# import esphome.codegen as cg
# import esphome.config_validation as cv
# from esphome.components import custom
# from esphome.const import CONF_ID

# BOOST_CONVERTER_ID = cg.declare_id("BoostConverter")

# BOOST_CONVERTER_SCHEMA = cv.Schema({})

# def to_code(config):
#     cg.add_library('boost_converter')

import esphome.config_validation as cv
import esphome.codegen as cg

from esphome.const import CONF_ID

CONF_FOO = "foo"
CONF_BAR = "bar"
CONF_BAZ = "baz"

example_component_ns = cg.esphome_ns.namespace("BoostConverter")
BoostConverterComponent = example_component_ns.class_("BoostConverter", cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(BoostConverterComponent),
    # cv.Required(CONF_FOO): cv.boolean,
    # cv.Optional(CONF_FOO): cv.boolean,
    # cv.Optional(CONF_BAR): cv.string,
    # cv.Optional(CONF_BAZ): cv.int_range(0, 255),
})


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    await cg.register_component(var, config)

    # cg.add(var.set_foo(config[CONF_FOO]))
    # if bar := config.get(CONF_BAR):
    #     cg.add(var.set_bar(bar))
    # if baz := config.get(CONF_BAZ):
    #     cg.add(var.set_baz(baz))