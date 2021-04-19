class: CommandLineTool
cwlVersion: v1.0

requirements:
  - class: InlineJavascriptRequirement

inputs:
  input_file:
    type: File
    inputBinding:
      loadContents: True

outputs:
  output_file:
    type: File
    outputBinding:
      glob: $(inputs.input_file.basename)

baseCommand: printf
stdout: $(inputs.input_file.basename)

arguments:
  - ${ return ("Hello " + (inputs.input_file.contents) + "!") }