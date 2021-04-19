cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: ShellCommandRequirement
  - class: InlineJavascriptRequirement
  - class: InitialWorkDirRequirement
    listing: [ $(inputs.input_vcf_gz) ]

inputs:
  input_vcf_gz:
    type: File

outputs:
  output_file:
    type: File
    outputBinding:
      glob: $(inputs.input_vcf_gz.basename).tbi


baseCommand: []

arguments:
  - tabix
  - -p
  - vcf
  - $(inputs.input_vcf_gz.basename)
