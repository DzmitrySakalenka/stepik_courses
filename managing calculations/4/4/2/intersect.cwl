cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: ShellCommandRequirement
  - class: InlineJavascriptRequirement

inputs:
  input_sam:
    type: File
    secondaryFiles:
      - .tbi

  input_fre:
    type: File
    secondaryFiles:
      - .tbi

  input_hap:
    type: File
    secondaryFiles:
      - .tbi    

  input_bam:
    type: File
    secondaryFiles:
      - .bai

outputs:
  output_file:
    type: File
    outputBinding:
      glob: $(inputs.input_bam.nameroot+".vcf")

baseCommand: []

arguments:
  - vcf-isec
  - -f
  - -n
  - '+2'
  - $(inputs.input_sam)
  - $(inputs.input_fre)
  - $(inputs.input_hap)
  - '>'
  - $(inputs.input_bam.nameroot+".vcf")
