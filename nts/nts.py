#! /usr/bin/env python3

import argument_parse.collect

d = argument_parse.collect.Arguments("arguments.yaml")
print(d.value("config"))
print(d.value("number"))
print(d.value("flag"))
