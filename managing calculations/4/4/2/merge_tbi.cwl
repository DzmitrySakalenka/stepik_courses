cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: ShellCommandRequirement
  - class: InlineJavascriptRequirement

inputs:
  input_vcf_gz:
    type: File

  input_vcf_gz_tbi:
    type: File

outputs:
  output_file:
    type: File
    outputBinding:
      glob: $(inputs.input_vcf_gz.basename)
    secondaryFiles:
      - .tbi

baseCommand: []

arguments:
  - cp
  - $(inputs.input_vcf_gz)
  - $(inputs.input_vcf_gz.basename)
  - ';'
  - cp
  - $(inputs.input_vcf_gz_tbi)
  - $(inputs.input_vcf_gz.basename).tbi
