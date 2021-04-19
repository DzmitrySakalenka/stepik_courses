cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: ShellCommandRequirement
  - class: InlineJavascriptRequirement

inputs:
  reference_gen_for_hap:
    type: File
    secondaryFiles:
      - .fai

  reference_dict:
    type: File

outputs:
  output_file:
    type: File
    outputBinding:
      glob: $(inputs.reference_gen_for_hap.basename)
    secondaryFiles:
      - .fai
      - ^.dict

baseCommand: []

arguments:
  - cp
  - $(inputs.reference_gen_for_hap)
  - $(inputs.reference_gen_for_hap.basename)
  - ';'
  - cp
  - $(inputs.reference_gen_for_hap.path).fai
  - $(inputs.reference_gen_for_hap.basename).fai
  - ';'
  - cp
  - $(inputs.reference_dict)
  - $(inputs.reference_gen_for_hap.nameroot).dict
