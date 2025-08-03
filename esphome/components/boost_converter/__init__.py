import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import custom
from esphome.const import CONF_ID

BOOST_CONVERTER_ID = cg.declare_id("BoostConverter")

BOOST_CONVERTER_SCHEMA = cv.Schema({})

def to_code(config):
    cg.add_library('boost_converter')
