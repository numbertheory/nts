# Argument Parse

## Example

```
description: "Top Level Description of whole function" 
arguments:
  - name: config
    required: False
    type: string
    multiple: False
    flags:
      - c
      - config
    help: "set path to config file"
  - name: number
    required: False
    type: integer
    multiple: False
    flags:
      - n
      - number
    help: "use a number"
  - name: flag
    required: False
    default: False
    type: boolean
    flags:
      - f
      - flag
    help: "set a flag"
```
