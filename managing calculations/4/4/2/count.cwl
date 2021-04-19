cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: ShellCommandRequirement
  - class: InlineJavascriptRequirement

inputs:
  input_common_var:
    type: File

outputs:
  output_file:
    type: stdout

baseCommand: []

arguments:
  - grep
  - -v
  - "^#"
  - -c
  - $(inputs.input_common_var)

stdout: $(inputs.input_common_var.nameroot+"_count.txt")
