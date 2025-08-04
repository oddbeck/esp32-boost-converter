import esphome.config_validation as cv
import esphome.codegen as cg

from esphome.const import CONF_ID

example_component_ns = cg.esphome_ns.namespace("my_component")
MyComponent = example_component_ns.class_("MyComponent", cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(MyComponent),
})


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    await cg.register_component(var, config)

    # cg.add(var.set_foo(config[CONF_FOO]))
    # if bar := config.get(CONF_BAR):
    #     cg.add(var.set_bar(bar))
    # if baz := config.get(CONF_BAZ):
    #     cg.add(var.set_baz(baz))