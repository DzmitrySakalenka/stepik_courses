cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: ShellCommandRequirement
  - class: InlineJavascriptRequirement

inputs:
  reference_gen_for_fre:
    type: File
    secondaryFiles:
      - .fai

  input_bam_bai:
    type: File
    secondaryFiles:
      - .bai

outputs:
  output_file:
    type: File
    outputBinding:
      glob: $(inputs.input_bam_bai.nameroot + "_fre.vcf")

baseCommand: []

arguments:
  - freebayes
  - -f
  - $(inputs.reference_gen_for_fre)
  - $(inputs.input_bam_bai)
  - '>'
  - $(inputs.input_bam_bai.nameroot + "_fre.vcf")
