cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: ShellCommandRequirement
  - class: InlineJavascriptRequirement

inputs:
  reference_gen_for_sam:
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
      glob: $(inputs.input_bam_bai.nameroot + "_sam.vcf")

baseCommand: []

arguments:
  - samtools
  - mpileup
  - -uf
  - $(inputs.reference_gen_for_sam)
  - $(inputs.input_bam_bai)
  - '|'
  - bcftools
  - view
  - -vcg
  - '-'
  - '>'
  - $(inputs.input_bam_bai.nameroot + "_sam.vcf")
